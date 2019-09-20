from datebase.database import DataBase
import logging
from common.logger import Logger
logger = Logger(logger='getajid').getlog()
logger.setLevel(level=logging.INFO)

'''
说明：
    公安端常用操作：获取案件id
    获取101阶段的ajid，即页面发起提捕时最新生成的ajid
'''


class GetAjid:
    def getajid(self):
        db= DataBase("ga")
        # 查询最新生成的ajid，和当前时间的时间差为3分钟以内
        sql ="select c_id from db_yw.t_tb_ajxx ajxx where d_xgsj between " \
             "(SELECT current_timestamp - interval '10 minute') and current_timestamp ORDER BY d_xgsj DESC LIMIT 1" \
             # "and n_tbxtzt=101"
        resda =db.getdata(sql,0)[1]
        if type(resda)==None:
            logger.info("未查询到该sql的结果")
        else:
            logger.info("查询到的ajid:{}".format(resda))
            return resda


if __name__ == '__main__':
    r=GetAjid()
    logger.info(r.getajid())

