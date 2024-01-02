from core import *



class ExportDataFrame(QThread):
    finished = Signal()
    progressbar_text = Signal(str)
    progressbar_value = Signal(int)
    finished_success = Signal()
    finished_error = Signal(str)
    finished_none_log = Signal(str)
    log_info = Signal(str)

    def __init__(self, dataframe: pd.DataFrame, dict_erros: dict, path: str, option_export: str, parent=None,validation_template=None,AppConfig=None):
        super().__init__(parent)
        self._dataframe = dataframe
        self._dict_erros = dict_erros
        self._path = path
        self._option_export = option_export
        self._app_config = AppConfig
        self._validador_template = validation_template
        self._default_encoding = self._app_config.get_default_encoding()
        self._default_export_format = self._app_config.get_default_export_format()


    def run(self):



        if self._default_encoding == "auto":
            try:
                self._default_encoding = self._app_config._encoding_current_file
                self.log_info.emit(f"Output-Encoding do arquivo: {self._default_encoding}")   
                self.log_info.emit(f"Output-Format in Settings: {self._default_export_format}")
            except Exception as e:
                self.log_info.emit(f"Output-Error ao obter encoding do arquivo: {e}")
                self.log_info.emit("Output-Será utilizado o encoding padrão: utf_8")
                self._default_encoding = 'utf_8'
        else:
            self.log_info.emit(f"Output-Encoding Manual in Settings: {self._default_encoding}")


        if self._option_export == 'VALIDOS':
            export = self._export_validos_to_xlsx()
            if export:
                self.finished_success.emit()
            else:
                self.finished_error.emit(export)
        elif self._option_export == 'ERROS':

            layout = self._app_config.get_default_type_export_layout() 
            export = self._export_full() if layout == 'Completa' else self._export_erros_to_excel_json()

            if export is True:
                self.finished_success.emit()
            elif export == 'EmpyError':
                self.finished_none_log.emit('Nenhum log encontrado para exportar')
            else:
                self.finished_error.emit(export)
        self.finished.emit()

    def _export_validos_to_xlsx(self):
        try:
            # Obtém os indexadores lógicos das colunas do template
            indexers = self._validador_template._Get_HeadersLogicalIndexers()

            # Reordena o DataFrame de acordo com a ordem das colunas do template
            self._dataframe = self._dataframe[indexers]

            data:pd.DataFrame = self._dataframe.copy()
            headers = data.columns.tolist()

            if self._dict_erros['erros']:
                lines_erros_ignore = [erros['row'] for erros in self._dict_erros['erros']]
                data = data.drop(lines_erros_ignore)
                data = data.astype(str)
                self.progressbar_value.emit(20)



            if self._default_export_format == 'xlsx':
                self.progressbar_value.emit(70)
                self.progressbar_text.emit('Convertendo para Excel, isso pode demorar, exportar em CSV é mais rápido')
                data.to_excel(self._path, sheet_name='resultados', index=False, header=headers, engine='xlsxwriter')
            else:
                self.progressbar_value.emit(70)
                data.to_csv(self._path, index=False, header=headers, sep=';', encoding=self._default_encoding)
            return True

            

        except Exception as e:
            return f'Erro ao exportar log para Excel\n{e}'
        
    def _export_erros_to_excel_json(self):
        
        if self._dict_erros is None:
            return 'EmptyError - Nenhum log encontrado para exportar'

        try:


            if self._dict_erros['erros']:
                if self._path:
                    if self._default_export_format == 'xlsx':
                        wb = xl.Workbook()
                        ws = wb.active

                        # CABEÇALHO
                        ws['A1'] = 'LINHA'
                        ws['B1'] = 'COLUNA'
                        ws['C1'] = 'ERRO'

                        # DADOS
                        row = 2

                        for erro in self._dict_erros['erros']:
                            ws.cell(row=row, column=1).value = erro['row'] + 1
                            ws.cell(row=row, column=2).value = erro['field_name']
                            ws.cell(row=row, column=3).value = erro['error']
                            row += 1
                            self.progressbar_value.emit((row / len(self._dict_erros['erros'])) * 100)
                            # texto de progresso
                            self.progressbar_text.emit(f"Exportando Linhas com Erros: {row} de {len(self._dict_erros['erros'])}")

                        wb.save(self._path)
                        return True

                    elif self._default_export_format == 'csv':
                        with open(self._path, 'w', newline='', encoding=self._default_encoding) as csvfile:
                            csv_writer = csv.writer(csvfile)

                            # CABEÇALHO
                            csv_writer.writerow(['LINHA', 'COLUNA', 'ERRO'])

                            # row 
                            row = 1
                    

                            # DADOS
                            for erro in self._dict_erros['erros']:
                                csv_writer.writerow([erro['row'] + 1, erro['field_name'], erro['error']])
                                row += 1
                                self.progressbar_value.emit((row / len(self._dict_erros['erros'])) * 100)
                                # texto de progresso
                                self.progressbar_text.emit(f"Exportando Linhas com Erros: {row} de {len(self._dict_erros['erros'])}")

                        return True

            else:
                return 'EmptyError'

        except Exception as e:
            return f'Erro ao exportar log para {self._default_export_format}\n{e}'
        
    def _export_full(self):
        try:
            # Obtém os indexadores lógicos das colunas do template
            indexers = self._validador_template._Get_HeadersLogicalIndexers()

            # Reordena o DataFrame de acordo com a ordem das colunas do template
            self._dataframe = self._dataframe[indexers]

            data:pd.DataFrame = self._dataframe.copy()
            headers = data.columns.tolist()
            headers.append('QUANTIDADE_ERROS')
            headers.append('ERRO_DESCRICAO')

            if self._dict_erros['erros']:
                new_col = [erros['row'] for erros in self._dict_erros['erros']]
                set_new_col = set(new_col)
                new_col = list(set_new_col)
                new_col.sort()


                data['QUANTIDADE_ERROS'] = 0
                data['QUANTIDADE_ERROS'] = data['QUANTIDADE_ERROS'].astype(int)
                data['ERRO_DESCRICAO'] = ''
                data['ERRO_DESCRICAO'] = data['ERRO_DESCRICAO'].astype(str)
                for i in new_col:
                    # Inicializa error_desc como uma string vazia
                    error_desc = ""

                    # Pega todos os erros da linha
                    erros = [erros for erros in self._dict_erros['erros'] if erros['row'] == i]

                    # Pega para cada chave a coluna col e error
                    for col, error in zip([erros['col'] for erros in erros], [erros['error'] for erros in erros]):
                        error_desc += f"Coluna: {col} Erro: {error} Linha: {i} |"

                    data.loc[i, 'QUANTIDADE_ERROS'] = len(erros)
                    data.loc[i, 'ERRO_DESCRICAO'] = error_desc

                data = data.astype(str)

            else:
                data['QUANTIDADE_ERROS'] = 0
                data['QUANTIDADE_ERROS'] = data['QUANTIDADE_ERROS'].astype(int)
                data['ERRO_DESCRICAO'] = ''
                data['ERRO_DESCRICAO'] = data['ERRO_DESCRICAO'].astype(str)


            if self._default_export_format == 'xlsx':
                    
                    self.progressbar_value.emit(70)
                    self.progressbar_text.emit('Convertendo para Excel, isso pode demorar, exportar em CSV é mais rápido')
                    data.to_excel(self._path, sheet_name='resultados', index=False, header=headers, engine='xlsxwriter')
            else:
                    self.progressbar_value.emit(70)
                    data.to_csv(self._path, index=False, header=headers, sep=';', encoding=self._default_encoding)
            return True
        except Exception as e:
            return f'Erro ao exportar log para Excel\n{e}'          
    
    
                