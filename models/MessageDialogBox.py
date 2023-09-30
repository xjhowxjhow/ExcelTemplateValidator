from core import *


class MessageDialogBox(QMessageBox):
    def __init__(self, title: str, message: str):
        super().__init__()
        self.title = title
        self.message = message

    def _ShowMessage(self):
        self.setWindowTitle(self.title)
        self.setText(self.message)
        self.setStandardButtons(QMessageBox.Ok)
        self.setIcon(QMessageBox.Information)
        self.exec_()

    def _ShowWarning(self):
        self.setWindowTitle(self.title)
        self.setText(self.message)
        self.setStandardButtons(QMessageBox.Ok)
        self.setIcon(QMessageBox.Warning)
        self.exec_()

    def _ShowCritical(self):
        self.setWindowTitle(self.title)
        self.setText(self.message)
        self.setStandardButtons(QMessageBox.Ok)
        self.setIcon(QMessageBox.Critical)
        self.exec_()

    def _ShowQuestion(self):
        self.setWindowTitle(self.title)
        self.setText(self.message)
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.setIcon(QMessageBox.Question)
        return self.exec_() == QMessageBox.Yes
