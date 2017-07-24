# -*- coding: utf-8 -*-
# 中文注释需要包含以上内容

#输入、输出都需要对中文字符进行处理
import os

# 输入采集数据文件夹地址，返回两个list包含所有AVJ、FLPJ文件路径
def eachFile(filepath):

    A_Dir = os.path.join(filepath, "AVJ").decode('utf8').encode('cp936')
    A_file = os.listdir(A_Dir)
    F_Dir = os.path.join(filepath, "FLPJ").decode('utf8').encode('cp936')
    F_file = os.listdir(F_Dir)

    A_filedir1=[]
    F_filedir1=[]

    for allDir in A_file:
        child = os.path.join(A_Dir, allDir)
        A_filedir1.append(child.decode('gbk'))
        print child.decode('gbk') # .decode('gbk')是解决中文显示乱码问题
    for allDir in F_file:
        child = os.path.join(F_Dir, allDir)
        F_filedir1.append(child.decode('gbk'))
        print child.decode('gbk')  # .decode('gbk')是解决中文显示乱码问题

    return (A_filedir1,F_filedir1)

# new_dir=unicode(r"C:\Users\mingl\Desktop\测试处理数据\test采集7-17", "utf8")
# os.mkdir(new_dir)
Data_dir = raw_input("输入要处理文件夹的地址：")
(A_filedir,F_filedir)=eachFile(Data_dir)
for drr in A_filedir:
    print drr