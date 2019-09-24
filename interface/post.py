import configparser
import os

import requests
import json
from common.logger import Logger
import uuid
import logging

logger = Logger(logger='callinterface').getlog()
logger.setLevel(level=logging.INFO)


class ZfxtInterface:
    """
        处理接口的类，路径等信息从配置文件中读取
    """

    def __init__(self):
        self.configer = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        self.configer.read(file_path)
        id = ""
        taskid = str(uuid.uuid1()).replace("-", "")  # 自动生成uuid
        ptajbh = ""
        ptajglbh = ""
        fsdw = ""
        jsdw = ""
        self.__xtbh = ""
        self.__filepath = ""
        self.__url = " "
        self.__body = {
            "taskId": taskid,
            "ptajbh": id,
            "ptajglbh": ptajglbh,
            "fsdw": fsdw,
            "jsdw": jsdw,
            "qqsj": "2018-10-04 17:30:00",
            "xtbh": self.__xtbh,
            "md5": "86890ddb5eb501f66a3f7c7d3fa6caa5",
            "path": self.__filepath}
        # 头信息
        self.heads = {}

    # 从ini文件中获取当前接口地址
    def interface_url(self, dw):
        if dw == "ga":
            self.__url = self.configer.get("post", "ga")
        elif dw == "zf":
            self.__url = self.configer.get("post", "zf")
        else:
            logger.info("当前单位未配置接口")
        logger.info("接口地址:{}".format(self.__url))
        return self.__url

    # 传入流程编号，文件路径自动拼接
    def get_file_path(self, lcnumber):
        self.__xtbh = lcnumber
        configer = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        configer.read(file_path)
        self.__filepath = configer.get("servicefilepath", "filepath") + '/' + str(lcnumber) + '.zip'
        logger.info("ftp文件地址:{}".format(self.__filepath))
        logger.info("流程:{}".format(self.__xtbh))

    def set_value(self):
        logger.info("开始调用接口，获取接口参数")
        path = '../logs/ajid.txt'
        file = open(path, "r", encoding="utf-8")
        for line in file.readlines():
            newline = line.strip('\n').split("=")
            if "平台案件编号" in newline[0]:
                self.ptajbh = newline[1]
                self.__body["ptajbh"] = self.ptajbh
                logger.info("平台案件编号为" + self.ptajbh)
            if "平台案件关联编号" in newline[0]:
                self.ptajglbh = newline[1]
                self.__body["ptajglbh"] = self.ptajglbh
                logger.info("平台案件关联编号为" + self.ptajglbh)

            if "接收单位编号" in newline[0]:
                self.jsdw = newline[1]
                self.__body["fsdw"] = self.jsdw  # 发送单位和接收单位可能需要调换
                logger.info("接收单位编号为" + self.jsdw)

            if "发送单位编号" in newline[0]:
                self.fsdw = newline[1]
                self.__body["jsdw"] = self.fsdw  # 发送单位和接收单位可能需要调换
                logger.info("发送单位编号为" + self.fsdw)
        file.close()
        self.__body["path"] = self.__filepath
        self.__body["xtbh"] = self.__xtbh
        self.data_json = json.dumps(self.__body)

    def post_main(self, lcnumber, dw):
        self.get_file_path(lcnumber)
        self.interface_url(dw)
        self.set_value()
        logger.info(self.data_json)
        result = requests.post(self.__url, data=self.data_json, headers=self.heads)
        return result.status_code


if __name__ == "__main__":
    f = ZfxtInterface()
    logger.info(f.post_main(104, 'ga'))
