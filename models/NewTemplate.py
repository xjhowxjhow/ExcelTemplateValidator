from core import *
from models.MessageDialogBox import MessageDialogBox


class QspinBoxLength(QSpinBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setRange(0, 9999)
        self.setSingleStep(1)
        self.setFrame(False)
        self.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.setSpecialValueText("")
        # default value
        self.setValue(250)


class ComboBoxTypesData(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.addItems(["VARCHAR", "INTEGER", "DATE", "DATETIME", "NUMBER", "BOOLEAN",
                      "TELEFONE - N implementado", "CPF - N implementado", "CNPJ - N implementado", "CEP - N implementado", "EMAIL - N implementado", "SITE - N implementado", "LISTA - N implementado", "LISTA MULTIPLA - N implementado"])
        self.setFrame(False)
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)
        self.lineEdit().setAlignment(Qt.AlignCenter)
        self.setStyleSheet(
            """
            QComboBox {
                background-color: #F0F0F0; /* Fundo branco meio cinza */
                color: #333; /* Texto mais escuro */
                padding: 5px;
                border-radius: 0px;
            }

            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;

                border-left: 1px solid #CCC; /* Borda cinza mais claro */
            }

            QComboBox::down-arrow {
                image: url(:/newicons/newicons/cil-arrow-bottom.png);
            }

            QComboBox::down-arrow:on {
                /* Topo do botão pressionado */
                top: 1px;
                left: 1px;
            }

            

            QComboBox QAbstractItemView {
                background-color: #F0F0F0; /* Fundo branco meio cinza */
                border: 1px solid #CCC; /* Borda cinza mais claro */
                color: #333; /* Texto mais escuro */
                selection-background-color: #CCC; /* Fundo do item selecionado cinza mais claro */
                selection-color: #333; /* Texto do item selecionado mais escuro */
            }
            """
        )


class CheckBoxRequired(QCheckBox):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setCheckState(Qt.Unchecked)
        self.setTristate(False)


class NewTemplate(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setRowCount(0)

        # HEADERS
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        self.setColumnCount(8)
        self.setHorizontalHeaderLabels(
            ["Ordem","Nome", "Tipo", "Tamaho", "Obrigatório", "OnlylistValues", "List(Separate with ;)", "UniqueValue"])

        # min width columns
        self.setColumnWidth(0, 50)
        self.setColumnWidth(1, 250)
        self.setColumnWidth(2, 250)
        self.setColumnWidth(3, 100)
        self.setColumnWidth(4, 100)
        self.setColumnWidth(5, 100)
        self.setColumnWidth(6, 250)
        self.setColumnWidth(7, 50)

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
        self.setSortingEnabled(False)
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

        # Events
        self.cellChanged.connect(self._Cell_Changed)
        self.cellClicked.connect(self._Cell_Clicked)
    def _Max_ordem(self):
        max_ordem = 0
        if self.rowCount() == 0:
            return max_ordem
        
        for row in range(self.rowCount()):
            if int(self.item(row, 0).text()) > max_ordem:
                max_ordem = int(self.item(row, 0).text())
        return max_ordem

    def _Add_Row(self):

        itemorder = QTableWidgetItem(str(self._Max_ordem()+1))

        self.insertRow(self.rowCount())
        self.setItem(self.rowCount()-1, 0, itemorder)
        self.setItem(self.rowCount()-1, 1, QTableWidgetItem(""))
        self.setCellWidget(self.rowCount()-1, 2, ComboBoxTypesData())
        self.setCellWidget(self.rowCount()-1, 3, QspinBoxLength())
        self.setCellWidget(self.rowCount()-1, 4, CheckBoxRequired())
        self.setCellWidget(self.rowCount()-1, 5, CheckBoxRequired())
        # adicionar txt vazio na ultima coluna list7
        self.setItem(self.rowCount()-1, 6, QTableWidgetItem(""))
        self.setCellWidget(self.rowCount()-1, 7, CheckBoxRequired())

        # ALINHAMENTO CENTRAL
        self.cellWidget(self.rowCount()-1,
                        2).lineEdit().setAlignment(Qt.AlignCenter)
        self.cellWidget(self.rowCount()-1,
                        3).lineEdit().setAlignment(Qt.AlignCenter)
        #DESACTIVE EDITABLE 0
        self.item(self.rowCount()-1, 0).setFlags(
            Qt.ItemIsSelectable | Qt.ItemIsEnabled)

    def _Delete_Row(self):
        current_row = self.currentRow()
        self.removeRow(current_row)
        self._ReorderOrdem()


    def _ReorderOrdem(self):
        for row in range(self.rowCount()):
            self.item(row, 0).setText(str(row+1))



    def _Cell_Changed(self, row, column):
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        # Set UPPERCASE
        if column == 1:
            self.item(row, column).setText(
                self.item(row, column).text().strip())

        if column == 6:
            # Valida lista separada por ;
            list_item = self.item(row, column).text().split(";")  # Separa por ;
            # REMOVE Quebra de linha
            # Remove espaços em branco
            list_item = list(map(lambda s: s.strip(), list_item))
            list_item = list(filter(None, list_item))  # Remove itens vazios
            # Remove itens duplicados
            list_item = list(dict.fromkeys(list_item))
            list_item = ";".join(list_item)  # Junta novamente com ;

            self.item(row, column).setText(list_item.strip())

    def _Cell_Clicked(self, row, column):
        # Set UPPERCASE
        if column == 4:  # checkbox
            if self.cellWidget(row, column).checkState() == Qt.Checked:
                self.cellWidget(row, column).setCheckState(Qt.Unchecked)
            else:
                self.cellWidget(row, column).setCheckState(Qt.Checked)

        if column == 5:  # checkbox
            if self.cellWidget(row, column).checkState() == Qt.Checked:
                self.cellWidget(row, column).setCheckState(Qt.Unchecked)
            else:
                self.cellWidget(row, column).setCheckState(Qt.Checked)

        if column == 7:  # checkbox
            if self.cellWidget(row, column).checkState() == Qt.Checked:
                self.cellWidget(row, column).setCheckState(Qt.Unchecked)
            else:
                self.cellWidget(row, column).setCheckState(Qt.Checked)

    def _Get_Data(self):

        data = []

        row_status, row_index = self._RowNameIsnull()
        if row_status:
            return False

        row_lsitstatus, row_listindex = self._ValidadeListIsValid()
        if row_lsitstatus == False:
            return False

        for row in range(self.rowCount()):
            data.append([])
            for column in range(self.columnCount()):
                if column == 0:
                    data[row].append(self.item(row, column).text())
                if column == 1:
                    data[row].append(self.item(row, column).text())
                elif column == 2:
                    data[row].append(self.cellWidget(
                        row, column).currentText())
                elif column == 3:
                    data[row].append(str(self.cellWidget(row, column).value()))
                elif column == 4:

                    if self.cellWidget(row, column).checkState() == Qt.Checked:
                        data[row].append("1")
                    else:
                        data[row].append("0")
                elif column == 5:

                    if self.cellWidget(row, column).checkState() == Qt.Checked:
                        data[row].append("1")
                    else:
                        data[row].append("0")
                elif column == 6:
                    data[row].append(self.item(row, column).text())

                elif column == 7:
                    if self.cellWidget(row, column).checkState() == Qt.Checked:
                        data[row].append("1")
                    else:
                        data[row].append("0")

        return data

    def _RowNameIsnull(self):
        row_index = None
        for row in range(self.rowCount()):
            if self.item(row, 1).text() == "":
                row_index = row

                MessageDialogBox("Atenção", "O campo nome da linha {} está vazio".format(
                    row_index+1))._ShowCritical()
                return True, row_index

        return False, row_index

    def _ValidadeListIsValid(self):
        for row in range(self.rowCount()):
            if self.cellWidget(row, 5).checkState() == Qt.Checked:
                if self.item(row, 6).text() == "":
                    MessageDialogBox("Atenção", "O campo List(Separate with ;) da linha {} está vazio".format(
                        row+1))._ShowCritical()
                    return False, row
                if self.item(row, 6).text().endswith(";"):
                    MessageDialogBox("Atenção", "O campo List(Separate with ;) da linha {} não pode terminar com ;".format(
                        row+1))._ShowCritical()
                    return False, row

        return True, row
