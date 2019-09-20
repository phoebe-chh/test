import psycopg2
import logging

from datebase.readconfig import ReadDbConfig
from common.logger import Logger
logger = Logger(logger ='database').getlog()
logger.setLevel(level=logging.INFO)

"""
 数据库操作类，连接数据，执行sql，并返回数据
"""


class DataBase:

    # 数据库地址等信息参数传入
    def __init__(self,dw):
        confg=ReadDbConfig()
        self.host = confg.host(dw)
        self.datebasename = confg.databasename(dw)
        self.port = confg.port(dw)
        self.user = confg.username(dw)
        self.password = confg.password(dw)

    # 链接数据库
    def connectdatabase(self):
        logger.info("链接数据库%s"%self.host)
        conn = psycopg2.connect(database=self.datebasename, user=self.user,password=self.password,
                                host=self.host,port=self.port)
        cur = conn.cursor()
        return conn,cur

    # 根据sql设置数据库中的字段的值
    def exe_update(self,sql):
        conn = self.connectdatabase()[0]
        cur = conn.cursor()
        try:
            result = cur.execute(sql)
            logger.info("update数据的sql为%s" % sql)
            conn.commit()
            logger.info("commit成功")
            return result
        except Exception as e:
            logger.error("未成功设置字段内容，异常信息%s" % e)

    # 关闭数据库
    def exe_close(self):
        try:
            cur=self.connectdatabase()[0]
            cur.close()
            logger.info("关闭成功")
        except Exception as e:
            logger.info("关闭失败，异常信息：%s" % e)

    # 通过sql，查询数据库，输出数据
    def getdata(self,sql,*number):
        rows=[]
        all_fields=[]
        curn = self.connectdatabase()[1]
        try:
            curn.execute(sql)
            rows = curn.fetchall()  # 返回数据，为一个列表
            all_fields = curn.description  # 返回表头名称
        except Exception as e:
            logger.error("sql执行失败，异常信息%s" % e)
        # 提取列表中的元祖
        if len(rows) == 0:
            logger.info("未查询到数据")
            return None
        else:
            temp = rows[0]
            listdata = []
            for item in temp:  # 转成一个列表
                listdata.append(item)

            listfield =[]
            for item in all_fields:
                listfield.append(item[0])

            if len(listdata) == 0:
                logger.warning("sql执行成功，但是未查到数据，结果集为空，请排查sql")
                return listdata
            if len(listdata) > 0 and number != ():
                n=number[0]
                logger.info("获取表头为:%s" % listfield[n])
                logger.info("获取第{}个数据值为:{}" .format(n+1,listdata[n]))
                return listfield[n],listdata[n]
            if number == ():  # 判断是否未传入参数
                logger.info("返回所有字段%s" % (listfield))
                logger.info("返回所有数据%s" % (listdata))
                return listfield,listdata


if __name__ =='__main__':
    r=DataBase('zf')
    r.connectdatabase()
    sql1 = "select * from db_yw.t_tb_ajxx ajxx where d_xgsj between (SELECT current_timestamp - interval '1 minute') " \
           "and current_timestamp"
    logger.info(type(r.getdata(sql1)))
    # sql = "update db_jz.t_jzgl_wj set n_yqz =1 WHERE c_ywid='E1EA7ACA467143BE9184C467E2FE408A' " \
    #     "and c_store_path is not null"
    # r.exe_update(sql)
    # r.exe_close()
    #

