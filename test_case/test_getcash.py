import requests
from test_case.test_func import get_cash
from common.excel_handler import Excel
import unittest
from unittestreport import ddt,list_data
from configparser import ConfigParser
from common.log_handler import logger
from common.tools import replace_data

@ddt
class TestGetcash(unittest.TestCase):
    excel = Excel(r"D:\new-study\data\test_case.xlsx", "getcash")
    cash_data = excel.excel_read()

    @classmethod
    def setUpClass(cls) -> None:
        conf = ConfigParser()
        conf.read(r"D:\new-study\conf\param.ini", encoding="utf-8")
        login_data = {"mobile_phone": conf.get("common", "mobile_phone"),
                      "pwd": conf.get("common", "pwd")
                      }
        headers = eval(conf.get("common", "headers"))
        url = conf.get("common", "basic_url")
        s = requests.request(method="post", json=login_data, headers=headers, url=url+"/member/login")
        response = s.json()
        # print(response)
        token = response["data"]["token_info"]["token"]
        headers["Authorization"] = "Bearer" + " " + token
        cls.headers = headers
        # print(cls.headers)
        cls.member_id = response["data"]["id"]
        # print(cls.member_id)

    @list_data(cash_data)
    def test_getcash(self, item):
        data = item["data"]
        # 正则替换数据
        cash_data = replace_data(data, TestGetcash)
        # cash_data = data.replace("*member_id*", str(self.member_id))
        response = get_cash(cash_data, self.headers)
        # print(response)
        try:
            self.assertEqual(eval(item["expected"])["msg"], response["msg"])
            logger.info(f"测试通过--{item['title']}")
        except AssertionError as e:
            logger.error(e)
            raise e

# if __name__ == '__main__':
#     unittest.main()