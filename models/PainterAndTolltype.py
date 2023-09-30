from core import *
from models.AppConfig import AppConfig


class WorkerSignals(QObject):
    finished = Signal()
    finished_erros = Signal(int)
    progressbar_value = Signal(int)
    progressbar_text = Signal(str)
    change_color = Signal(list)
    set_tooltip = Signal(list)
    change_color_unique = Signal(list)
    set_tooltip_unique = Signal(list)



class WorkerPainterThread(QRunnable):
    

    def __init__(self, dict_erros, qt_headers, qt_rows, parent=None):
        super().__init__(parent)

        self.dict_erros = dict_erros
        self.app_config = AppConfig()
        self.qt_headers = qt_headers
        self.qt_rows = qt_rows
        self.signals = WorkerSignals()
        self.setAutoDelete(True)
        

    def run(self):

        BATCH_TOOLTIPE = []
        BATCH_COLOR = []
        BATCH_SIZE = 100

        dict_erros = self.dict_erros
        data = dict_erros['erros']
        qt_headers = self.qt_headers
        qt_rows = self.qt_rows

        SETTINGS_R = self.app_config.get_export_excel_pinter_row_limit()
        SETTINGS_C = self.app_config.get_export_excel_pinter_collum_limit()

        if qt_rows > SETTINGS_R and qt_headers > SETTINGS_C:

            for error_item in data:
                row = error_item['row']
                col = error_item['col']

                tooltipe_model = f"""<span><b>Erros Encontrados:</b></span>
                                    <br>
                                    Erros: <b>{error_item['error']}</b>
                                 """
                BATCH_TOOLTIPE.append([row, col, tooltipe_model])
                BATCH_COLOR.append([row, col, QColor(156, 66, 66, 200)])

                if len(BATCH_TOOLTIPE) >= BATCH_SIZE:
                    self.signals.set_tooltip.emit(BATCH_TOOLTIPE)
                    self.signals.change_color.emit(BATCH_COLOR)
                    BATCH_TOOLTIPE = []
                    BATCH_COLOR = []

            if BATCH_TOOLTIPE:  
                self.signals.set_tooltip.emit(BATCH_TOOLTIPE)
                self.signals.change_color.emit(BATCH_COLOR)
        else:

            row_erro = list(dict.fromkeys([item['row'] for item in data]))
            row_and_col_erro = list(dict.fromkeys(
                [(item['row'], item['col']) for item in data]))



            QLIST_TOOLTIP = []
            QLIST_COLOR = []

            for row in range(qt_rows):
                if row in row_erro:
                    for col in range(qt_headers):
                        tooltipe_model_line = f"""<span><b>Erros Encontrados:</b></span>
                                                <br>
                                                Este Valor é valido, Mas esta linha contem erros:
                                                <br>
                                                Colunas: <b>{
                                                    [item['field_name'] for item in data if item['row'] == row]
                                                } </b>
                                                """
                        QLIST_TOOLTIP.append([row, col, tooltipe_model_line])
                        QLIST_COLOR.append([row, col, QColor(210, 175, 175)])

                else:
                    for col in range(qt_headers):
                        tooltipe_model_line_Success = f"""<span><b>Sucesso:</b></span>
                                                        <br>
                                                        Este Valor é valido, e esta linha não contem erros!
                                                        <br>
                                            """
                        QLIST_TOOLTIP.append([row, col, tooltipe_model_line_Success])
                        QLIST_COLOR.append([row, col, QColor(66, 156, 66, 200)])

                for col in range(qt_headers):
                    if (row, col) in row_and_col_erro:
                        tooltipe_model = f"""<span><b>Erros Encontrados:</b></span>
                                                <br>
                                                Erros: <b>{
                                                    [item['error'] for item in data if item['row'] == row and item['col'] == col]
                                                } </b>
                                                """

                        QLIST_TOOLTIP.append([row, col, tooltipe_model])
                        QLIST_COLOR.append([row, col, QColor(156, 66, 66, 200)])


                self.signals.progressbar_value.emit(int((row/qt_rows)*100))
                self.signals.progressbar_text.emit(f"Identificando Linhas com Erros: {row} de {qt_rows}")
                
            
            #Signal Update
            self.signals.progressbar_value.emit(0)
            for index, item in enumerate(QLIST_TOOLTIP):
                self.signals.set_tooltip_unique.emit(QLIST_TOOLTIP[index])
                self.signals.change_color_unique.emit(QLIST_COLOR[index])
                self.signals.progressbar_value.emit(int((index/len(QLIST_TOOLTIP))*100))
                self.signals.progressbar_text.emit(f"Aplicando Estilo: {index} de {len(QLIST_TOOLTIP)}")
                    


        #delay prevent crash
        self.signals.finished_erros.emit(len(data))
        sleep(0.1)
        self.signals.finished.emit()
