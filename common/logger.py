import logging
import time
import os


class Logger(object):
    def __init__(self, logger):
        '指定保存日志的文件路径，日志级别，以及调用文件,将日志存入到指定的文件中'
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        # 创建一个handler，用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # log_dir = os.path.abspath('.')+'../logs/'
        log_dir = os.path.abspath('..') + '/logs/'
        # log_name = rq + '.log'
        log_name = log_dir + rq + '.log'
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.DEBUG)
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # ch.setLevel(logging.ERROR)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger


if __name__ == "__main__":
    logger = Logger(logger='callinterfacetest').getlog()
    logger.setLevel(level=logging.INFO)
    logger.debug("this is  debug")
    logger.info("this is info")
    logger.error("error")
