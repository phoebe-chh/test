import zipfile
import os
import logging

from common.readconfig import ReadConfig
from common.logger import Logger
logger = Logger(logger='zipallfile').getlog()
logger.setLevel(level = logging.INFO)


class ZipAllFile:
    """
    压缩文件类
    参数需要提供当前需要压缩文件的协同编号
    """
    def zip_file(self,xtbh):
        """文件夹名称以协同编号结尾"""
        cg = ReadConfig()
        zippath = cg.getvalue('localPath', 'path') + '\\' + str(xtbh)
        file_news=zippath+".zip"
        logger.info(file_news)
        # 压缩文件
        z = zipfile.ZipFile(file_news,'w',zipfile.ZIP_DEFLATED)
        for dirpath, dirnames, filenames in os.walk(zippath):
            fpath = dirpath.replace(zippath, '')
            fpath = fpath and fpath + os.sep or ''
            for filename in filenames:
                z.write(os.path.join(dirpath, filename), fpath + filename)
        z.close()
        if os.path.exists(file_news):
            logger.info('文件压缩成功')
        else:
            logger.info('文件压缩失败')
        return file_news

if __name__ == "__main__":
    f=ZipAllFile()
    # path=r"C:\Users\lenovo\Desktop\kkk\test\TB\104"
    u=f.zip_file(204)
    print(u)