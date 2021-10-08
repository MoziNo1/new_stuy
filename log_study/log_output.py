import logging

"""
logging 默认日志收集器为root ，让创建日志收集器没有传name值时，使用的则为root日志收集器，默认收集warning以上等级的信息

"""

log = logging.getLogger(name="log_test")
# setlevel设置当前日志收集器的收集等级
log.setLevel("DEBUG")
# 创建日志收集器的渠道，用于确定输出日志的等级
# StreamHandler 用于将日志输出到控制台 FileHandler用于将日志输出到文件
log_control_tunnel = logging.StreamHandler()
log_file_tunnel = logging.FileHandler("log.txt", encoding="utf-8")
# 设置输出日志的等级
log_control_tunnel.setLevel("DEBUG")
log_file_tunnel.setLevel("ERROR")
# 输出日志的格式,首先通过Formatter实例化对象，然后在实例化的同时，设置输出日志格式的详细信息
standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]' #其中name为getlogger指定的名字
log_format = logging.Formatter(standard_format)
# 将输出日志格式加到固定渠道
log_control_tunnel.setFormatter(log_format)
log_file_tunnel.setFormatter(log_format)
# 最后将日志的传输渠道加到之前创建的日志收集器中
log.addHandler(log_control_tunnel)
log.addHandler(log_file_tunnel)

log.debug("--debug--")
log.info("--info--")
log.warning("--warning--")
log.error("--error--")
log.critical("--critical--")
