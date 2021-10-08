import openpyxl
from common.path_handler import data_path
import os

class ExcelTest(object):

    def __init__(self):
        self.data_path = os.path.join(data_path, "test_login_case.xlsx")
        self.sheet_name = "login"

    def do_excel(self):

        workbook = openpyxl.load_workbook(self.data_path)
        sheet = workbook[self.sheet_name]
        rows = list(sheet.rows)
        title = []
        for i in rows[0]:
            title.append(i.value)
        print(title)
        case_data = []
        for i in rows[1:]:
            data = [j.value for j in i]
            case_data.append(dict(zip(title, data)))
        print(case_data)


excel = ExcelTest()
excel.do_excel()