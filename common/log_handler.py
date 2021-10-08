import logging
from configparser import ConfigParser
import os


class Logging(object):

    def __init__(self):
        conf = ConfigParser()
        conf.read(r"D:\new-study\conf\param.ini", encoding="utf-8")
        self.name = conf.get("logging", "name")
        self.filename = conf.get("logging", "filename")
        self.collect_level = conf.get("logging", "collect_level")
        self.output_level = conf.get("logging", "output_level")

    def create_log(self):
        # 第一步创建日志收集器
        log = logging.getLogger(name=self.name)

        # 第二步设置日志收集器的等级
        log.setLevel(self.collect_level)

        # 第三步设置日志收集器的输出渠道和日志输出的格式
        control_handler = logging.StreamHandler()
        standard_format = f'[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                          f'[%(levelname)s][%(message)s]  '  # 其中name为getlogger指定的名字
        log_format = logging.Formatter(standard_format)
        control_handler.setFormatter(log_format)

        file_handler = logging.FileHandler(filename=self.filename, encoding="utf-8")
        file_handler.setFormatter(log_format)

        # 设置不同输出渠道的日志输出等级
        control_handler.setLevel(self.output_level)
        file_handler.setLevel(self.output_level)

        # 第四步将输出渠道加到日志收集器中
        log.addHandler(control_handler)
        log.addHandler(file_handler)

        return log


logger = Logging().create_log()