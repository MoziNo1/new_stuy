import re
from common.conf_handler import conf_do


def replace_data(data, cls):
    """
    :param data: 需要替换的数据
    :param cls: 测试类的类名
    :return: 返回替换后的数据
    """

    while re.search('\*(.+?)\*', data):
        # search 返回匹配的第一个对象
        res = re.search('\*(.+?)\*', data)
        # 将要被替换的东西
        res1 = res.group()
        # print(res1)
        # 用什么替换
        res2 = res.group(1)
        # print(res2)
        try:
            value = getattr(cls, res2)
            if type(value) == int:
                value = str(value)
        except Exception as e:
            value = conf_do().get("common", res2)
        data = data.replace(res1, value)

    return data

