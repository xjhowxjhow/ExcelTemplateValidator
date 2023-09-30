from core import *
from models.AppConfig import AppConfig


class ExportDataFrame(QThread):
    finished = Signal()
    progressbar_text = Signal(str)
    progressbar_value = Signal(int)
    finished_success = Signal()
    finished_error = Signal(str)
    finished_none_log = Signal(str)

    def __init__(self, dataframe: pd.DataFrame, dict_erros: dict, path: str, option_export: str, parent=None,validation_template=None):
        super().__init__(parent)
        self._dataframe = dataframe
        self._dict_erros = dict_erros
        self._path = path
        self._option_export = option_export
        self._app_config = AppConfig()
        self._validador_template = validation_template


    def run(self):
        if self._option_export == 'VALIDOS':
            export = self._export_validos_to_xlsx()
            if export:
                self.finished_success.emit()
            else:
                self.finished_error.emit(export)
        elif self._option_export == 'ERROS':
            export = self._export_erros_to_excel_json()
            if export is True:
                self.finished_success.emit()
            elif export == 'EmpyError':
                self.finished_none_log.emit('Nenhum log encontrado para exportar')
            else:
                self.finished_error.emit(export)
        self.finished.emit()

    def _export_validos_to_xlsx(self):
        #Pega as headers/ordem  pelo nome das colunas do template do qtableview : retorna uma lista com nome das colunas na posicao atual
        indexers :list = self._validador_template._Get_HeadersLogicalIndexers()

        #reorda o dataframe de acordo com a ordem das colunas do template
        self._dataframe = self._dataframe[indexers]
        
        try:
            data = self._dataframe.copy()
            headers = data.columns.tolist()

            if self._dict_erros['erros']:
                lines_erros_ignore = [erros['row'] for erros in self._dict_erros['erros']]

                data = data.drop(lines_erros_ignore)
                data = data.astype(str)


                print('DATAFRAME EXPORT')

                format_cfg = self._app_config.get_default_export_format()

                print(F'FORMATO EXPORT {format_cfg}')

                if format_cfg == 'xlsx':
                    print('convertendo para excel')
                    convert = data.to_excel(self._path, index=False, header=headers)
                else:
                    print('convertendo para csv')
                    convert = data.to_csv(self._path, index=False, header=headers, sep=';', encoding='latin-1')
                print('CONVERTIDO?')
                if convert:
                    return False
                else:
                    return True
            return True
        except Exception as e:
            return f'Erro ao exportar log para excel\n{e}'

    def _export_erros_to_excel_json(self):
        if self._dict_erros is None:
            return 'EmpyError'
        try:
            if self._dict_erros['erros']:
                if self._path:
                    wb = xl.Workbook()
                    ws = wb.active

                    # CABEÇALHO
                    ws['A1'] = 'LINHA'
                    ws['B1'] = 'COLUNA'
                    ws['C1'] = 'CAMPO'
                    ws['D1'] = 'ERRO'

                    # DADOS
                    row = 2

                    for erro in self._dict_erros['erros']:
                        ws.cell(row=row, column=1).value = erro['row'] + 1
                        ws.cell(row=row, column=2).value = erro['col'] + 1
                        ws.cell(row=row, column=3).value = erro['field_name']
                        ws.cell(row=row, column=4).value = erro['error']
                        row += 1
                        self.progressbar_value.emit( (row / len(self._dict_erros['erros'])) * 100)
                        # texto de progresso
                        self.progressbar_text.emit(
                            f"Exportando Linhas com Erros: {row} de {len(self._dict_erros['erros'])}")
                        


                    wb.save(self._path)
                    return True
            else:
                return 'EmpyError'
        except Exception as e:
            return f'Erro ao exportar log para excel\n{e}'
