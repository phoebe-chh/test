# -*- coding: UTF-8 -*-
# import HTMLTestRunner_cn
libPath = 'D:\\Anaconda3\\Lib\\'
import os
import sys

sys.path.append(libPath)
import HTMLTestRunner_cn
import unittest
import time

# 解决cmd中执行py文件报导入模块不存在的问题
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
# print(sys.path)
# libPath = 'D:\\Anaconda3\\Lib\\'
sys.path.append(rootPath)
# sys.path.append(libPath)
# print(sys.path)
# for file in os.listdir(os.getcwd()):
#      print(file)
sysp = 'D:\\PycharmProjects\\autotest'
sys.path.append(sysp)
# print(sys.path)
case_path = os.path.dirname(os.path.abspath('.')) + '/test_cases/'
# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/test_reports/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式
HtmlFile = report_path + now + "report_example.html"
fp = open(HtmlFile, "wb")

# 构建suite
suite = unittest.defaultTestLoader.discover(case_path, pattern="test_1*.py", top_level_dir=None)

if __name__ == '__main__':
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp, title=u"苏州项目自动化测试报告", description=u"用例测试情况")
    # 开始执行测试套件
    runner.run(suite)
