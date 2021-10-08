from common.excel_handler import Excel
from test_func import login
import unittest
from unittestreport import ddt, list_data
import json
from common.log_handler import logger

import os


@ddt
class TestLogin(unittest.TestCase):

    excel = Excel(r"D:\new-study\data\test_case.xlsx", "login")
    case_data = excel.excel_read()

    @list_data(case_data)
    def test_login(self, item):
        response = json.loads(login(item))
        logger.info(f"测试通过--{item['title']}")
        logger.info(response)
        row = item["case_id"] + 1
        expect_data = eval(item["expected"])
        try:
            self.assertEqual(response["msg"], expect_data["msg"])
        except AssertionError as e:
            self.excel.write_data(row=row, column=8, value="error")
            logger.error(f"测试未通过--{item['title']}")
            logger.error(e)
            raise e
        else:
            self.excel.write_data(row=row, column=8, value="pass")


