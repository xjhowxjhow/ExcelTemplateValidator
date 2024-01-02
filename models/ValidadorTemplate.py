from core import *
from models.Database import Database
from models.AppConfig import AppConfig


class ColoredItemDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.background_color = {}  

    def setCellColor(self, row, col, color):
        self.background_color[(row, col)] = color

    def getCellColor(self, row, col):
        return self.background_color.get((row, col), None)

    def paint(self, painter, option, index):
        painter.save()

        row = index.row()
        col = index.column()

        if (row, col) in self.background_color:
            painter.fillRect(option.rect, self.background_color[(row, col)])
        else:

            painter.fillRect(option.rect, QColor(255, 255, 255))



        painter.drawText(option.rect.adjusted(10, 0, 0, 0), Qt.AlignLeft | Qt.AlignVCenter, index.data())
        painter.setPen(QPen(Qt.black, 0, Qt.SolidLine))
        painter.drawRect(option.rect)


        if option.state & QStyle.State_Selected:
            painter.setPen(QPen(Qt.blue, 0, Qt.SolidLine))
            painter.drawRect(option.rect)


        if option.state & QStyle.State_HasFocus:
            painter.setPen(QPen(Qt.red, 0, Qt.SolidLine))
            painter.drawRect(option.rect)


        painter.restore()
    


class ExcelTableModel(QAbstractTableModel):
    def __init__(self, data, headers, parent=None):
        super().__init__(parent)
        self._data = data
        self._headers = headers
        self._tooltips = [
            ['' for _ in range(len(headers))] for _ in range(len(data))]

    def rowCount(self,  parent=None):
        return len(self._data)

    def columnCount(self,  parent=None):
        return len(self._headers)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        row = index.row()
        col = index.column()

        if role == Qt.DisplayRole:
            return str(self._data[row][col])
        elif role == Qt.ToolTipRole:
            return str(self._tooltips[row][col])

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._headers[section])
            if orientation == Qt.Vertical:
                return str(section + 1)
        return None

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def setTooltip(self, row, col, tooltip):
        self._tooltips[row][col] = tooltip
        topLeft = self.index(row, col)
        bottomRight = self.index(row, col)
        self.dataChanged.emit(topLeft, bottomRight)



class WorkerSignals(QObject):
    finished = Signal()
    finished_erros = Signal(int)
    progressbar_value = Signal(int)
    progressbar_text = Signal(str)
    change_none_to_empty = Signal(list)
    change_color = Signal(list)
    set_tooltip = Signal(list)
    set_logger = Signal(dict)
    painter_rows = Signal(list)
    validate_duplicatas = Signal()





class WorkerThreadValidacao(QRunnable):
    def __init__(self,dataframe: pd.DataFrame, template_name, parent=None,start=int, end=int,number_thread=int):
        super().__init__(parent)

        self.start_index = start
        self.end_index = end
        self.data = dataframe
        self.number_thread = number_thread
        self.template_name = template_name
        self.dba = Database()
        self.qt_erros = 0
        self.dict_erros_temp = {"erros": []}
        self.signals =WorkerSignals()

        
        # CONFIG APP
        # ////////////////////////////////////////////////////////////////
        self.app_config = AppConfig()
        self.setAutoDelete(True)


    def run(self):
        try:
            self.dict_erros_temp = {"erros": []}
            self.qt_erros = 0
            self.signals.progressbar_text.emit(f"Validando Linhas...")
            


            #------------------------------------------------------------
            obrigatorio_columns = {col: self._VerifyObrigatorio(col) for col in self.data.columns}
            type_columns = {col: self._VerifyTypeField(col) for col in self.data.columns}
            tamanho_columns = {col: self._VerifyTamanho(col) for col in self.data.columns}
            only_list_values_columns = {col: self._VerifyOnlyListValues(col) for col in self.data.columns}
            unique_values_columns = {col: self._VerifyUniqueValues(col) for col in self.data.columns}

            for col in self.data.columns:
                obrigatorio_f = obrigatorio_columns[col]
                type_f = type_columns[col]
                tamanho_f = tamanho_columns[col]
                only_list_values_f = only_list_values_columns[col]
                unique_values_f = unique_values_columns[col]
                column = self.data[col]

                self._process_column(field_name=col, column=column, obrigatorio_f=obrigatorio_f, type_f=type_f, tamanho_f=tamanho_f, only_list_values_f=only_list_values_f, unique_values_f=unique_values_f)

                    
                count_collumns = self.data.columns.shape[0]
                columns_actally = self.data.columns.tolist().index(col) + 1
                progress_percent = int((columns_actally / count_collumns) * 100)
                self.signals.progressbar_value.emit(progress_percent)
                self.signals.progressbar_text.emit(f"job Validando Coluna nome: {col} - {columns_actally}/{count_collumns} - {progress_percent}%")

            


        except Exception as e:
            print(e)
            # self.signals.validate_duplicatas.emit()
            self.signals.finished.emit()


        if self.dict_erros_temp["erros"] != []:
            self.signals.set_logger.emit([self.number_thread ,self.dict_erros_temp])


        self.signals.finished_erros.emit(self.qt_erros)
        # self.signals.validate_duplicatas.emit()
        self.signals.finished.emit()





    def _process_column(self, field_name, column:pd.Series, obrigatorio_f, type_f, tamanho_f, only_list_values_f, unique_values_f):



        series = column                         # aplica a as validacoes para cada coluna 
        series_empty = series.eq("").all()      #verifica se toda a coluna é uma string vazia
        
        #// Coluna Obrigatória e toda Vazia
        if obrigatorio_f == "1" and series_empty: 
                                                                                                                                    
            self._AppendErros(row=series.index, col=field_name, field_name=field_name, error="Campo Obrigatorio não pode ser vazio")      # adiciona todos os indices da coluna que são vazios passa o range
            self.qt_erros += series.shape[0] 

        #// Coluna Não Obrigatória e toda Vazia
        elif obrigatorio_f == "0" and series_empty:
            pass

        #// Coluna Não Obrigatória e Obrigatorias Com Valores
        elif obrigatorio_f == "0" and not series_empty or obrigatorio_f == "1" and not series_empty:
            
            #ignora indices vazios apenas para colunas não obrigatorias
            if obrigatorio_f == "0":
                series = series[series.ne("")] 
                series = series[series.notnull()]
        
            if obrigatorio_f == "1" and not series_empty:

                series_null = series[series.eq("")]
                if series_null.shape[0] > 0:
                    self._AppendErros(row=series_null.index, col=field_name, field_name=field_name, error="Campo Obrigatorio não pode ser vazio")
                    self.qt_erros += series_null.shape[0]
                
                series = series[series.ne("")]
            
            #// Verifica se o tipo da coluna é válido
            series_type = series.apply(lambda x: self._ValidaTipo(tipo=type_f, valor=x))
            series_type = series_type[series_type == False]
            if series_type.shape[0] > 0:
                self._AppendErros(row=series_type.index, col=field_name, field_name=field_name, error=f"Tipo Inválido Esperado: {type_f}")
                self.qt_erros += series_type.shape[0]

            #// Verifica se o tamanho da coluna é válido
            series_tamanho = series.apply(lambda x: self._ValidaTamanho(tamanho_real=tamanho_f, valor=x))
            series_tamanho = series_tamanho[series_tamanho == False]
            if series_tamanho.shape[0] > 0:
                self._AppendErros(row=series_tamanho.index, col=field_name, field_name=field_name, error=f"Tamanho Inválido Esperado: {tamanho_f}")
                self.qt_erros += series_tamanho.shape[0]

            #// Verifica se o valor da coluna é válido
            if only_list_values_f == "1":
                list_values = self._VerifyListValues(field_name).split(";") # lista de valores validos para essa coluna
                
                def check_in_list(valor):
                    return valor.upper() in list_values
                
                series_only_list_values = series.apply(lambda x: check_in_list(x))
                series_only_list_values = series_only_list_values[series_only_list_values == False]
                if series_only_list_values.shape[0] > 0:
                    self._AppendErros(row=series_only_list_values.index, col=field_name, field_name=field_name, error=f"Valor inválido, não está na lista de valores válidos")
                    self.qt_erros += series_only_list_values.shape[0]

                
            #// Verifica se os valores da coluna são únicos
            if unique_values_f == "1":
                series_unique_values = series[series.duplicated(keep=False)]
                if series_unique_values.shape[0] > 0:
                    self._AppendErros(row=series_unique_values.index, col=field_name, field_name=field_name, error=f"Coluna de valores Unico, esse valor está duplicado")
                    self.qt_erros += series_unique_values.shape[0]

            
            #// Fim das validações
        






    def _AppendErros(self, row, col, field_name, error):
        self.dict_erros_temp["erros"].extend([{"row": r, "col": col, "field_name": field_name, "error": error} for r in row])





    def _VerifyEmptyField(self, valor):
        value_item = str(valor).strip()
        if value_item in ["", None, "None"]:
            return True
        return False

    def _ValidaUniqueValues(self, row, col, valor):

        for r in range(len(self.data)):
            if r == row:
                continue
            if self.data[r][col] == valor:
                return r

        return None  # Retorna None se o valor for único

    def _VerifyTypeField(self, fild_name):
        data = self.dba.type_field(self.template_name, fild_name)
        return data

    def _VerifyObrigatorio(self, fild_name):
        data = self.dba.obrigatorio_field(self.template_name, fild_name)
        return data

    def _VerifyTamanho(self, fild_name):
        data = self.dba.tamanho_field(self.template_name, fild_name)
        return data

    def _VerifyOnlyListValues(self, fild_name):
        data = self.dba.only_list_values_field(self.template_name, fild_name)
        return data

    def _VerifyListValues(self, fild_name):
        data = self.dba.list_values_field(self.template_name, fild_name)
        return data

    def _VerifyUniqueValues(self, fild_name):
        data = self.dba.unique_values_field(self.template_name, fild_name)
        return data

    def _ValidaVarchar(self, valor):
        if valor == "":
            return False
        else:
            return True

    def _ValidaInteger(self, valor):
        try:
            int(str(valor))
            return True
        except ValueError:
            return False

    def _ValidaDate(self, valor):
        try:
            formats = ["%d/%m/%Y"]
            for format in formats:
                try:
                    datetime.strptime(valor, format)
                    return True
                except:
                    pass
            return False
        except Exception as e:
            return False

    def _ValidaDatetime(self, valor):
        try:
            formats = ["%d/%m/%Y %H:%M", "%d/%m/%Y %H:%M:%S", "%d/%m/%Y %H:%M:%S.%f",]
            for format in formats:
                try:
                    datetime.strptime(valor, format)
                    return True
                except:
                    pass
            return False
        except Exception as e:
            return False

    def _ValidaNumber(self, valor):

        SETTINGS_NUMBER = self.app_config.get_number_type()
        if SETTINGS_NUMBER == "a":
            # ACEita tanto 1,0 quanto 1.0
            pattern = r'^[+-]?\d+(\.\d+)?$|^[+-]?\d+(\,\d+)?$'
        elif SETTINGS_NUMBER == "p":
            # aceita apenas ponto 1.0
            pattern = r'^[+-]?\d+(\.\d+)?$'
        elif SETTINGS_NUMBER == "v":
            # aceita apenas virgula 1,0
            pattern = r'^[+-]?\d+(\,\d+)?$'
        else:
            pattern = r'^[+-]?\d+(\,\d+)?$'
        try:
            if re.match(pattern, str(valor)):
                return True
            else:
                return False
        except Exception as e:
            return False

    def _ValidaBoolean(self, valor):
        return str(valor).lower() == "true" or str(valor).lower() == "false"

    def _ValidaTipo(self, tipo, valor):

        if tipo == "VARCHAR":
            return self._ValidaVarchar(valor)
        elif tipo == "INTEGER":
            return self._ValidaInteger(valor)
        elif tipo == "DATE":
            return self._ValidaDate(valor)
        elif tipo == "DATETIME":
            return self._ValidaDatetime(valor)
        elif tipo == "NUMBER":
            return self._ValidaNumber(valor)
        elif tipo == "BOOLEAN":
            return self._ValidaBoolean(valor)
        else:
            return False

    def _ValidaObrigatorio(self, valor):
        if valor == "1":
            return True
        else:
            return False

    def _ValidaOnlyListValues(self, valor):
        if valor == "1":
            return True
        else:
            return False

    # Validador Tamanho

    def _ValidaTamanho(self, tamanho_real, valor):
        try:

            if len(str(valor)) > int(tamanho_real):
                return False
            else:
                return True
        except Exception as e:
            return False

    def _ValidaObrigatorioValor(self, obrigatorio, valor):
        if obrigatorio == "1" and valor in ["", None, "None"]:
            return False
        else:
            return True


class ValidadorTemplate(QTableView):
    progressbar_value = Signal(int)
    progressbar_text = Signal(str)
    progressbar_export_value = Signal(int)
    progressbar_export_text = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.path_xlsx = None
        self.template_name = None
        self.data = None
        self.headers = None
        self.dict_erros = None

        # CONFIG MODEL
        # ////////////////////////////////////////////////////////////////
        self.modelo = ExcelTableModel([], [])
        self.setModel(self.modelo)

        # CONFIG DELEGATE
        # ////////////////////////////////////////////////////////////////
        # Criar e definir o delegate personalizado
        self.delegate = ColoredItemDelegate()
        self.setItemDelegate(self.delegate)

        # CONFIG TABLE
        # ////////////////////////////////////////////////////////////////

        self.setHorizontalHeader(QHeaderView(Qt.Horizontal))
        self.horizontalHeader().setSectionsMovable(True)
        self.horizontalHeader().setDragEnabled(True)
        self.horizontalHeader().setDragDropMode(QHeaderView.InternalMove)

        # Selection and interaction
        self.horizontalHeader().setStretchLastSection(True)
        self.setFrameShape(QFrame.NoFrame)
        self.setFrameShadow(QFrame.Raised)
        self.setEditTriggers(QAbstractItemView.CurrentChanged |
                             QAbstractItemView.DoubleClicked)
        self.setTabKeyNavigation(True)
        self.setProperty("showDropIndicator", True)
        self.setDragDropOverwriteMode(False)
        self.setAlternatingRowColors(True)
        self.setTextElideMode(Qt.ElideMiddle)
        self.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.setShowGrid(True)
        self.setGridStyle(Qt.SolidLine)
        self.setSortingEnabled(True)
        self.setCornerButtonEnabled(True)
        self.horizontalHeader().setVisible(True)
        self.horizontalHeader().setCascadingSectionResizes(False)
        self.horizontalHeader().setDefaultSectionSize(250)
        self.horizontalHeader().setProperty("showSortIndicator", True)
        self.horizontalHeader().setStretchLastSection(True)
        self.verticalHeader().setVisible(True)
        self.verticalHeader().setCascadingSectionResizes(False)
        self.verticalHeader().setHighlightSections(True)
        self.verticalHeader().setProperty("showSortIndicator", False)
        self.verticalHeader().setStretchLastSection(False)

        # DISABLE EDIT
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setFocusPolicy(Qt.NoFocus)

        self.dba = Database()

    def _LoadTemplate(self, dataframe):
        if dataframe is None:
            return False
        self.data = dataframe

        # reset table
        self.rows = dataframe.values.tolist()
        self.headers = dataframe.columns.tolist()
        self.modelo = ExcelTableModel(self.rows, self.headers)
        #reset colors cells delegate
        self.delegate.background_color = {}
        self.delegate.parent = self

        self.setModel(self.modelo)




    def _SetTollTip(self, index):
        for idx in index:
            col = self.headers.index(idx[1]) #pega o index da coluna pelo nome
            self.modelo.setTooltip(idx[0], col, idx[2])

    def _ChangeColor(self, index):
        for idx in index:
            col_name = idx[1]
            col = self.headers.index(col_name) #pega o index da coluna pelo nome
            self.delegate.setCellColor(idx[0], col, idx[2])


    # EXPORT to XLSX
    # ///////////////////////////////////////////////////////////////

    def _Get_HeadersLogicalIndexers(self):
        logical_indices = []
        header = self.horizontalHeader()
        for visual_index in range(header.count()):
            logical_col = header.logicalIndex(visual_index)
            item_text = self.model().headerData(logical_col, Qt.Horizontal, Qt.DisplayRole)
            logical_indices.append(item_text)
        return logical_indices

    def _Get_DataLogicalIndexers(self):

        items = []
        model = self.model()  # Get a reference to the model
        for row in range(model.rowCount()):
            row_items = []
            for visual_col in range(model.columnCount()):
                logical_col = self.horizontalHeader().logicalIndex(visual_col)
                index = model.index(row, logical_col)
                item_text = model.data(index, Qt.DisplayRole)
                row_items.append(item_text)
            items.append(row_items)
        return items


    # ///////////////////////////////////////////////////////////////
