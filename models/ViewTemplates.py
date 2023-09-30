from core import *
from models.Database import Database
from models.MessageDialogBox import MessageDialogBox

class QspinBoxLength(QSpinBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setRange(0, 9999)
        self.setSingleStep(1)
        self.setFrame(False)
        self.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.setSpecialValueText("")


class ComboBoxTypesData(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.addItems(["VARCHAR", "INTEGER", "DATE", "DATETIME", "NUMBER", "BOOLEAN",
                      "TELEFONE", "CPF", "CNPJ", "CEP", "EMAIL", "SITE", "LISTA", "LISTA MULTIPLA"])
        self.setFrame(False)
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)
        self.lineEdit().setAlignment(Qt.AlignCenter)


class CheckBoxRequired(QCheckBox):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setCheckState(Qt.Unchecked)
        self.setTristate(False)

class EditSaveButton(QPushButton):
    EditCliked = Signal()
    SaveCliked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Editar")
        self.setFixedSize(100, 30)
        self.setCheckable(True)
        self.setChecked(False)
        self.setFlat(True)
        self.setIcon(QIcon(":/newicons/newicons/edit.png"))
        self.clicked.connect(self._ChangeText)
    def _ChangeText(self):
        if self.isChecked():
            self.setIcon(QIcon(":/newicons/newicons/save.png"))
            self.setText("Salvar")
            self.SaveCliked.emit()

        else:
            self.setIcon(QIcon(":/newicons/newicons/edit.png"))
            self.setText("Editar")
            self.EditCliked.emit()


class SetViewTemplate(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.temaplate_name = None


        self.setRowCount(0)
        self.setColumnCount(9)
        self.setHorizontalHeaderLabels(
            ["Ordem","Nome", "Tipo", "Tamaho", "Obrigatório", "OnlylistValues", "List(Separate with ;)", "UniqueValue", "Ações"])

        # min width columns
        self.setColumnWidth(0, 50)
        self.setColumnWidth(1, 250)
        self.setColumnWidth(2, 250)
        self.setColumnWidth(3, 250)
        self.setColumnWidth(4, 250)
        self.setColumnWidth(5, 250)
        self.setColumnWidth(6, 250)
        self.setColumnWidth(7, 50)
        self.setColumnWidth(8, 50)

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
        self.horizontalHeader().setStretchLastSection(False)
        self.verticalHeader().setVisible(True)
        self.verticalHeader().setCascadingSectionResizes(False)
        self.verticalHeader().setHighlightSections(True)
        self.verticalHeader().setProperty("showSortIndicator", False)
        self.verticalHeader().setStretchLastSection(False)

        # DISABLE EDIT
        # self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setFocusPolicy(Qt.NoFocus)

        
        


    def _Set_Data_Table(self, data_table,template_name:str):
        
        if data_table != None:
            self.temaplate_name = template_name
            self.setRowCount(0)
            for row in data_table:
                rowPosition = self.rowCount()
                EditButton = EditSaveButton()
                EditButton.EditCliked.connect(lambda:self._EditRow('Edit'))
                EditButton.SaveCliked.connect(lambda:self._EditRow('Save'))

                self.insertRow(rowPosition)
                self.setItem(rowPosition, 0, QTableWidgetItem(str(row[0])))
                self.setItem(rowPosition, 1, QTableWidgetItem(row[1]))
                self.setItem(rowPosition, 2, QTableWidgetItem(row[2]))
                self.setItem(rowPosition, 3, QTableWidgetItem(str(row[3])))
                self.setItem(rowPosition, 4, QTableWidgetItem(row[4]))
                self.setItem(rowPosition, 5, QTableWidgetItem(row[5]))
                self.setItem(rowPosition, 6, QTableWidgetItem(row[6]))
                self.setItem(rowPosition, 7, QTableWidgetItem(row[7]))
                self.setCellWidget(rowPosition, 8, EditButton)



                # bloqueia edicao
                self.item(rowPosition, 0).setFlags(
                    Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.item(rowPosition, 1).setFlags(
                    Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.item(rowPosition, 2).setFlags(
                    Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.item(rowPosition, 3).setFlags(
                    Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.item(rowPosition, 4).setFlags(
                    Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.item(rowPosition, 5).setFlags(
                    Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.item(rowPosition, 7).setFlags(
                    Qt.ItemIsSelectable | Qt.ItemIsEnabled)

            self.resizeColumnsToContents()
            self.resizeRowsToContents()
            return True

        else:
            return False
        
    
    def _LockUnlockRows(self,action:str,row:int):
                    
        self.item(row, 0).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled if action == 'Edit' else Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable)
        self.item(row, 1).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled if action == 'Edit' else Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable)
        self.item(row, 2).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled if action == 'Edit' else Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable)
        self.item(row, 3).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled if action == 'Edit' else Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable)
        self.item(row, 4).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled if action == 'Edit' else Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable)
        self.item(row, 5).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled if action == 'Edit' else Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable)
        self.item(row, 6).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled if action == 'Edit' else Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable)
        self.item(row, 7).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled if action == 'Edit' else Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable)


    def _EditRow(self,action:str):

        row:int = self.currentRow()
        self._LockUnlockRows(action,row)

        if action =='Edit':
            NewValuesUp:list = [ self.item(row,coll).text() for coll in range(8)]
            print(self.temaplate_name)
            print(NewValuesUp)
            self._UpdateTableRow(NewValuesUp)

            

    def _UpdateTableRow(self,data):
        db = Database()
        fields= ['campo_ordem','campo_nome', 'campo_tipo', 'campo_tamanho', 'campo_obrigatorio','onlylistValue','ListValue','unique_coll']
        try:
            for index ,item in enumerate(data):
                print(f"""CAMPO ORDEM: {fields[index]} VALOR: {item}""")
                sequence = db.cursor.execute(f"""SELECT seq_id FROM templates WHERE campo_nome = '{data[1]}' AND template_nome = '{self.temaplate_name}'""").fetchone()[0]

                db.cursor.execute(f"""UPDATE templates SET {fields[index]} = '{item}' WHERE seq_id = {sequence}""")
                db.conn.commit()

            MessageDialogBox(title='Atualizado com Sucesso',message='Atualizado com Sucesso')._ShowMessage()
        except Exception as e:
            MessageDialogBox(title='Erro ao Realizar Atualizar',message=e)._ShowCritical()
            db.conn.rollback()
        db.conn.close()

        