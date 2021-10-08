import yaml
import requests
import json
import random
from common.database_handler import mysql
from common.tools import conf_do

conf = conf_do()
url = conf.get("common", "basic_url")
update_url = conf.get("common", "update_url")

def register(test_data):
    with open(r"D:\new-study\conf\request.yaml") as f:
        res = yaml.load(f)
        headers = res["headers"]
        basic_url = res["basic_url"]
    # loads 将字符串转为字典json格式，dumps将字典json转为字符串
    item_data = test_data["data"]
    item_data = item_data.replace("*mobile_phone*", random_mobile())
    test_param = eval(item_data)
    s = requests.request(url=basic_url+test_data["url"], method="post", headers=headers, json=test_param)
    response = s.text
    return response


# 获取随机手机号
def random_mobile():
    first_three = [135,136,137,138,139]
    # 随机生成前三位
    first = random.choice(first_three)
    # 随机生成中间四位与后四位
    mid_four = random.randint(1000, 9999)
    last_four = random.randint(1000, 9999)
    mobile_phone = str(first) + str(mid_four) + str(last_four)
    search_mobile_sql = """select * from member where mobile_phone = "{}" """ .format(mobile_phone)
    # print(search_mobile_sql)
    res = mysql.mysql_do(search_mobile_sql)
    if res:
        random_mobile()
    else:
        return mobile_phone
    # print(mobile_phone)


def get_cash(cash_data,headers):
    with open(r"D:\new-study\conf\request.yaml") as f:
        res = yaml.load(f)
        basic_url = res["basic_url"]
        param = json.loads(cash_data)
    s = requests.request(method="post", url=basic_url+"/member/withdraw", json=param, headers=headers)
    return s.json()


def login(login_data):
    with open(r"D:\new-study\conf\request.yaml") as f:
        res = yaml.load(f)
        headers = res["headers"]
        basic_url = res["basic_url"]
        param = eval(login_data["data"])
        s = requests.request(method="post", headers=headers, json=param, url=basic_url+login_data["url"])
        # print(basic_url+login_data["url"])
        response = s.text
        return response


def recharge(recharge_data, login_data):
    with open(r"D:\new-study\conf\request.yaml") as f:
        res = yaml.load(f)
        headers = res["headers"]
        basic_url = res["basic_url"]
        param = eval(recharge_data["data"])
        login_response = login(login_data)
        # print(login_response)
        login_json_response = json.loads(login_response)
        # print(login_json_response)
        token = login_json_response["data"]["token_info"]["token"]
        headers["Authorization"] = "Bearer" + " " + token
        # print(headers)
        # print(token)
        s = requests.request(method="post", url=basic_url+recharge_data["url"], headers=headers, json=param)
        return s.json()


def update_user(update_data, headers):
    data = eval(update_data["data"])
    s = requests.request("PATCH", headers=headers, json=data, url=url+update_data["url"])
    return s.json()


def get_info(info_data, headers, member_id):
    info_url = url + info_data["url"].format(member_id)
    print(info_url)
    s = requests.request("get", headers=headers, url=info_url)
    return s.json()


def add_project(project_data, headers):
    data = eval(project_data["data"])
    s = requests.request("post", headers=headers, json=data, url=url+project_data["url"])
    return s.json()
