from test_func import add_project,conf
import unittest
from unittestreport import ddt, list_data
import requests
from common.excel_handler import Excel
from common.tools import replace_data
from common.log_handler import logger
from common.database_handler import MysqlConnect


@ddt
class TestUpdate(unittest.TestCase):
    excel = Excel(r"D:\new-study\data\test_case.xlsx", "add_project")
    project_data = excel.excel_read()
    # print(update_data)

    # 登录获取token
    @classmethod
    def setUpClass(cls) -> None:
        # 通过配置文件读取相关登录数据
        mobile = conf.get("common", "mobile_phone")
        pwd = conf.get("common", "pwd")
        login_data = {"mobile_phone": mobile, "pwd": pwd}
        headers = eval(conf.get("common", "headers"))
        url = conf.get("common", "basic_url") + "/member/login"
        s = requests.request("post", json=login_data, headers=headers, url=url)
        response = s.json()
        cls.member_id = response["data"]["id"]
        token = response["data"]["token_info"]["token"]
        headers["Authorization"] = "Bearer" + " " + token
        cls.headers = headers
        # print(cls.headers)
        # 链接数据库，对进行修改成功的数据进行校验
        cls.mysql = MysqlConnect()

    @list_data(project_data)
    def test_project(self, item):
        search_sql = f'select count(*) from loan where member_id = {self.member_id}'
        # print(search_sql)
        before_count = self.mysql.mysql_do(search_sql)[0]
        print(before_count)
        item = replace_data(str(item), TestUpdate)
        item = eval(item)
        # print(type(item), item)
        res = add_project(item, self.headers)
        print(res)
        try:
            self.assertEqual(res["msg"], eval(item["expected"])["msg"])
            if res["msg"] == "OK":
                last_count = self.mysql.mysql_do(search_sql)[0]
                print(last_count)
                logger.info(f"测试用例--{item['title']}测试通过")

        except AssertionError as e:
            logger.error(f"测试用例--{item['title']}测试失败")
            logger.error(e)


if __name__ == '__main__':
    unittest.main()