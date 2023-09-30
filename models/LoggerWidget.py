from models.MessageDialogBox import MessageDialogBox
from core import *


class LoggerWidget(QPlainTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        # ATRIBUTOS
        # ///////////////////////////////////////////////////////////////
        self._log = ''
        self._log_list = []
        self._log_list_size = 0
        self._current_json = {"erros": []}
        # CONFIGURAÇÕES DO WIDGET
        # ///////////////////////////////////////////////////////////////
        self.setReadOnly(True)
        self.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.setUndoRedoEnabled(False)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.setFrameStyle(QFrame.NoFrame)
        self.setFrameShadow(QFrame.Plain)
        self.setLineWidth(0)
        self.setMidLineWidth(0)
        self.setTabChangesFocus(True)
        self.setAcceptDrops(False)

    def Cabeçalho(self):
        string_v = f"""
        =================================================
         LOG DE ERROS {datetime.now()}
        =================================================
        """
        return string_v

    def add_log(self, log):
        self._current_json = log
        self._log += self.Cabeçalho()

        log = json.dumps(log, indent=4, ensure_ascii=False)

        self._log += log

        # self._log_list.append(log) Caso queira salvar em uma lista
        # self._log_list_size += 1

        self.setPlainText(self._log)
        self.moveCursor(QTextCursor.End)
        self.ensureCursorVisible()

    def append_log_per_thread(self, log:list):


        id_thread = log[0]
        if log[1] == {}: return None

        logger = json.dumps(log[1] ,indent=4, ensure_ascii=False)

        self._log += f'\n\
        =================================================\n\
        LOG DE ERROS {datetime.now()} - THREAD ID {id_thread}\n\
        =================================================\n\
        {logger}'

        #append self.current_json
        for i in log[1]['erros']:
            self._current_json['erros'].append(i)


        self.setPlainText(self._log)
        self.moveCursor(QTextCursor.End)
        self.ensureCursorVisible()


    def add_log_system(self, log):
        head = f""" SYSTEM LOG {datetime.now()} : """
        self._log += head + log + '\n'
        self.setPlainText(self._log)
        self.moveCursor(QTextCursor.End)
        self.ensureCursorVisible()

    def clear_log(self):
        self._log = ''
        self._log_list = []
        self._log_list_size = 0
        self._current_json = {"erros": []}
        self.setPlainText(self._log)
        self.moveCursor(QTextCursor.End)
        self.ensureCursorVisible()

    def get_log_list(self):
        return self._log_list

    def get_log_list_size(self):
        return self._log_list_size

