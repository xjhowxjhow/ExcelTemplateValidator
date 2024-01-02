from core import *
from models.Database import Database



class Signals(QObject):
    progressbar_value = Signal(int)
    progressbar_text = Signal(str)
    error = Signal(str)
    finished = Signal()
    start_painter_rows = Signal()
    set_logger = Signal(dict)


class WorkerValidadorDuplicadas(QRunnable):
    def __init__(self, dataframe: pd.DataFrame, template_name ,parent=None):
        super().__init__(parent)
        self._dataframe = dataframe
        self._dict_erros_temp = {
            'erros': [],
            'qt_erros': 0
        }
        self.signals = Signals()
        self.dba = Database()
        self.template_name = template_name
        self.setAutoDelete(True)

    def ResetErros(self):
        self._dict_erros_temp = {
            'erros': [],
            'qt_erros': 0
        }


    def run(self):
        self.ResetErros()
        self.signals.progressbar_text.emit(f"Verificando Duplicatas...")
        uniques_fields = [item[0]for item in self.dba.get_all_fields_uniques(self.template_name)]
        if uniques_fields != []:
            try:
                
                self._VerificaDuplicatas(self._dataframe, uniques_fields)
                self.signals.set_logger.emit(['Thread Duplicatas',self._dict_erros_temp])

            except Exception as e:
                print(e)
                self.signals.start_painter_rows.emit()
        
            
        self.signals.start_painter_rows.emit()


    def _VerificaDuplicatas(self,dataframe: pd.DataFrame, uniques_fields):
        
        unique_values_mapping = {field_name: {} for field_name in uniques_fields}
        try:
            self.signals.progressbar_text.emit(f"Verificando Duplicatas...")
            for row, row_data in dataframe.iterrows():
                progress_percentage = int((row / len(dataframe)) * 100)
                self.signals.progressbar_value.emit(progress_percentage)
                for field_name in uniques_fields:
                    col = dataframe.columns.get_loc(field_name)
                    valor = row_data[col] if not pd.isnull(row_data[col]) else ""
                    
                    if valor in unique_values_mapping[field_name] and unique_values_mapping[field_name][valor] != row:
                        existing_row = unique_values_mapping[field_name][valor]
                        error_msg = f"Valor Duplicado, esta coluna é Única e esse valor já existe na linha {existing_row + 1}"
                        self._AppendErros(row, col, field_name, error_msg)
                        # sun_erros()
                    unique_values_mapping[field_name][valor] = row
        except Exception as e:
            return False
        
    def _AppendErros(self, row, col, field_name, error):
        self._dict_erros_temp["erros"].append({"row": row, "col": col, "field_name": field_name, "error": error})