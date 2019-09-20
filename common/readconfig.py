import logging
import os
import configparser
from common.logger import Logger
logger = Logger(logger='read-config').getlog()
logger.setLevel(level=logging.INFO)


class ReadConfig:
    """
    读取配置文件，初始化
    """
    def __init__(self):
        self.configer = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        logger.info(file_path)
        self.configer.read(file_path)

    def readconfig(self,nodename,childname):

        """
        通过单位判断读取哪个配置文件，传入ga或者zf
        """
        try:
            value=self.configer.get(nodename,childname)
            return value
        except configparser.NoSectionError as e:
            logger.info("当前选项无数据，异常信息{}".format(e))
        except configparser.NoOptionError as e:
            logger.info("当前选项无数据，异常信息{}".format(e))

    # 返回配置文件中的值
    def getvalue(self,nodename,childname):
        reda=self.readconfig(nodename,childname)
        return reda


if __name__ == '__main__':
    r=ReadConfig()
    logger.info(r.getvalue("DataBase-ga","host"))

