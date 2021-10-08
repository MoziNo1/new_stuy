import unittest
from unittestreport import ddt, list_data
from common.database_handler import MysqlConnect
from test_func import register, random_mobile
import json
from common.excel_handler import Excel
from common.log_handler import logger
import re

datas = [{"title": "判断", "name": "乌鸦坐飞机", "age": 18}, {"title": "判断", "name": "www", "age": "123456"}]


@ddt
class TestRegister(unittest.TestCase):

    excel = Excel(file_name=r"D:\new-study\data\test_case.xlsx", sheet_name="register")
    case_data = excel.excel_read()
    print(case_data)

    @list_data(case_data)
    def test_01(self, item):
        response = register(item)
        logger.info(f"测试通过--{item['title']}")
        logger.info(response)
        result = json.loads(response)
        expect_data = json.loads(item["expected"])
        row = item["case_id"] + 1
        try:
            self.assertEqual(result["msg"], expect_data["msg"])
        except AssertionError as e:
            self.excel.write_data(row=row, column=8, value="error")
            logger.error(f"测试未通过--{item['title']}")
            logger.error(e)
            raise e
        else:
            self.excel.write_data(row=row, column=8, value="pass")

    @list_data(datas)
    def test_02(self, item):
        mysql = MysqlConnect()
        res = mysql.mysql_do(f"""select * from member where reg_name = "{item["name"]}" """)
        if res:
            print("可新增用户")
        else:
            print("当前用户已存在")
#
#
# if __name__ == '__main__':
#     unittest.main()