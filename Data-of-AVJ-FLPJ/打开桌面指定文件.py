# -*- coding: utf-8 -*-
# 中文注释需要包含以上内容
import os

#fname = raw_input('Enter the file name: ')
#fname = "test.txt"
fname = "2607AVJ测试.txt"
path="C:\Users\mingl\Desktop\测试处理数据"
filepath = os.path.join(path,fname)

#打开文件时，使用unicode(filepath , "utf8")进行处理
filepath1=unicode(filepath , "utf8")
fhand = open(filepath1)
count = 0
for line in fhand:
    if line.startswith(' G52607') :
        count = count + 1
print 'There were', count, 'subject lines in', fname