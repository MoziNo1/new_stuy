import os

# 获取当前文件的绝对路径
# abs_path = os.path.abspath("log.txt")
# print(abs_path)
# # 获取文件的所在目录，即上层目录,注意dirname中传入的是文件的绝对路径
# dir_path = os.path.dirname(abs_path)
# print(dir_path)
# # 获取当前文件的根目录，再用dirname
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_path)
