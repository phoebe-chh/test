import time
import logging
from common.logger import Logger
logger = Logger(logger='searchresult').getlog()
logger.setLevel(level = logging.INFO)


class SaveResultToFile:
    """
    保存数据到文件中

    """
    # 保存数据到文件，传入数据标识，和字符串内容
    def clearfile(self):
        logger.info("保存结果到logs/ajid.txt")
        path = "../logs/ajid.txt"
        with open(path, "w", encoding="utf-8") as f:
            pass

    # 写入字符串到文件中，保存时用=分开
    def writefile(self,name,str):
        logger.info("保存结果到logs/ajid.txt")
        path="../logs/ajid.txt"
        with open(path, "a", encoding="utf-8") as f:
            rq = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
            f.write("当前时间" + rq + "\n")
            if len(str) == 0:
                logger.info("请不要保存空字符串到文件中")
            else:
                if name == 'ajid':
                    self.__ajid = str
                    f.write("存入" + name + "=" + str + "\n")
                else:
                    f.write(name + "=" + str + "\n")

    # 读取文件内容，传入数据标识，通过=号进行区分，返回=号后面内容
    def readfile(self,name):
        path = "../logs/ajid.txt"
        lines=[]
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if "=" in line:
                    lines = line.strip('\n').split("=")
                    logger.info(lines)
        return lines[1]  # 返回=号右边的内容

    # def searchdatafromdb(self,sql):
    #      = DataBase('ga')
    #

    # 从数据库查询数据,当前sql是查询tb表的数据
    # def searchdatafromdb(self):
    #     s = DataBase('ga')
    #     # id = GetAjidFromUrl().getajidfromurl()
    #     logger.info("查询到的ajid:{}".format( self.__ajid))
    #     # 查询sql
    #     sql = "SELECT * from (select ajxx.c_ajmc,ajxx.c_id,ajxx.c_jcajid,ajxx.n_tbxtzt,corp.c_alias alise_js FROM db_yw.t_tb_ajxx ajxx" \
    #         "  join db_uim.t_aty_corp corp on ajxx.c_jcyjsdw=corp.c_id where ajxx.c_id='%s')t1," \
    #         "(select corp.c_alias alise_fs FROM db_yw.t_tb_ajxx ajxx  " \
    #         " join db_uim.t_aty_corp corp on ajxx.c_zcjg=corp.c_id  " \
    #         " where ajxx.c_id='%s' )t2 "%( self.__ajid, self.__ajid)
    #     logger.info("需要通过ajid查询的sql:{}".format(sql))
    #     resda=s.getdata(sql)
    #     return resda

    # 保存结果集
    def savedata_to_record_file(self):
        # 保存结果到log中的record.txt中
        logger.info("保存结果到logs/record.txt中")
        path="../logs/record.txt"
        # 写入文件
        fieldname=self.searchdatafromdb()[0]
        if type(fieldname) == None:
            logger.info("未查询到数据，文件内容不更新")
        else:
            date=self.searchdatafromdb()[1]
            rq = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
            with open(path, "w", encoding="utf-8") as f:
                f.write("当前时间" + rq + "***************测试开始**********************"+"\n")
                for i in range(len(fieldname)):
                    if fieldname[i]=="c_ajmc":
                        fieldname[i]="案件名称"
                    if fieldname[i]=="c_id":
                        fieldname[i] = "平台案件编号"
                    if fieldname[i]=="c_jcajid":
                        fieldname[i] = "平台案件关联编号"
                    if fieldname[i] == "alise_fs":
                        fieldname[i] = "发送单位编号"
                    if fieldname[i] == "alise_js":
                        fieldname[i] = "接收单位编号"
                    if fieldname[i] == "n_tbxtzt":
                        fieldname[i] = "协同编号"
                    f.write(fieldname[i]+"="+str(date[i])+"\n")
                f.write("**************************************此次测试结束********************"+"\n")
            logger.info("保存结果成功")


if __name__ =='__main__':
    Q=SaveResultToFile()
    Q.clearfile()
    Q.writefile('ajid','31321321321')
    # Q.writefile('ajid', '31321321321')
    print(Q.readfile('ajid'))
    # Q.savedata_to_record_file()
