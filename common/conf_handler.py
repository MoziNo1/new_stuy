from configparser import ConfigParser


def conf_do():
    conf = ConfigParser()
    conf.read(r"D:\new-study\conf\param.ini", encoding="utf-8")
    return conf
