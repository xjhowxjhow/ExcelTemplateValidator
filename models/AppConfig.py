from core import *
import json
import os


class AppConfig(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # [Accepts ex: 1.0 OR 1,0 OR AMBOS] [v = virgula] [p = ponto] [a = ambos]
        self.number_type = None
        self.defalt_encoding = None
        self.export_excel_pinter_row_limit = None
        self.export_excel_pinter_collum_limit = None
        self.default_export_format = None
        self.default_type_export_layout = None
        self.max_thread_pool = 100
        self.thread_pool_validator = 10
        self.load_config()

        # for auto incoding
        self._encoding_current_file = None

    def load_config(self):
        try:
            with open('config.json', 'r') as f:
                config = json.load(f)
                self.number_type = config['number_type']
                self.export_excel_pinter_row_limit = config['export_excel_pinter_row_limit']
                self.export_excel_pinter_collum_limit = config['export_excel_pinter_collum_limit']
                self.default_export_format = config['default_export_format']
                self.default_encoding = config['default_encoding']
                self.default_type_export_layout = config['default_type_export_layout']
                
        except Exception as e:
            print(e)
            self.number_type = 'p'
            self.export_excel_pinter_row_limit = 10000
            self.export_excel_pinter_collum_limit = 30
            self.default_export_format = 'csv'
            self.default_encoding = 'utf_8'
            self.default_type_export_layout = 'Minima'

            self.save_config()

    def save_config(self):
        try:
            with open('config.json', 'w') as f:
                config = {
                    'number_type': self.number_type,
                    'export_excel_pinter_row_limit': self.export_excel_pinter_row_limit,
                    'export_excel_pinter_collum_limit': self.export_excel_pinter_collum_limit,
                    'default_export_format': self.default_export_format,
                    'default_encoding': self.default_encoding,
                    'default_type_export_layout': self.default_type_export_layout
                }
                json.dump(config, f)
            return True
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
    
    def set_default_encoding(self, default_encoding):
        self.default_encoding = default_encoding
        self.save_config()

    def set_default_type_export_layout(self, default_type_export_layout):
        self.default_type_export_layout = default_type_export_layout
        self.save_config()

    def get_number_type(self):
        return self.number_type

    def get_export_excel_pinter_row_limit(self):
        return self.export_excel_pinter_row_limit

    def get_export_excel_pinter_collum_limit(self):
        return self.export_excel_pinter_collum_limit
    
    def get_default_export_format(self):
        return self.default_export_format
    
    def get_default_encoding(self):
        return self.default_encoding
    
    def get_default_type_export_layout(self):
        return self.default_type_export_layout

    def default_config(self):
        self.number_type = 'p'
        self.export_excel_pinter_row_limit = 10000
        self.export_excel_pinter_collum_limit = 30
        self.default_export_format = 'csv'
        self.default_encoding = 'auto'
        self.default_type_export_layout = 'Minima'
        self.save_config()



    def get_encondingtipes(self):
        return ['auto','ascii','big5','big5hkscs','cp037','cp273','cp424','cp437','cp500','cp720','cp737','cp775','cp850','cp852','cp855',
          'cp856','cp857','cp858','cp860','cp861','cp862','cp863','cp864','cp865','cp866','cp869','cp874','cp875','cp932','cp949',
          'cp950','cp1006','cp1026','cp1125','cp1140','cp1250','cp1251','cp1252','cp1253','cp1254','cp1255','cp1256','cp1257','cp1258',
          'euc_jp','euc_jis_2004','euc_jisx0213','euc_kr','gb2312','gbk','gb18030','hz','iso2022_jp','iso2022_jp_1','iso2022_jp_2',
          'iso2022_jp_2004','iso2022_jp_3','iso2022_jp_ext','iso2022_kr','latin_1','iso8859_2','iso8859_3','iso8859_4','iso8859_5','iso8859_6',
          'iso8859_7','iso8859_8','iso8859_9','iso8859_10','iso8859_11','iso8859_13','iso8859_14','iso8859_15','iso8859_16','johab','koi8_r','koi8_t',
          'koi8_u','kz1048','mac_cyrillic','mac_greek','mac_iceland','mac_latin2','mac_roman','mac_turkish','ptcp154','shift_jis','shift_jis_2004',
          'shift_jisx0213','utf_32','utf_32_be','utf_32_le','utf_16','utf_16_be','utf_16_le','utf_7','utf_8','utf_8_sig']