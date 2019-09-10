from datebase.database import DataBase
from datebase.getajid import GetAjid

import logging
from logs.logger import Logger
logger = Logger(logger='update_qzzt').getlog()
logger.setLevel(level = logging.INFO)


class UpdateQzzt:
    # 公安端常用操作：设置签章状态
    def update_qzzt(self):
        r =DataBase("ga")
        # 查询最新生成的ajid
        g=GetAjid()
        ajid=g.getajid()
        if type(ajid)==None:
            logger.info("未查询到ajid,无法设置签章状态")
        else:
            sql = "update db_jz.t_jzgl_wj set n_yqz =1 WHERE c_ywid='%s' and c_store_path is not null" % (ajid)
            r.exe_update(sql)
        r.exe_close()


if __name__ =='__main__':
    f=UpdateQzzt()
    f.update_qzzt()
