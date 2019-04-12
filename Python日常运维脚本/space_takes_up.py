#!usr/bin/env python
#-*- coding:utf-8 _*-

"""
@author:T-guoh
@file: server_monitor.py
@time: 2019/03/18
"""

import os

#统计指定目录下各个文件夹的大小，方便观察具体目录的大小
def CountDirSize(srcDir):
    dirSizeDict = {}
    fileSizeDict = {}
    for fileList in os.listdir(srcDir):
        filePath = os.path.join(srcDir,fileList)
        if os.path.isdir(filePath):
            size = 0
            for roots,dirs,files in os.walk(filePath):
                for fileName in files:
                    fileNamePath = os.path.join(roots,fileName)
                    sizetemp = 0
                    try:
                        sizetemp = os.path.getsize(fileNamePath)
                        if sizetemp > 1024*1024:
                            fileSizeDict[fileNamePath] = sizetemp
                    except:
                        sizetemp = 0
                    size += sizetemp
            dirSizeDict[fileList] = size
    #按照从大到小的顺序降序排列
    dirSizeDict = sorted(dirSizeDict.items(),key = lambda dirSizeDict:dirSizeDict[1],reverse = True)
    Sum = 0
	#各个目录占用空间
    print("Each directory takes up space:")
    for ele in dirSizeDict:
        temp = ele[1]/1024/1024
        Sum += temp
        #以单位为M，输出大小
        print(ele[0] + ":" + str(temp) + " M")
    #以单位为G，输出大小
    print("Total use:" + str(Sum / 1024) +" G")
    print("")
    #前20个大文件占用空间
    print("Top 20 large file takes up space:")
    fileSizeDict = sorted(fileSizeDict.items(),key = lambda fileSizeDict:fileSizeDict[1],reverse = True)
    for ele in fileSizeDict[:20]:
        print(ele[0] + ":" +str(ele[1]/1024/1024) + " M")

if __name__ == "__main__":
    srcDir = "c:\\"
    CountDirSize(srcDir)