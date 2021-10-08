import pymysql
from configparser import ConfigParser
import os


class MysqlConnect(object):

    def __init__(self):
        # 通过配置文件读取相关数据库链接信息
        mysql_ini = ConfigParser()
        mysql_ini.read(r"D:\new-study\conf\param.ini", encoding="utf-8")
        self.host = mysql_ini.get("mysql", "host")
        self.port = mysql_ini.getint("mysql", "port")
        self.username = mysql_ini.get("mysql", "username")
        self.password = mysql_ini.get("mysql", "password")
        self.db = mysql_ini.get("mysql", "db")
        self.con = pymysql.connect(host=self.host, port=self.port, user=self.username, password=self.password,
                                       db=self.db)

    def mysql_do(self, sql):
        """连接数据库"""
        connect = pymysql.connect(host=self.host, port=self.port, user=self.username, password=self.password,
                                       db=self.db)
        # 创建游标
        all_data =()
        cur = connect.cursor()

        # 执行sql语句
        try:
            # result = []
            cur.execute(sql)
            if "select" in sql:
                all_data = cur.fetchall()
                cur.close()
                # self.connect.close()
            else:
                connect.commit()
        except Exception as e:
            connect.rollback()
            raise e
        finally:
            return all_data


mysql = MysqlConnect()





