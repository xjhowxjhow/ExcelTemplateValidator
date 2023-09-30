from core import *


class Database:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.create_connection()
        self.create_table_templates()
        self.create_table_fields_types()
        self.create_fields_types()


    def create_connection(self):
        try:
            self.conn = sqlite3.connect("database.db", check_same_thread=False)
            self.cursor = self.conn.cursor()
        except Error as e:
            return e

    def create_table_templates(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS templates (
                seq_id INTEGER PRIMARY KEY AUTOINCREMENT,
                template_nome TEXT NOT NULL,
                campo_ordem INTEGER NOT NULL,
                campo_nome TEXT NOT NULL,
                campo_tipo TEXT NOT NULL,
                campo_tamanho INTEGER NOT NULL,
                campo_obrigatorio TEXT NOT NULL,
                onlylistValue TEXT NOT NULL,
                ListValue BLOB NOT NULL,
                unique_coll TEXT NOT NULL
            )""")
        except Error as e:
            return e
        
    
    def create_table_fields_types(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS fields_types (
                seq_id INTEGER PRIMARY KEY AUTOINCREMENT,
                type_name TEXT NOT NULL
            )""")
            types = ['VARCHAR', 'INTEGER', 'DATE', 'DATETIME', 'NUMBER', 'BOOLEAN', 'TELEFONE', 'CPF', 'CNPJ', 'CEP', 'EMAIL', 'SITE', 'LISTA', 'LISTA MULTIPLA']

            #VERIFICA SE JA EXISTE TIPO
            if self.cursor.execute("SELECT COUNT(*) FROM fields_types").fetchone()[0] > 0:
                return False
            
            for type in types:
                #INSERT OR IGNORE INTO my_table (name, age) VALUES ('Karen', 34) UPDATE my_table SET age = 34 WHERE name='Karen'
                self.cursor.execute(""" INSERT OR IGNORE INTO fields_types (type_name)  VALUES (?)""", (type,))
                self.conn.commit()
                
        except Error as e:
            print(e)
            return e

    def create_fields_types(self):

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS fields_formats (
            seq_id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL
        )""")

        try:
            #VERIFICA SE JA EXISTE FORMATOS
            if self.cursor.execute("SELECT COUNT(*) FROM fields_formats").fetchone()[0] > 0:
                return False
            
            list_formats =[
                "dd/MM/yyyy HH:mm:ss",
                "dd-MM-yyyy HH:mm",
                "dd-MM-yyyy HH:mm:ss XXX",
                "%d/%m/%Y %H:%M", 
                "%d/%m/%Y %H:%M:%S",
                "%d/%m/%Y %H:%M:%S.%f",
                "yyyy/MM/dd HH:mm:ss.SSS",
                "yyyy/MM/dd HH:mm:ss.SSS XXX",
                "yyyy/MM/dd HH:mm:ss",
                "yyyy/MM/dd HH:mm:ss XXX",
                "yyyyMMddHHmmss",
                "yyyy/MM/dd",
                "yyyy-MM-dd",
                "yyyy-MM-dd HH:mm:ss",
                "yyyy-MM-dd HH:mm:ss XXX",
                "yyyyMMdd",
                "MM/dd/yyyy",
                "MM/dd/yyyy HH:mm:ss",
                "MM-dd-yyyy",
                "MM-dd-yyyy HH:mm:ss",
                "MM/dd/yy",
                "MM-dd-yy",
                "dd/MM/yyyy",
                "yyyy-MM-dd'T'HH:mm:ss.SSSXXX",
                "yyyy-MM-dd HH:mm:ss.SSS",
                "#,##0.###",
                "0.00",
                "0000000000000",
                "#.#",
                "#",
                "###,###,###.#",
                "#######.###",
                "#####.###%"
            ]
            for format in list_formats:
                self.cursor.execute("""INSERT OR IGNORE INTO fields_formats (type) VALUES (?)""", (format,))
                self.conn.commit()
        except Error as e:
            print(e)
            return e
    def insert_template(self, template_nome, lista_campos):

        # VERIFICA SE JA EXISTE NOME DE TEMPLATE
        exists = self.cursor.execute(
            "SELECT COUNT(*) FROM templates WHERE template_nome = ?", (template_nome,)).fetchone()[0]
        if exists > 0:
            return False
        else:
            print(lista_campos)
            for items in lista_campos:
                self.cursor.execute("""INSERT INTO templates (template_nome, campo_ordem,campo_nome, campo_tipo, campo_tamanho, campo_obrigatorio,onlylistValue,ListValue,unique_coll) VALUES (?,?,?,?,?,?,?,?,?)""", (
                    template_nome, items[0], items[1], items[2], items[3], items[4], items[5], items[6], items[7]))
                self.conn.commit()

    def select_all_templates_names(self):
        try:
            self.cursor.execute("SELECT DISTINCT template_nome FROM templates")
            return self.cursor.fetchall()
        except Error as e:
            return e

    def select_config_template(self, template_nome):
        try:
            self.cursor.execute(
                "SELECT campo_ordem,campo_nome,campo_tipo,campo_tamanho,campo_obrigatorio,onlylistValue,ListValue,unique_coll FROM templates WHERE template_nome = ? ORDER BY 1 ASC", (template_nome,))
            return self.cursor.fetchall()
        except Error as e:
            return e

    def delete_template(self, template_nome):
        try:
            self.cursor.execute(
                "DELETE FROM templates WHERE template_nome = ?", (template_nome,))
            self.conn.commit()
        except Error as e:
            return e

    # gerador de template

    def select_campos_template(self, template_nome):
        try:
            self.cursor.execute(
                "SELECT campo_nome, campo_obrigatorio FROM TEMPLATES WHERE template_nome = ? ORDER BY campo_ordem ASC", (template_nome,))
            return self.cursor.fetchall()
        except Error as e:
            return e

    def select_camposnome_template(self, template_nome):
        try:
            self.cursor.execute(
                "SELECT campo_nome FROM TEMPLATES WHERE template_nome = ? ORDER BY campo_ordem ASC", (template_nome,))
            return self.cursor.fetchall()
        except Error as e:
            return e

    def template_exists(self, template_nome):
        try:
            exists = self.cursor.execute(
                "SELECT 1 FROM TEMPLATES WHERE template_nome = ?", (template_nome,))
            if exists:
                return True
            else:

                return False

        except Error as e:
            return e

    def template_num_colls(self, template_nome):
        try:

            self.cursor.execute(
                "SELECT count(campo_nome) FROM templates WHERE template_nome = ?", (template_nome,))
            return self.cursor.fetchall()
        except Error as e:
            return e

    # Validador Type
    # ////////////////////////////////////////////////////////

    def type_field(self, template_name, field_name):
        try:
            self.cursor.execute(
                "SELECT campo_tipo FROM templates WHERE template_nome = ? AND campo_nome = ?", (template_name, field_name))
            return self.cursor.fetchone()[0]
        except Error as e:
            return e

    def obrigatorio_field(self, template_name, field_name):
        try:
            self.cursor.execute(
                "SELECT campo_obrigatorio FROM templates WHERE template_nome = ? AND campo_nome = ?", (template_name, field_name))
            return self.cursor.fetchone()[0]
        except Error as e:
            return e

    def tamanho_field(self, template_name, field_name):
        try:
            self.cursor.execute(
                "SELECT campo_tamanho FROM templates WHERE template_nome = ? AND campo_nome = ?", (template_name, field_name))
            return self.cursor.fetchone()[0]
        except Error as e:
            return e

    def only_list_values_field(self, template_name, field_name):
        try:
            self.cursor.execute(
                "SELECT onlylistValue FROM templates WHERE template_nome = ? AND campo_nome = ?", (template_name, field_name))
            return self.cursor.fetchone()[0]
        except Error as e:
            return e

    def list_values_field(self, template_name, field_name):
        try:
            self.cursor.execute(
                "SELECT ListValue FROM templates WHERE template_nome = ? AND campo_nome = ?", (template_name, field_name))
            return self.cursor.fetchone()[0]
        except Error as e:
            return e

    def unique_values_field(self, template_name, field_name):
        try:
            self.cursor.execute(
                "SELECT unique_coll FROM templates WHERE template_nome = ? AND campo_nome = ?", (template_name, field_name))
            return self.cursor.fetchone()[0]
        except Error as e:
            return e

    def get_all_fields_uniques(self, template_name):
        try:
            self.cursor.execute(
                "SELECT campo_nome FROM templates WHERE template_nome = ? AND unique_coll = '1'", (template_name,))
            return self.cursor.fetchall()
        except Error as e:
            return e

    def get_descr_template(self, template_name):
        try:
            self.cursor.execute(f"""
                                SELECT  campo_ordem AS ORDEM
                                        ,campo_nome AS NOME
	                                    ,campo_tipo as TIPO
	                                    , campo_tamanho AS TAMANHO
	                                    ,campo_obrigatorio AS OBRIGATORIO
	                                    ,onlylistValue AS APENAS_LISTA
	                                    ,ListValue AS LISTA_DE_VALORES
	                                    ,unique_coll AS COLUNA_UNICA
                                FROM templates
                                WHERE template_nome = '{template_name}' ORDER BY 1 ASC""")
            return self.cursor.fetchall()
        
        except Error as e:
            return e


#   def
# if __name__ == "__main__":
#     db = Database()
#     db.create_connection()
