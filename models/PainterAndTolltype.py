from core import *
from models.AppConfig import AppConfig


class WorkerSignals(QObject):
    finished = Signal()
    finished_erros = Signal(int)
    progressbar_value = Signal(int)
    progressbar_text = Signal(str)
    change_color = Signal(list)
    set_tooltip = Signal(list)




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

        SETTINGS_R = self.app_config.get_export_excel_pinter_row_limit()    #NAO USADO MAIS
        SETTINGS_C = self.app_config.get_export_excel_pinter_collum_limit() #NAO USADO MAIS


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



        #delay prevent crash
        self.signals.finished_erros.emit(len(data))
        sleep(0.1)
        self.signals.finished.emit()
