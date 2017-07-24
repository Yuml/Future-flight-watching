# -*- coding: utf-8 -*-
# 中文注释需要包含以上内容

#输入、输出都需要对中文字符进行处理
import os

def eachFile(filepath):
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join(filepath, allDir)
        print child.decode('gbk') # .decode('gbk')是解决中文显示乱码问题

#不能正常打开含中文的文件夹目录？需要增加  .decode('utf8').encode('cp936')
fp = "C:\\Users\\mingl\\Desktop\\测试处理数据\\test采集7-17".decode('utf8').encode('cp936')
#ufp=fp.decode('gbk')
#ufp = unicode(fp,'utf-8')
eachFile(fp)