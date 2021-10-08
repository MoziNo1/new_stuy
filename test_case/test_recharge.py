from test_case.test_func import recharge
import unittest
from unittestreport import ddt, list_data
from common.excel_handler import Excel
from common.log_handler import logger
from common.database_handler import MysqlConnect


@ddt
class TestRecharge(unittest.TestCase):
    excel_recharge = Excel(r"D:\new-study\data\test_case.xlsx", "recharge")
    excel_login = Excel(r"D:\new-study\data\test_case.xlsx", "login")
    recharge_case_data = excel_recharge.excel_read()
    login_data = excel_login.excel_read()[0]

    @classmethod
    def setUpClass(cls) -> None:
        cls.mysql = MysqlConnect()

    @list_data(recharge_case_data)
    def test_recharge(self, item, mid=login_data):
        # 获取充值前余额
        # mysql = MysqlConnect()
        begin_sql = f'select leave_amount from member where id = "{eval(item["data"])["member_id"]}"'
        begin_amount = float(self.mysql.mysql_do(begin_sql)[0][0])
        print(begin_amount)
        response = recharge(item, mid)
        # print(response)
        rows = item["case_id"] + 1
        try:
            self.assertEqual(response["msg"], eval(item["expected"])["msg"])
            if response["msg"] == "OK":
                end_sql = f'select leave_amount from member where id = "{eval(item["data"])["member_id"]}"'
                # print(type(mysql.mysql_do(end_sql)[0][0]))
                # print(mysql.mysql_do(end_sql)[0][0])
                end_amount = float(self.mysql.mysql_do(end_sql)[0][0])
                print(end_amount)
                recharge_amount = eval(item["data"])["amount"]
                # print(type(recharge_amount))
                if type(recharge_amount) == str:
                    recharge_amount = float(eval(item["data"])["amount"])
                # print(type(recharge_amount))
                # print(recharge_amount)
                self.assertEqual(begin_amount, end_amount - recharge_amount)
            logger.info(response)
        except AssertionError as e:
            logger.error(e)
            self.excel_recharge.write_data(row=rows, column=8, value="error")
            raise e
        else:
            self.excel_recharge.write_data(row=rows, column=8, value="pass")


if __name__ == '__main__':
    unittest.main()