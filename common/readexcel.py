import  pandas  as pd
import logging
from common.logger import Logger
logger = Logger(logger='readconfig').getlog()
logger.setLevel(level=logging.INFO)


class ReadExcel:
    """
    说明：
        通用方法，读取配置文件，配置文件中包含了页面元素位置，需要手动维护
    """
    # 初始化数据
    def initestdata(self):
        self._indexnumber=[]

    # 读取的配置文件中的页面名称
    def testcase_name(self, casename):
        self.initestdata()  # 初始化数据
        self.df = pd.read_excel(r'../config/config.xlsx',sheet_name='config')
        test_data = []
        for i in self.df.index.values:  # 获取行号的索引，并对其进行遍历：
            row_data = self.df.loc[i].reindex(['页面名称'])  # 根据i来获取每一行指定的数据 并存入到列表中
            test_data.append(row_data[0])
            if row_data[0] == casename:
                self._indexnumber.append(i)  # 保存当前所在行
        return self._indexnumber  # 返回行数列表

    # 通过对象名称和页面名称，从配置文件中获取页面元素路径
    def get_element(self,pagename,elementname):
        pname = self.testcase_name(pagename)
        elename = self.element_name()
        elepath = self.elements_path()
        elenumber=0
        for i in range(len(pname)):
            if elename[i] == 'nan':
                logger.info("测试对象为空，请检查配置文件")
            elif elename[i] == elementname:
                logger.info("操作第%s行元素,当前测试对象元素路径：%s"%(str(pname[i]+2),elepath[i]))
                elenumber=i
                break
        return elepath[elenumber]

    # 定位方式，id或者xpath等
    def lcoalte_model(self):
        test_data = []
        for i in self._indexnumber:
            row_data = self.df.loc[i].reindex(['定位方式'])
            test_data.append(row_data[0])
        return test_data

    # 测试对象名称
    def element_name(self):
        elename =[]
        for i in self._indexnumber:
            row_data = self.df.loc[i].reindex(['测试对象名称'])
            elename.append(row_data[0])
        newlist=set(elename)  # 转换成set，检查是否有重复元素
        if len(newlist)==len(elename):
            return elename
        else:
            raise ValueError("当前页面元素的对象名称重复，请检查配置文件")

    # 元素路径
    def elements_path(self):
        test_data = []
        for i in self._indexnumber:
            row_data = self.df.loc[i].reindex(['控件元素'])
            test_data.append(row_data[0])
        return test_data

    # 测试数据，一般用在sendkeys时
    def test_data(self):
        test_data = []
        for i in self._indexnumber:
            row_data = self.df.loc[i].reindex(['测试数据'])
            if isinstance(row_data[0],str):
                test_data.append(row_data[0])
            elif isinstance(row_data[0],int):
                temp=int(row_data[0])
                test_data.append(str(temp))
            else:
                test_data.append(str(row_data[0]))
        return test_data

    # 操作元素的方式，sendkeys或者click等
    def operate_method(self):
        test_data = []
        for i in self._indexnumber:
            row_data = self.df.loc[i].reindex(['操作方法'])
            test_data.append(row_data[0])
        return test_data

    # 间隔时间，操作元素之间的间隔，暂停几秒
    def pause_time(self):
        test_data = []
        for i in self._indexnumber:
            row_data = self.df.loc[i].reindex(['间隔时间'])
            test_data.append(int(row_data[0]))
        return test_data

    # 通过对象名称获取测试数据
    def get_test_data_by_name(self,pagename,elementname):
        self.testcase_name(pagename)
        elename=self.element_name()
        testdata=self.test_data()

        for i in self._indexnumber:
            if elename[i]==elementname:
                logger.info("找到测试对象,当前测试对象的测试数据：%s"%(testdata[i]))
                return testdata[i]


if __name__ == "__main__":
    r=ReadExcel()
    # s=r.testcase_name('login_page')
    # print(r.pause_time())
    # print(r.element_name())
    print(r.get_element('login_page','element1'))
    print(r.get_test_data_by_name('login_page', 'element1'))