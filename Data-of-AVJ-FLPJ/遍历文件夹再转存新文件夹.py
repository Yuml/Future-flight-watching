# -*- coding: utf-8 -*-
# 中文注释需要包含以上内容

#输入、输出都需要对中文字符进行处理
import os
import re


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
        # print child.decode('gbk') # .decode('gbk')是解决中文显示乱码问题
    for allDir in F_file:
        child = os.path.join(F_Dir, allDir)
        F_filedir1.append(child.decode('gbk'))
        # print child.decode('gbk')  # .decode('gbk')是解决中文显示乱码问题

    return (A_filedir1,F_filedir1)

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

def All_P(A_filedir,F_filedir,out_path,in_date):
    out_path_A = unicode(os.path.join(out_path,"out_AVJ"), "utf8")
    if not os.path.exists(out_path_A):
        os.mkdir(out_path_A)
    for filedir in A_filedir:
        out_dir=os.path.join(out_path_A,"out_"+os.path.basename(filedir))
        P_AVJ(filedir, out_dir,in_date)

    out_path_F = unicode(os.path.join(out_path, "out_FLPJ"), "utf8")
    if not os.path.exists(out_path_F):
        os.mkdir(out_path_F)
    for filedir in F_filedir:
        out_dir = os.path.join(out_path_F, "out_" + os.path.basename(filedir))
        P_FLPJ(filedir, out_dir,in_date)


# new_dir=unicode(r"C:\Users\mingl\Desktop\测试处理数据\test采集7-17", "utf8")
# os.mkdir(new_dir)
Data_dir = raw_input("输入要处理文件夹的地址：")
in_date = raw_input("输入采集日期  YYYY/MM/DD：")
(A_filedir,F_filedir)=eachFile(Data_dir)

All_P(A_filedir,F_filedir,Data_dir,in_date)

