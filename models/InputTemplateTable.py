from core import *
from models.Database import Database
from models.MessageDialogBox import MessageDialogBox



class WorkerThread(QObject):
    finished = Signal()
    values_data = Signal(pd.DataFrame)  # dataframe
    progressbar_value = Signal(int)
    progressbar_text = Signal(str)
    valid_signal = Signal(list)
    headers = Signal(list)
    rows_count = Signal(int)
    log_info = Signal(str)

    def __init__(self, path, template_name, AppConfig,parent=None):
        super().__init__(parent)

        self.path_xlsx = path
        self.template_name = template_name
        self.valid = False
        self.type_file = None
        self.dba = Database()
        self.app_config = AppConfig
        
        ##
        self._default_encoding = self.app_config.get_default_encoding()

                



    def run(self):


        if self._default_encoding == "auto":
            try:
                self._default_encoding = open(self.path_xlsx).encoding
                self.log_info.emit(f"Input-Encoding do arquivo: {self._default_encoding}")   
                self.app_config._encoding_current_file = self._default_encoding
            except Exception as e:
                self.log_info.emit(f"Input-Error ao obter encoding do arquivo: {e}")
                self.log_info.emit("Input-Será utilizado o encoding padrão: utf_8")
                self._default_encoding = 'utf_8'
        else:
            self.log_info.emit(f"Input-Encoding Manual in Settings: {self._default_encoding}")


        self.valid = self._ValidaPathXlsx()
        if self.valid[0]:
            self._SetTable()
            self.valid_signal.emit(self.valid)
            self.finished.emit()
            return True
        else:
            self.valid_signal.emit(self.valid)
            self.finished.emit()
            print("error input template")
            return False

    def _ValidaPathXlsx(self):

        if os.path.exists(self.path_xlsx):
            if self.template_name:
                if self.dba.template_exists(self.template_name):
                    valid, count_db, coutn_excel = self._ValidaHeadersTemplate()
                    if valid:
                        return [True, "Planilha Valida!"]
                    else:
                        text = [False, "Planilha Invalida!",
                                f" A quantidade de campos do template {self.template_name} possui : {count_db}\n E a Planilha Importada Possui: {coutn_excel} \n Verifique os campos da planilha importada "]
                        return text
                else:
                    return False
            else:
                return False
        else:
            return False

    def _ValidaHeadersTemplate(self):
        try:
            colluns_template_db = int(
                self.dba.template_num_colls(self.template_name)[0][0])
            colluns_template_model_xlsx = int(self._GetNumColumnsFromExcel())

            if colluns_template_db == colluns_template_model_xlsx:
                return [True, 0, 0]
            else:
                return [False, colluns_template_db, colluns_template_model_xlsx]

        except Exception as e:
            return False

    def _GetNumColumnsFromExcel(self):

        if self.path_xlsx.endswith('.xlsx'):
            try:
                workbook = xl.load_workbook(
                    self.path_xlsx, read_only=True, data_only=True)
                sheet = workbook.active
                num_columns = sheet.max_column

                self.file_type = 'xlsx'

                return num_columns
            except Exception as e:
                return 0
        elif self.path_xlsx.endswith('.csv'):
            try:
                df = pd.read_csv(self.path_xlsx, sep=';')
                num_columns = len(df.columns)

                self.file_type = 'csv'

                return num_columns
            except Exception as e:
                return 0

        elif self.path_xlsx.endswith('.xls'):
            try:
                xlsread = xlrd.open_workbook(self.path_xlsx)
                sheet = xlsread.sheet_by_index(0)
                num_columns = sheet.ncols

                self.file_type = 'xls'

                return num_columns
            except Exception as e:
                return 0

    def _SetTable(self):
        headers = [i[0]
                   for i in self.dba.select_camposnome_template(self.template_name)]
        random_name = str(uuid.uuid4())  # random name for the temporary CSV

        self.log_info.emit("Loading Spreadsheet...")
        self.log_info.emit(f"Random Name: {random_name} in {self.path_xlsx}")

        def xlsx_xls_to_csv(path_xlsx, path_csv):
            path_xlsx = os.path.abspath(path_xlsx)
            path_csv = os.path.abspath(path_csv)

            excel = win32.gencache.EnsureDispatch('Excel.Application')
            wb = excel.Workbooks.Open(path_xlsx)
            wb.SaveAs(path_csv, FileFormat=6)
            wb.Close(False)
            excel.Application.Quit()

            self.log_info.emit("CSV Converted using Engine:w32com")
            return True

        def xlsx_xls_to_csv2(path_xlsx, path_csv):
            path_xlsx = os.path.abspath(path_xlsx)
            path_csv = os.path.abspath(path_csv)
            self.log_info.emit("Trying to convert using Xlsx2csv...")
            try:
                
                Xlsx2csv(path_xlsx,
                         outputencoding=self._default_encoding,
                         dateformat='%d/%m/%Y',
                         delimiter=';'
                         ).convert(path_csv)
                
                self.log_info.emit("Sucess! Using Engine Xlsx2csv")
            except Exception as e:
                self.log_info.emit(f"Error ao converter Using Engine Xlsx2csv: {e}")
                return False

        def load_dataframe(file_type):
            try:

                if file_type == 'xlsx' or file_type == 'xls':
                    # logger
                    self.log_info.emit(
                        f"File is {file_type} Converting Spreadsheet to CSV...")

                    path_csv = os.path.join(
                        os.getcwd(), f'{str(random_name)}.csv')

                    try:
                        xlsx_xls_to_csv(self.path_xlsx, path_csv)
                    except Exception as e:
                        self.log_info.emit(
                            f"An error occurred while converting the spreadsheet to CSV using Engine:w32com: {e}")
                        xlsx_xls_to_csv2(self.path_xlsx, path_csv)

                    df = pd.read_csv(path_csv, sep=';', dtype=str, encoding_errors='ignore',
                                     low_memory=False, keep_default_na=False, encoding=self._default_encoding)
                    self.log_info.emit("CSV Buffer DF Loaded, Removing CSV...")

                    os.remove(path_csv)

                    self.log_info.emit("CSV Removed!")
                    self.log_info.emit("Sucess!")

                elif file_type == 'csv':
                    self.log_info.emit("File is CSV, Loading CSV...")
                    df = pd.read_csv(self.path_xlsx, sep=';', dtype=str, encoding_errors='ignore',
                                     low_memory=False, keep_default_na=False, encoding=self._default_encoding)
                else:
                    raise ValueError("Unsupported file type")
            except Exception as e:
                # logger
                self.log_info.emit(f"Error {e} ")
                self.log_info.emit(
                    "Error ao converter Planilha para CSV, será carregado o formato original...")

                if file_type == 'xlsx' or file_type == 'xls':
                    df = pd.read_excel(self.path_xlsx, dtype=str)

                elif file_type == 'csv':
                    df = pd.read_csv(self.path_xlsx, sep=';', dtype=str, encoding_errors='ignore',
                                     low_memory=False, keep_default_na=False, encoding=self._default_encoding)
                else:
                    raise ValueError("Unsupported file type")

            df = df.fillna('')
            df = df.rename(columns=dict(zip(df.columns, headers)))
            return df

        if self.file_type in ['xlsx', 'csv', 'xls']:
            try:
                self.progressbar_text.emit(
                    f"Por favor espere, Carregando {self.file_type.upper()} em memória...")
                df = load_dataframe(self.file_type)
                self.values_data.emit(df)
                self.progressbar_text.emit("Carregando Dados...")
                self.headers.emit(df.columns.tolist())
                self.progressbar_text.emit("Carregando Colunas...")
                self.rows_count.emit(len(df.index))
                self.progressbar_text.emit("Carregando Linhas...")
                self.progressbar_text.emit("Planilha Carregada com Sucesso!")
                self.progressbar_value.emit(100)
                return True
            except Exception as e:
                self.log_info.emit(f"Error ao carregar Planilha: {e}")
                return False
        else:
            self.log_info.emit(
                f"Unsupported file type selected: {self.file_type}")
            return False


class ExcelTableModel(QAbstractTableModel):
    def __init__(self, data=None, headers=None):
        super().__init__()
        self._data = data or []
        self._headers = headers or []

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._headers)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            row = index.row()
            col = index.column()

            return str(self._data[row][col])
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._headers[section])
            if orientation == Qt.Vertical:
                return str(section + 1)
        return None


class TemplateInput(QTableView):
    progressbar_value = Signal(int)
    progressbar_text = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.path_xlsx = None
        self.template_name = None

        self.modelo = ExcelTableModel()
        self.setModel(self.modelo)

        self._headers = None
        self._data = pd.DataFrame()

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
        # tamanho da linha e coluna de acordo com o texto

        # DISABLE EDIT
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setFocusPolicy(Qt.NoFocus)

        self.dba = Database()

    def _GetPath(self):
        return self.path_xlsx

    def _GetTemplateName(self):
        return self.template_name

    def _Set_Data(self, dataframe: pd.DataFrame):
        self._data = dataframe

        rows = self._data.values.tolist()
        col = self._data.columns.tolist()

        self.modelo = ExcelTableModel(rows, col)
        self.setModel(self.modelo)

    def _Get_Data(self) -> pd.DataFrame:
        return self._data
