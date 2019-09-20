#coding:utf-8
import xml.dom.minidom
import logging

from common.readconfig import ReadConfig
from common.logger import Logger
logger = Logger(logger='repleace-file').getlog()
logger.setLevel(level = logging.INFO)


class ReplaceFileContent:
    '''处理xml，用相应的字段替换
    xml模板本地文件夹中，根据record中的字段内容替换xml中字段内容
    本地文件夹的路径在ini配置文件中
    '''

    def getnodename(self):
        logger.info("找到record.txt文件中记录的节点名称")
        now_file_path = '../logs/ajid.txt'
        nodename = []
        with open(now_file_path, "r", encoding="utf-8") as f:
            for line in f:
                if "=" in line:
                    lines=line.strip('\n').split("=")
                    nodename.append(lines[0])
        return nodename
    # 从ini文件中读取本地文件的路径
    def get_file_path(self):
        cg=ReadConfig()
        return cg.getvalue('localPath','path')

    def getnodecontent(self):
        logger.info("找到record.txt文件中需要替换的节点内容")
        now_file_path = '../logs/ajid.txt'
        nodecontent = []
        with open(now_file_path, "r", encoding="utf-8") as f:
            for line in f:
                if "=" in line:
                    lines = line.strip('\n').split("=")
                    nodecontent.append(lines[1])
        return nodecontent

    def replace_content(self,xtbh):
        oldcontent = self.getnodename()
        logger.info("需要替换的节点为%s"%oldcontent)
        newcontent = self.getnodecontent()
        logger.info("需要替换成%s" % newcontent)
        logger.info("找到ajxx.xml的路径")
        # xmlpath = "../xmls/ajxx.xml"
        xmlpath=self.get_file_path() +'/'+str(xtbh)+"/"+"ajxx.xml" # 从配置文件中读取的文件路径
        xmlobject = open(xmlpath, 'r', encoding='UTF-8')
        DOMTree = xml.dom.minidom.parse(xmlobject)
        root = DOMTree.documentElement
        file_data = ''
        logger.info("开始替换内容")
        with open(xmlpath, "r", encoding="utf-8") as f:
            for line in f:
                for j in range(len(oldcontent)):
                    if oldcontent[j] in line:
                        itemlist = root.getElementsByTagName(oldcontent[j])
                        for i in range(len(itemlist)):
                            old_str = itemlist[i].firstChild.data
                            new_str = newcontent[j]
                            line = line.replace(old_str, new_str)
                file_data += line
        with open(xmlpath, "w", encoding="utf-8") as f:
            f.write(file_data)
        xmlobject.close()
        logger.info("文件内容替换结束")
        return xmlpath
    #
    # def copyfile(self,path):
    #     # 把生成好的xml放在某个文件夹中
    #     shutil.copy(self.replace_content(), path)
    #     logger.info("xml已经替换成功，放在路径%s"%path)


if __name__ == "__main__":
    f=ReplaceFileContent()
    print(f.getnodename())
    print(f.getnodecontent())
    # f.getnodecontent()
    xmlp=f.replace_content(204)
    # f.copyfile(r"C:\Users\lenovo\Desktop\kkk\test\TB\104")
