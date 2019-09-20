import paramiko
import logging

from common.readconfig import ReadConfig
from common.logger import Logger

logger = Logger(logger='putonserver').getlog()
logger.setLevel(level = logging.INFO)


class PutOnService:
    """
    把文件放在服务类
    参数：单位，ga或者zf
    服务器配置，ip，端口，用户名，密码等读取ini文件
    """
    def __init__(self,dw):
        cg = ReadConfig()
        if dw == 'ga':
            self.__hostname =cg.getvalue('FtpServer-ga','host')
            self.__port = int(cg.getvalue('FtpServer-ga', 'port'))
            self.__username = str(cg.getvalue('FtpServer-ga', 'username'))
            self.__password = str(cg.getvalue('FtpServer-ga', 'password'))
        elif dw == 'zf':
            self.__hostname = cg.getvalue('FtpServer-zf','host')
            self.__port = int(cg.getvalue('FtpServer-zf', 'port'))
            self.__username = cg.getvalue('FtpServer-zf', 'username')
            self.__password = cg.getvalue('FtpServer-zf', 'password')
        else:
            logger.info("该单位未配置ftp服务器")

    # 链接服务器
    def link_server(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接服务器
        ssh.connect(hostname=self.__hostname,port=self.__port,username=self.__username,password=self.__password)
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command('ls /opt')
        # 获取命令结果
        res, err = stdout.read(), stderr.read()
        result = res if res else err
        logger.info("result.decode为%s"%result.decode())
        if result.decode():
            logger.info("ok，登陆服务器%s成功！"% self.__hostname)
        else:
            logger.info("登陆%s失败！"% self.__hostname)

    # 推送文件
    def putto_server(self,xtbh):
        cg = ReadConfig()
        localpath = cg.getvalue('localPath', 'path') + '\\' + str(xtbh)+'.zip'
        logger.info("本地文件路径{}".format(localpath))
        servicepath='/home/ftp'+cg.getvalue('servicefilepath', 'filepath') + '/' + str(xtbh)+'.zip'
        logger.info("ftp服务器路径{}".format(servicepath))
        transport = paramiko.Transport(self.__hostname,self.__port)
        transport.connect(username=self.__username, password=self.__password)
        logger.info("连接服务器%s成功，开始上传压缩包" % self.__hostname)
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(localpath,servicepath)
        logger.info("上传到服务器成功")
        sftp.close()


if __name__ == "__main__":
    # servicepath="/home/ftp/autotest/104.zip"
    # localpath=r"C:\Users\lenovo\Desktop\kkk\test\TB\after_jiami\104.zip"
    f=PutOnService('zf')
    f.putto_server(204)
    # f.link_server()