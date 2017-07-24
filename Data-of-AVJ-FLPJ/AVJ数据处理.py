# -*- coding: utf-8 -*-
# 中文注释需要包含以上内容
import os
import re
#filepath = "C:\Users\mingl\Desktop\测试处理数据\2709AVJ测试.txt".decode('utf8').encode('cp936')

#给定输入路径及文件名及输出路径及文件名
def P_AVJ(filepath_in,filepath_out,in_date):
    if not isinstance(filepath_in, unicode):
        filepath_in = unicode(filepath_in, "utf8")
    if not isinstance(filepath_out, unicode):
        filepath_out = unicode(filepath_out, "utf8")
    fl_no = os.path.basename(filepath_in)[:4]
    mylines1=[]
    lines = open(filepath_in,'r')
    output = open(filepath_out,'w')
    sList=''
    for line in lines:
        if line.startswith(" ",2,4):
            mylines1.append(line[4:].strip())
            sList =sList+line[4:].strip()+" "

    # K1舱、P1舱 没录入
    p1 = r"[1-3][0-9][A-Z][A-Z][A-Z][1-2][0-9].+? N[0-9A-Z]"
    lst = re.findall(p1,sList)
    #for line in lst:
    #    print line

#    p2 = r"(?<=[\s][A-Z])[0-9A-Z]+ "
    # 24JUL17 KWLWUZ 1950   2030   CR9 0   F3 A3 DQ YA TA HA MA GA SA LA QA EA VA RA OA UA ZA XA PA K6 BQ IQ JQ W3 NQ
    p2 = r"(\d{1,2}\w{3})\d{2} (\w{3})(\w{3}) (\d{4}...\d{4})...CR9( \d   )F(\w+) A(\w+) D(\w+) Y(\w+) T(\w+) H(\w+) M(\w+) G(\w+) S(\w+) L(\w+) Q(\w+) E(\w+) V(\w+) R(\w+) O(\w+) U(\w+) Z(\w+) X(\w+) P(\w+) K(\w+) B(\w+) I(\w+) J(\w+) W(\w+) N(\w+)"
    # output.writelines('日期    航段   起飞   落地        F A D Y T H M G S L Q E V R O U Z X P K B I J W N \n')

    MM=dict()
    MM={'JAN':'/01/','FEB':'/02/','MAR':'/03/','APR':'/04/','MAY':'/05/','JUN':'/06/','JUL':'/07/','AUG':'/08/','SEP':'/09/','OCT':'/10/','NOV':'/11/','DEC':'12'}
    # CC=dict()
    # CC={'Q':' ','A':'9','S':' '}

    for line in lst:
        lis2 = re.findall(p2,line)
        for li in lis2:
            l22 = list(li)
            l33 = []
            l33.append(in_date)

            x5="2017"+MM[l22[0][2:]]+l22[0][:2]

            l33.append(x5)
            l33.append(fl_no)
            l33=l33+l22[1:5]
            for i in l22[5:]:
                if i == "Q" or i == "E" or i=="S":
                    i = " "
                elif i=="A":
                    i="9"
                l33.append(i)
            l44 = [','.join(l33)]
            output.writelines(l44)
            output.writelines('\n')
            #print li
        #print lis2
    lines.close()
    output.close()



   # for line in mylines1:

#    for line in mylines1:
#        print line
#    for line in mylines1:
#        output.write(line)
#        output.write(" ")
#    output.write(sList)
in_date = "2017/01/05"
fname = "2623AVJ测试.txt"
path="C:\Users\mingl\Desktop\测试处理数据"
path1 = os.path.join(path,fname)
#filepath1=unicode(filepath , "utf8")
path2=r"C:\Users\mingl\Desktop\测试处理数据\out_2623AVJ测试.txt"
#filepath2=unicode(path2,"utf8")
P_AVJ(path1,path2,in_date)
