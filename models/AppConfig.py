from core import *



class AppConfig(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # [Accepts ex: 1.0 OR 1,0 OR AMBOS] [v = virgula] [p = ponto] [a = ambos]
        self.number_type = None
        self.export_excel_pinter_row_limit = None
        self.export_excel_pinter_collum_limit = None
        self.default_export_format = None
        self.max_thread_pool = 100
        self.thread_pool_validator = 10
        self.load_config()

    def load_config(self):
        try:
            with open('config.json', 'r') as f:
                config = json.load(f)
                self.number_type = config['number_type']
                self.export_excel_pinter_row_limit = config['export_excel_pinter_row_limit']
                self.export_excel_pinter_collum_limit = config['export_excel_pinter_collum_limit']
                self.default_export_format = config['default_export_format']
        except Exception as e:

            self.number_type = 'p'
            self.export_excel_pinter_row_limit = 10000
            self.export_excel_pinter_collum_limit = 30
            self.default_export_format = 'xlsx'
            self.save_config()

    def save_config(self):
        try:
            with open('config.json', 'w') as f:
                json.dump(self.__dict__, f, indent=4)
        except Exception as e:
            return False

    def set_number_type(self, number_type):
        self.number_type = number_type
        self.save_config()

    def set_export_excel_pinter_row_limit(self, export_excel_pinter_row_limit):
        self.export_excel_pinter_row_limit = export_excel_pinter_row_limit
        self.save_config()

    def set_export_excel_pinter_collum_limit(self, export_excel_pinter_collum_limit):
        self.export_excel_pinter_collum_limit = export_excel_pinter_collum_limit
        self.save_config()

    def set_default_export_format(self, default_export_format):
        self.default_export_format = default_export_format
        self.save_config()

    def get_number_type(self):
        return self.number_type

    def get_export_excel_pinter_row_limit(self):
        return self.export_excel_pinter_row_limit

    def get_export_excel_pinter_collum_limit(self):
        return self.export_excel_pinter_collum_limit
    
    def get_default_export_format(self):
        return self.default_export_format

    def default_config(self):
        self.number_type = 'p'
        self.export_excel_pinter_row_limit = 10000
        self.export_excel_pinter_collum_limit = 30
        self.default_export_format = 'xlsx'
        self.save_config()
