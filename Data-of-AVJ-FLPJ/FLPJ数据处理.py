# -*- coding: utf-8 -*-
# 中文注释需要包含以上内容
import os
import re

def P_FLPJ(filepath_in,filepath_out,in_date):
    if not isinstance(filepath_in, unicode):
        filepath_in = unicode(filepath_in, "utf8")
    if not isinstance(filepath_out, unicode):
        filepath_out = unicode(filepath_out, "utf8")

    fl_no=os.path.basename(filepath_in)[:4]
    mylines1 = []
    lines = open(filepath_in, 'r')
    output = open(filepath_out, 'w')

    lines1=[]
    for line in lines:
        if line.startswith("FLIGHT  TOTAL"):
            break
        if line.startswith(" ", 40, 50):
            nothing=0
        else:
            if line.startswith(" ", 18, 20):
                llll=line[39:].rstrip()
                if llll.endswith("+"):
                    llll=llll[:-1]
                lines1.append(llll.rstrip())
                # lines1.append(line[39:].rstrip())
                #print line[40:]
            else:
                lines1.append(line.rstrip())
                #print line


    sList = ''
    lines2=[]
    for line in lines1:
        sList=sList+line
        if line.endswith("//"):
            # print sList
            lines2.append(sList)
            # output.writelines(sList)
            # output.writelines("\n")
            sList = ''

    lines3=[]
    for line in lines2:
        if line.startswith(" "):
            if line.startswith(" ",15):
                line = lline+line[17:]
            else:
                line = sline+line[13:]
        else:
            lline=line[:17]
            sline=line[:13]
        lines3.append(line)
        # print line

    # p2 = r"(\d{1,2}\w{3}\d{2} \w{6} \d{4}   \d{4}   CR9 \d   )F(\w )A(\w )D(\w )Y(\w )T(\w )H(\w )M(\w )G(\w )S(\w )L(\w )Q(\w )E(\w )V(\w )R(\w )O(\w )U(\w )Z(\w )X(\w )P(\w )K(\w )B(\w )I(\w )J(\w )W(\w )N(\w)"
    p2 = r"(\d{1,2}\w{3})/\d CR9  (\w{3} )(\w{3}..).{16}/F(\w+)/A(\w+)/D(\w+)/Y(\w+)/T(\w+)/H(\w+)/M(\w+)/G(\w+)/S(\w+)/L(\w+)/Q(\w+)/E(\w+)/V(\w+)/R(\w+)/O(\w+)/U(\w+)/Z(\w+)/X(\w+)/P(\w+)/K(\w+)/B(\w+)/I(\w+)/J(\w+)/W(\w+)/N(\w+)//"
    # output.writelines('日期  出发 到达  F A D Y T H M G S L Q E V R O U Z X P K B I J W N \n')

    MM = dict()
    MM = {'JAN': '/01/', 'FEB': '/02/', 'MAR': '/03/', 'APR': '/04/', 'MAY': '/05/', 'JUN': '/06/', 'JUL': '/07/',
          'AUG': '/08/', 'SEP': '/09/', 'OCT': '/10/', 'NOV': '/11/', 'DEC': '12'}

    for line in lines3:
        lis2 = re.findall(p2, line)
        for li in lis2:

            l22 = list(li)
            l33 = []
            l33.append(in_date)
            x5 = "2017" + MM[l22[0][2:]] + l22[0][:2]
            l33.append(x5)
            l33.append(fl_no)
            l33 = l33 + l22[1:3]
            for i in l22[3:]:
                if i == "0":
                    i = " "
                l33.append(i)
            l44 = [','.join(l33)]
            output.writelines(l44)
            output.writelines('\n')
            # print l33
        # print lis2

    lines.close()
    output.close()


in_date = "2017/01/05"
fname = "2607FLPJ测试.txt"
path="C:\Users\mingl\Desktop\测试处理数据"
path1 = os.path.join(path,fname)
#filepath1=unicode(filepath , "utf8")

path2=r"C:\Users\mingl\Desktop\测试处理数据\out_2607FLPJ测试.txt"
#filepath2=unicode(path2,"utf8")
P_FLPJ(path1,path2,in_date)