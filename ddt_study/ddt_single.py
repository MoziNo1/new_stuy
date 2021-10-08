
from ddt import ddt,data,unpack,file_data
import unittest


@ddt
class OutputNum(unittest.TestCase):

    @data(1, 2, 3)
    def test_output(self, value):
        print(value)

    @data((1, 2, 3), (4, 5, 6))
    def test_output1(self, value):
        print(value)

    @data((1, 2, 3), (4, 5, 6))
    @unpack
    def test_output2(self, value, value2, value3):
        print(value, value2, value3)

    @data([{'name': 'lili', 'age': 12},{'sex': 'male', 'job': 'teacher'}])
    @unpack
    def test_01(self, a, b):
        print(a, b)

    @data({'name': 'lili', 'age': '16'}, {'name': 'female', 'age': 'nurser'})
    @unpack
    # unpack拆分字典中数据时，下面方法中的形参名称必须与字典中的key键名称相同
    def test_01(self, name, age):
        # 此处取出来的是字典中的value
        print(name, age)


if __name__ == '__main__':
    unittest.main()