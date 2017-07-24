# -*- coding: utf-8 -*-
import os

filepath = r"C:\Users\mingl\Desktop\测试处理数据\test采集7-17\\"
A_Dir = os.path.join(filepath, "out_AVJ").decode('utf8').encode('cp936')
out_A_file = os.listdir(A_Dir)
F_Dir = os.path.join(filepath, "out_FLPJ").decode('utf8').encode('cp936')
out_F_file = os.listdir(F_Dir)


A_filedir1=[]
F_filedir1=[]

for allDir in out_A_file:
    child = os.path.join(A_Dir, allDir)
    A_filedir1.append(child.decode('gbk'))
    # print child.decode('gbk') # .decode('gbk')是解决中文显示乱码问题
for allDir in out_F_file:
    child = os.path.join(F_Dir, allDir)
    F_filedir1.append(child.decode('gbk'))
    # print child.decode('gbk')  # .decode('gbk')是解决中文显示乱码问题

output_txt=open(os.path.join(filepath, "ALL_AVJ.txt").decode('utf8').encode('cp936'),"w")
for fl in A_filedir1:
    input_txt=open(fl,"r")
    output_txt.write(input_txt.read())
    input_txt.close()
output_txt.close()

output_txt=open(os.path.join(filepath, "ALL_FLPJ.txt").decode('utf8').encode('cp936'),"w")
for fl in F_filedir1:
    input_txt=open(fl,"r")
    output_txt.write(input_txt.read())
    input_txt.close()
output_txt.close()