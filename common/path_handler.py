import os

# 首先获取当前文件的绝对路径
current_path = os.path.abspath(__file__)
# print(current_path)
# 获取根目录
base_dir_path = os.path.dirname(os.path.dirname(current_path))
# print(base_dir_path)
# 配置文件路径
conf_path = os.path.join(base_dir_path, "conf")
# print(conf_path)
data_path = os.path.join(base_dir_path, "data")
# print(data_path)
log_path = os.path.join(base_dir_path, "log")
# print(log_path)
report_path = os.path.join(base_dir_path, "report")
# print(report_path)
case_path = os.path.join(base_dir_path, "test_case")
# print(case_path)




