from configparser import ConfigParser
import yaml
r = ConfigParser()
r.read("param.ini", encoding="utf-8")
c = r.get("mysql", "port")
d = r.getint("mysql","port")
print(c, type(c), d, type(d))

with open("data.yaml", "r") as f:
    res = yaml.load(f, Loader=yaml.Loader)
print(res)
