import requests
import json
from test_case.login import login
from jsonpath import jsonpath
headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json"}
basic_url = "http://api.lemonban.com/futureloan"

# s = requests.session()
# response = s.post(basic_url + "/member/register", json={"mobile_phone": "13278095111", "pwd": "Zzh12345"}, headers=headers)
# print(response.json())
#
# param = {"pageIndex": 1, "pageSize": 20}
# g = requests.get(basic_url + "/loans", params=param, headers=headers)
# print(g.text)

login_data = {"mobile_phone": "13278095136", "pwd": "Zzh12345"}
s1 = requests.request(method="post", headers=headers, json=login_data, url=basic_url+"/member/login")

print(s1.json()["data"]["token_info"])
print(jsonpath(s1.json(), "$..token"))