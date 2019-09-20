import logging
import os
import configparser
from common.logger import Logger
logger = Logger(logger='read-db-config').getlog()
logger.setLevel(level=logging.INFO)


class ReadDbConfig:
    """
    读取配置文件，初始化
    """
    def __init__(self):
        self.configer = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        logger.info(file_path)
        self.configer.read(file_path)
        self.__ip = None
        self.__dbname = None
        self.__severport = None
        self.__uname = None
        self.__pword =None

    def readconfig(self,dw):

        """
        通过单位判断读取哪个配置文件，传入ga或者zf
        """
        if dw == "ga":
            self.__ip=self.configer.get("DataBase-ga", "host")
            self.__dbname=self.configer.get("DataBase-ga", "databasename")
            self.__severport = self.configer.get("DataBase-ga", "port")
            self.__uname = self.configer.get("DataBase-ga", "username")
            self.__pword= self.configer.get("DataBase-ga", "password")

        elif dw == "zf":
            self.__ip = self.configer.get("DataBase-zf", "host")
            self.__dbname = self.configer.get("DataBase-zf", "databasename")
            self.__severport = self.configer.get("DataBase-zf", "port")
            self.__uname = self.configer.get("DataBase-zf", "username")
            self.__pword= self.configer.get("DataBase-zf", "password")
        else:
            logger.info("当前单位未配置数据库连接")

    # 返回配置文件中的值
    def host(self,dw):
        self.readconfig(dw)
        return self.__ip

    def databasename(self,dw):
        self.readconfig(dw)
        return self.__dbname

    def port(self,dw):
        self.readconfig(dw)
        return self.__severport

    def username(self,dw):
        self.readconfig(dw)
        return self.__uname

    def password(self,dw):
        self.readconfig(dw)
        return self.__pword


if __name__ == '__main__':
    r=ReadDbConfig()
    logger.info(r.host("ga"))
    logger.info(r.databasename("ga"))
    logger.info(r.port("ga"))
    logger.info(r.username("ga"))
    logger.info(r.password("ga"))

