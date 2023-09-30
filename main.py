#################################################################################
# Created by:   Jhonatan Deni | Qt Designer version: 5.15.2                     #
# GITHUB:       https://github.com/xjhowxjhow/TemplateValidator                 #
# Linkedin:     https://www.linkedin.com/in/jhonatan-deni-a23077192/            #
# Site:         https://jhonatandeni.netlify.app/                               #
# V1.9.1                                                                        #
# WARNING! All changes made in this file will be lost when recompiling UI file! #
#################################################################################

# CORE
from core import *
# POOL THREADS
from models.ControlThread import ControlThread
# CLASSMODELS
from models.NewTemplate import NewTemplate
from models.ViewTemplates import SetViewTemplate
from models.Database import Database
from models.GeraTemplatexls import GeraTemplatexls
from models.InputTemplateTable import TemplateInput, WorkerThread
from models.ValidadorTemplate import ValidadorTemplate, WorkerThreadValidacao
from models.PainterAndTolltype import WorkerPainterThread
from models.ExportDataFrame import ExportDataFrame
from models.ValidadorDuplicatas import WorkerValidadorDuplicadas
# ALERTS
from models.MessageDialogBox import MessageDialogBox
from models.LoggerWidget import LoggerWidget
# APPCONFIG
from models.AppConfig import AppConfig



class MainWindow (Ui_mainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        self.show()
        self.app = QCoreApplication.instance()
        self.progressBar.hide()
    
        # CONFIGS
        # ///////////////////////////////////////////////////////////////
        self.app_config = AppConfig()
        self.app_config.load_config()

        # THREADS
        # ///////////////////////////////////////////////////////////////
        self.ControlThread = ControlThread()

        # DB CONNECTION
        # ///////////////////////////////////////////////////////////////
        self.db = Database()

        # CUSTOM WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.TemplateWidget = NewTemplate()
        self.verticalLayout_22.addWidget(self.TemplateWidget)

        self.ViewTemplate = SetViewTemplate(None)
        self.set_view_template_layout.addWidget(self.ViewTemplate)

        self.TemplateInputWidget = TemplateInput()
        self.set_view_template.addWidget(self.TemplateInputWidget)

        self.ValidadorTemplate = ValidadorTemplate()
        self.set_validador_template_.addWidget(self.ValidadorTemplate)

        self.loggerViewWidget = LoggerWidget()
        self.loger_layout_customwid.addWidget(self.loggerViewWidget)

        # SIGNALS CUSTOM WIDGETS PROGRESSBAR VALUE
        # ///////////////////////////////////////////////////////////////
        self.TemplateInputWidget.progressbar_value.connect(lambda x: self.ProgressBarValue(x))
        self.ValidadorTemplate.progressbar_value.connect(lambda x: self.ProgressBarValue(x))
        self.ValidadorTemplate.progressbar_export_value.connect(lambda x: self.ExportToXlsProgressValue(x))

        # SIGNALS CUSTOM WIDGETS PROGRESSBAR TEXT
        # ///////////////////////////////////////////////////////////////
        self.TemplateInputWidget.progressbar_text.connect(lambda x: self.ProgressBarText(x))
        self.ValidadorTemplate.progressbar_text.connect(lambda x: self.ProgressBarText(x))

        # EVENT FILTERS
        # ///////////////////////////////////////////////////////////////
        self.btn_page_home.installEventFilter(self)
        self.btn_page_config.installEventFilter(self)
        self.btn_page_clients.installEventFilter(self)

        # TABELA ADICIONAR TEMPLATE
        # ///////////////////////////////////////////////////////////////
        self.btn_gerar_template.installEventFilter(self)
        self.new_fild_template.installEventFilter(self)
        self.delete_fild_template.installEventFilter(self)

        # SIGNALS CHANGED WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.listWidget.itemClicked.connect(self.ListViewTemplateClicked)
        self.btn_pg_add_new_template.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_new_template))
        self.btn_deleta_template.clicked.connect(self.DeleteTemplate)
        self.searchtemplates.textChanged.connect(self.SearchListTemplate)
        self.ControlThread.finished_all_thread.connect(lambda:  self.StartValidationDuplites())

        # BTNS SIGNALS FUNCTIONS
        # ///////////////////////////////////////////////////////////////
        self.btn_cria_xls_template.clicked.connect(self.GeraTemplate)
        self.start.clicked.connect(self.InputTemplate)
        self.start_validation.clicked.connect(self.StartValidationTemplate)
        self.export_xlsx.clicked.connect(lambda: self.ExportToXls('VALIDOS'))
        self.jsontoxls.clicked.connect(lambda: self.ExportToXls('ERROS'))
        self.btn_exit_program.clicked.connect(self.app.quit)
        self.save_config.clicked.connect(self.SaveConfig)
        self.reset_config.clicked.connect(self.LoadConfig)

        # STARTER FUNCTIONS
        # ///////////////////////////////////////////////////////////////
        self.LoadConfig()
        self.SetTemplatesList()
        self.SetViewTemplate(None, None)


    def LoadConfig(self):
        self.config_export_row_limit.setValue(
            self.app_config.get_export_excel_pinter_row_limit())
        self.config_export_coll_limit.setValue(
            self.app_config.get_export_excel_pinter_collum_limit())
        NumberType = self.app_config.get_number_type()
        if NumberType == 'v':
            self.config_datatype_number_allowerd_v.setChecked(True)
            self.config_datatype_number_allowerd_p.setChecked(False)
        elif NumberType == 'p':
            self.config_datatype_number_allowerd_p.setChecked(True)
            self.config_datatype_number_allowerd_v.setChecked(False)
        elif NumberType == 'a':
            self.config_datatype_number_allowerd_p.setChecked(True)
            self.config_datatype_number_allowerd_v.setChecked(True)
        else:
            self.config_datatype_number_allowerd_p.setChecked(False)
            self.config_datatype_number_allowerd_v.setChecked(False)

    def SaveConfig(self):
        if self.config_datatype_number_allowerd_v.isChecked() and self.config_datatype_number_allowerd_p.isChecked():
            self.app_config.set_number_type('a')
        elif self.config_datatype_number_allowerd_v.isChecked():
            self.app_config.set_number_type('v')
        elif self.config_datatype_number_allowerd_p.isChecked():
            self.app_config.set_number_type('p')
        else:
            self.app_config.set_number_type('p')

        self.app_config.set_export_excel_pinter_row_limit(
            self.config_export_row_limit.value())
        self.app_config.set_export_excel_pinter_collum_limit(
            self.config_export_coll_limit.value())
        self.app_config.set_default_export_format(
            self.default_export.currentText())
        self.app_config.save_config()
        MessageDialogBox(
            "Sucess!", "Configurações Salvas com Sucesso")._ShowMessage()
        self.LoadConfig()

    def ResetConfig(self):
        return self.app_config.default_config()

    def SetButtonsState(self, state):
        self.btn_cria_xls_template.setEnabled(state)
        self.start.setEnabled(state)
        self.start_validation.setEnabled(state)
        self.export_xlsx.setEnabled(state)
        self.jsontoxls.setEnabled(state)

        if state == True:
            self.progressBar.hide()
            self.progressBar_2.hide()
        else:
            self.progressBar.show()
            self.progressBar_2.show()

    def ProgressBarValue(self, value):
        self.progressBar.setValue(value)

    def ProgressBarText(self, text):
        self.progressBar.setFormat(text)

    def ExportToXlsProgressValue(self, value):
        self.progressBar_2.setValue(value)

    def ExportToXlsProgressText(self, text):
        self.progressBar_2.setFormat(text)

    def ExportToXls(self, option):
        def NenhunLogEncontrado():
            self.SetButtonsState(True)
            self.ShowWarningMessage(
                "Atenção", "Nenhum log encontrado para exportar")

        def FinishExport():
            self.SetButtonsState(True)
            question = self.ShowQuestionMessage(
                "Sucesso!", "Deseja abrir o arquivo?")
            if not question:
                return False
            os.startfile(save_file[0])

        def ExportErro(error):
            self.SetButtonsState(True)
            self.ShowCriticalMessage(
                "Atenção", f"Erro ao salvar o arquivo: {error}")
        type_format= self.app_config.get_default_export_format() #xlsx ou csv


        save_file_filter = "Excel (*.csv)" if type_format == 'csv' else "Excel (*.xlsx)" 

        save_file = QFileDialog.getSaveFileName(
            self, "Salvar Arquivo", "", save_file_filter)

        if not save_file[0]:
            self.ShowWarningMessage(
                "Atenção", "Selecione um local para salvar o arquivo")
            self.SetButtonsState(True)
            return False

        self.SetButtonsState(False)

        option_export = option
        data = self.ValidadorTemplate.data
        dict_erros = self.loggerViewWidget._current_json
        self.threadExport = ExportDataFrame(
            dataframe=data, dict_erros=dict_erros, path=save_file[0], option_export=option_export,validation_template=self.ValidadorTemplate)
        self.threadExport.progressbar_value.connect(
            self.ExportToXlsProgressValue)
        self.threadExport.progressbar_text.connect(
            self.ExportToXlsProgressText)
        self.threadExport.finished_success.connect(FinishExport)
        self.threadExport.finished_error.connect(lambda x: ExportErro(x))
        self.threadExport.finished_none_log.connect(NenhunLogEncontrado)
        self.threadExport.start()
        self.threadExport.finished.connect(self.threadExport.quit)
        self.threadExport.finished.connect(self.threadExport.deleteLater)

    def ShowWarningMessage(self, title, message):
        self.SetButtonsState(True)
        MessageDialogBox(title, message)._ShowWarning()

    def ShowQuestionMessage(self, title, message):
        self.SetButtonsState(True)
        return MessageDialogBox(title, message)._ShowQuestion()

    def ShowCriticalMessage(self, title, message):
        self.SetButtonsState(True)
        MessageDialogBox(title, message)._ShowCritical()

    def StartValidationTemplate(self):
        QT_THREADS = self.ControlThread.MaxThreadCount()
        self.SetButtonsState(False)
        self.ClearLogger()
        self.ControlThread.RestartPool()
        self.ControlThread.counter_thread = 0


        template_name = self.TemplateInputWidget._GetTemplateName()
        data = self.TemplateInputWidget._Get_Data()

        if data.empty == True:
            MessageDialogBox("Atenção", "Selecione um arquivo")._ShowWarning()
            self.SetButtonsState(True)
            return False

        self.ValidadorTemplate._LoadTemplate(dataframe=data)

        qt_rows = len(data.index)

        if qt_rows < 500:  # Se for menor que 100 linhas, roda em uma thread
            QT_THREADS = 1

        rows_per_thread = qt_rows // QT_THREADS
        rest_rows = qt_rows % QT_THREADS
        list_exec = []

        
        print(f'QT THREADS COUNT: {self.ControlThread.counter_thread}')

        for i in range(QT_THREADS):
            print(f'EXEC THREAD: {i}')
            start = i * rows_per_thread
            end = (i + 1) * rows_per_thread
            if i == QT_THREADS - 1:
                end += rest_rows

            sliceframe = data.iloc[start:end]
            # SIGNALS
            RunableworkerValidador = WorkerThreadValidacao(
                dataframe=sliceframe, template_name=template_name, start=start, end=end, number_thread=i)
            RunableworkerValidador.signals.progressbar_value.connect(
                lambda x: self.ProgressBarValue(x))
            RunableworkerValidador.signals.progressbar_text.connect(
                lambda x: self.ProgressBarText(x))
            RunableworkerValidador.signals.set_logger.connect(
                lambda x: self.AppendLoggerThread(x))
            RunableworkerValidador.signals.finished.connect(
                lambda i=i: self.ControlThread.finish_job_thread(id_thread=list_exec[i]))
            list_exec.append(RunableworkerValidador)

            self.ControlThread.counter_thread += 1

        self.ControlThread.start_jobs_thread(QRunable=list_exec)
        
    def StartValidationDuplites(self): 
        
        RunableworkerValidadoDuplicadas = WorkerValidadorDuplicadas(
            dataframe=self.ValidadorTemplate.data, template_name=self.TemplateInputWidget.template_name)
        RunableworkerValidadoDuplicadas.signals.progressbar_value.connect(
            lambda x: self.ProgressBarValue(x))
        RunableworkerValidadoDuplicadas.signals.progressbar_text.connect(
            lambda x: self.ProgressBarText(x))
        RunableworkerValidadoDuplicadas.signals.set_logger.connect(
            lambda x: self.AppendLoggerThread(x))
        RunableworkerValidadoDuplicadas.signals.start_painter_rows.connect(
            lambda: self.PainterRows())
        self.ControlThread.start_single_thread(
            QRunable=RunableworkerValidadoDuplicadas)

    def PainterRows(self):
        # WORKER DATA
        # ///////////////////////////////////////////////////////////////
        dict_erros = self.loggerViewWidget._current_json  # pega o dict de erros do logger
        # qt colunas dataframe
        qt_headers = self.ValidadorTemplate.data.shape[1]
        qt_rows = self.ValidadorTemplate.data.shape[0]  # qt linhas dataframe
        # WORKER PAINTER
        # ///////////////////////////////////////////////////////////////
        Runableworkerpainter = WorkerPainterThread(
            dict_erros, qt_headers, qt_rows)
        # SIGNALS
        # ///////////////////////////////////////////////////////////////
        Runableworkerpainter.signals.progressbar_value.connect(
            lambda x: self.ProgressBarValue(x))
        Runableworkerpainter.signals.progressbar_text.connect(
            lambda x: self.ProgressBarText(x))
        Runableworkerpainter.signals.change_color.connect(
            lambda x: self.ValidadorTemplate._ChangeColor(x))
        Runableworkerpainter.signals.set_tooltip.connect(
            lambda x: self.ValidadorTemplate._SetTollTip(x))

        # TESTE UNIQUES
        Runableworkerpainter.signals.change_color_unique.connect(
            lambda x: self.ValidadorTemplate._ChangeColorUnique(x))
        Runableworkerpainter.signals.set_tooltip_unique.connect(
            lambda x: self.ValidadorTemplate._SetToollTipUnique(x))

        # SIGNALS START END FINISHED
        # ///////////////////////////////////////////////////////////////
        Runableworkerpainter.signals.finished.connect(
            lambda: self.FinishEnabelBtn())
        Runableworkerpainter.signals.finished_erros.connect(
            lambda x: self.FinishValidation(x))
        # START THREAD IN POOL
        # ///////////////////////////////////////////////////////////////
        self.ControlThread.start_single_thread(QRunable=Runableworkerpainter)

    def FinishEnabelBtn(self):

        self.SetButtonsState(True)

    def SetLogger(self, log):
        self.loggerViewWidget.add_log(log)

    def AppendLoggerThread(self, log: list):
        self.loggerViewWidget.append_log_per_thread(log)

    def ClearLogger(self):
        self.loggerViewWidget.clear_log()

    def InputTemplate(self):

        file_path = QFileDialog.getOpenFileName(
            self, "Abrir Arquivo", "", "Excel (*.csv *.xls *.xlsx)")
        template_name = self.combo_templates.currentText()
        self.SetButtonsState(False)

        if file_path[0] == "":
            MessageDialogBox("Atenção", "Selecione um arquivo")._ShowWarning()
            self.SetButtonsState(True)
            return False
        else:
            self.progressBar.show()

        def TemplateInvalid(text_error):
            
            MessageDialogBox(str(text_error[1]), str(text_error[2]))._ShowWarning()
            self.SetButtonsState(True)
            return False

        def TemplateCarregado():
            self.label_file_directory.setText(file_path[0])
            self.logvierw.setCurrentIndex(0)
            MessageDialogBox(
                "Atenção", "Arquivo Importado com Sucesso")._ShowMessage()
            self.SetButtonsState(True)
            return True

        self.thread = QThread()
        self.worker = WorkerThread(file_path[0], template_name)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.TemplateInputWidget.template_name = template_name
        self.worker.log_info.connect(
            lambda x: self.loggerViewWidget.add_log_system(x))
        self.worker.progressbar_value.connect(
            lambda x: self.ProgressBarValue(x))
        self.worker.progressbar_text.connect(lambda x: self.ProgressBarText(x))
        self.worker.valid_signal.connect(
            lambda x: TemplateInvalid(x) if x[0] == False else TemplateCarregado())
        self.worker.values_data.connect(
            lambda x: self.TemplateInputWidget._Set_Data(x))

        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()

    def FinishValidation(self, values):

        self.label_12.setText(f'Resultado: {values} Erros')
        MessageDialogBox(
            "Validação", f"Validação Concluida com {values} Erros")._ShowMessage()
        self.logvierw.setCurrentIndex(1)
        self.SetButtonsState(True)

    def PageTemplatesCurrentPage(self):
        page = self.stackedWidget.currentWidget()
        if page == self.page_new_template:
            return 'new'
        elif page == self.page_view_template:
            return 'view'
        else:
            return None

    def SetTemplatesList(self):

        self.listWidget.clear()
        self.combo_templates.clear()

        templates = self.db.select_all_templates_names()
        for template in templates:
            self.listWidget.addItem(template[0])
            self.combo_templates.addItem(template[0])

    def SearchListTemplate(self):
        filter_text = self.searchtemplates.text().lower()

        for index in range(self.listWidget.count()):
            item = self.listWidget.item(index)
            if filter_text in item.text().lower():
                item.setHidden(False)
            else:
                item.setHidden(True)

    def SetViewTemplate(self, data,template):
        self.ViewTemplate._Set_Data_Table(data_table=data,template_name=template)

    def ListViewTemplateClicked(self):
        template = self.listWidget.currentItem().text()
        data = self.db.select_config_template(template)
        self.SetViewTemplate(data=data, template=template)

        if self.PageTemplatesCurrentPage() == 'new':
            self.stackedWidget.setCurrentWidget(self.page_view_template)

        self.name_template_view.setText(template)

    def DeleteTemplate(self):
        quention = MessageDialogBox(
            "Atenção", "Deseja realmente deletar o template?")._ShowQuestion()
        if quention == False:
            return False

        template = self.listWidget.currentItem().text()
        self.db.delete_template(template)
        self.SetTemplatesList()
        self.SetViewTemplate(None, None)
        self.name_template_view.setText("View Template")

    def GeraTemplate(self):
        quetion = MessageDialogBox(
            "Atenção", "Deseja realmente gerar o template?")._ShowQuestion()

        if quetion == False:
            return False

        template = self.name_template_view.text()
        data = self.db.select_campos_template(template)
        template = self.listWidget.currentItem().text()
        if data == None:
            return False
        else:

            save_file = QFileDialog.getSaveFileName(
                self, "Salvar Arquivo", "", "Excel (*.xlsx)")
            if save_file[0] == "":
                MessageDialogBox(
                    "Atenção", "Selecione um local para salvar o arquivo")._ShowWarning()
                return False
            else:

                gerador = GeraTemplatexls(data, save_file[0], template)
                gerador._Gera_template()

    def eventFilter(self, obj, event):

        if obj == self.btn_page_home and event.type() == QEvent.MouseButtonPress:
            self.content.setCurrentWidget(self.page1)
            return True

        if obj == self.btn_page_config and event.type() == QEvent.MouseButtonPress:
            self.content.setCurrentWidget(self.page2)
            return True

        if obj == self.btn_page_clients and event.type() == QEvent.MouseButtonPress:
            self.content.setCurrentWidget(self.page_view_clients)
            return True

        if obj == self.new_fild_template and event.type() == QEvent.MouseButtonPress:
            self.TemplateWidget._Add_Row()
            return True

        if obj == self.delete_fild_template and event.type() == QEvent.MouseButtonPress:
            self.TemplateWidget._Delete_Row()
            return True

        if obj == self.btn_gerar_template and event.type() == QEvent.MouseButtonPress:
            quention = MessageDialogBox(
                "Atenção", "Deseja finalizar a criacao do template e salvar?")._ShowQuestion()
            if quention == False:
                return True

            data = self.TemplateWidget._Get_Data()
            if data == False:
                return True
            else:
                name_template = self.name_new_template.text()

                if name_template == "":
                    MessageDialogBox(
                        "Atenção", "Digite um nome para o template")._ShowWarning()
                    return True

                if len(data) == 0:
                    MessageDialogBox(
                        "Atenção", "Adicione campos ao template")._ShowWarning()
                    return True

                if self.db.insert_template(name_template, data) == False:
                    MessageDialogBox(
                        "Atenção", "já existe um template com esse nome")._ShowWarning()
                    return True
                self.SetTemplatesList()

                return True

        return super(MainWindow, self).eventFilter(obj, event)


if __name__ == '__main__':
    os.environ['QT_MULTIMEDIA_PREFERRED_PLUGINS'] = 'windowsmediafoundation'
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    ret = app.exec_()
    sys.exit()
