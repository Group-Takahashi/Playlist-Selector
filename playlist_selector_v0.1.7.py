#内置库
import csv
# import sqlite3
import time
import random

#文件读取
print("""
====================================================
                Playlist Selector     
                                    v0.1.7
====================================================
Powered by Python3.

Written by TakahashiHaruki.
Requested by SHDocter.
2021/06/25.
====================================================
P.S. 狗日落下次自己写！！！    (╯°口°)╯(┴—┴
====================================================

OPTIONS：
请将csv文件复制到本脚本所在目录下，并确认以下内容：
1.文件名为playlist.csv
2.列2为歌名，列3为演唱者，列4为来源，列5为点歌人

确认后按Enter继续，若不正确请关闭窗体。

====================================================
""")


input("按Enter以继续...")


with open(r'.\playlist.csv', encoding='UTF-8', errors='ignore') as csvfile:
    reader = csv.reader(csvfile)
    muusicId = [row[0] for row in reader]    #抽取列
    csvfile.seek(0)                          #将文件查找并回0
    musicName = [row[1] for row in reader]
    csvfile.seek(0)
    artistName = [row[2] for row in reader]
    csvfile.seek(0)
    platformName = [row[3] for row in reader]
    csvfile.seek(0)
    viewerName = [row[4] for row in reader]

    time.sleep(0.2)

resultNum = []
startNum = 0
endNum = len(musicName)
numQuantity = int(input("请输入抽取歌曲数目:"))

resultNum = random.sample(range(startNum,endNum+1),numQuantity)

artistChoice = input("是否需要打印演唱者(Y/n, default with Y):")
platformChoice = input("是否需要打印点歌平台来源(Y/n, default with Y):")
viewerChoice = input("是否需要打印点歌观众昵称(Y/n, default with Y):")
idChoice = input("是否需要打印编号(Y/n, default with Y):")

print("""
====================================================
                    抽取结果
====================================================""")
for resultOutput in range(numQuantity):
    print("曲名:" + musicName[resultNum[resultOutput]])
    if artistChoice != "n":
        print("演唱者:" + artistName[resultNum[resultOutput]])
    if platformChoice != "n":
        print("点歌平台来源:" + platformName[resultNum[resultOutput]])
    if viewerChoice != "n":
        print("点歌观众昵称:"+viewerName[resultNum[resultOutput]])
    if idChoice != "n":
        print("编号:"+muusicId[resultNum[resultOutput]])
    print("====================================================")

delRequest = "n"

delRequest = input("是否需要从csv文件中删除已抽出的列并生成新文件(Y/n, default with n):")

if delRequest == "Y":
    print("""
====================================================
您已选择从csv文件中删除已抽出的列并生成新文件，五秒后开始执行...
(如需要打断请按\"Ctrl+C\")
====================================================""")
    time.sleep(5)
    print("开始执行操作...")
    time.sleep(1)
    print("还没写完，存个寂寞自己手动删！(╬ﾟдﾟ)▄︻┻┳═一")
    lineId =  []
    for i in range(numQuantity):
        lineId.append(muusicId[resultNum[i]])
    print("需要删除的行号为:"+str(lineId))
    input("按Enter退出程序...")
else:
    input("按Enter退出程序...")

