from core import *
from models.Database import Database


class GeraTemplatexls(object):
    def __init__(self, headers, path, template_name):
        self.headers = headers
        self.path = path
        self.template_name = template_name
        self.db = Database()
        self.wb = xl.Workbook()
        self.ws1 = self.wb.active
        self.ws1.title = f'Template - {str(template_name)}'
        self.ws2 = self.wb.create_sheet("Legenda Template")

    def _LegendaTemplateSheet(self, template_name) -> list:
        return self.db.get_descr_template(template_name)

    def _Gera_template(self):
        data_descr_sheet = self._LegendaTemplateSheet(self.template_name)
        headers_descr_sheet = ['ORDEM','NOME', 'TIPO', 'TAMANHO', 'OBRIGATORIO',
                               'APENAS_LISTA', 'LISTA_DE_VALORES', 'COLUNA_UNICA']
        self.ws2.append(headers_descr_sheet)

        for row in range(len(data_descr_sheet)):
            for col in range(len(data_descr_sheet[row])):
                cell = self.ws2.cell(row=row+2, column=col+1)
                cell.value = data_descr_sheet[row][col]
                cell.font = Font(color="000000")
                cell.fill = PatternFill(
                    start_color='97d3ff', end_color='97d3ff', fill_type='solid')
                cell.border = Border(left=Side(border_style='thin'),
                                     right=Side(border_style='thin'),
                                     top=Side(border_style='thin'),
                                     bottom=Side(border_style='thin'))

        for col_index, header_coll in enumerate(self.headers, start=1):
            cell = self.ws1.cell(row=1, column=col_index)
            cell.font = Font(color="FFFFFF")
            cell.alignment = Alignment(horizontal='center', vertical='center')

            if header_coll[1] == '1':
                red_fill = PatternFill(
                    start_color='FFFF0000', end_color='FFFF0000', fill_type='solid')
                cell.fill = red_fill
            else:
                black_fill = PatternFill(
                    start_color='FF000000', end_color='FF000000', fill_type='solid')
                cell.fill = black_fill

            cell.value = header_coll[0]

        self.wb.save(self.path)
        return True
