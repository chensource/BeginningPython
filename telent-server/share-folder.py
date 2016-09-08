#! /usr/bin/env python
# -*- coding: utf-8 -*-
#@author zcwang3@gmail.com
#@version 2010-09-25 14:57

import os
import time

sourceDir = r"\\10.4.18.107\webroot\CentaNet.Admin"
bakDir = r'\\10.4.18.107\webroot\bak\WebAdmin_bak'
targetDir = r"D:\test"
city = ['bj', 'tj', 'cd', 'nj', 'cq', 'wh', 'dg', 'hz']
copyFileCounts = 0


def copyFiles(sourceDir, targetDir):
    global copyFileCounts
    print(u"%s 当前处理文件夹%s已处理%s 个文件" %
          (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
           sourceDir, copyFileCounts))
    for f in os.listdir(sourceDir):
        sourceF = os.path.join(sourceDir, f)
        targetF = os.path.join(targetDir, f)

        if os.path.isfile(sourceF):
            #创建目录
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)
            copyFileCounts += 1

            #文件不存在，或者存在但是大小不同，覆盖
            if not os.path.exists(targetF) or (os.path.exists(targetF) and (
                    os.path.getsize(targetF) != os.path.getsize(sourceF))):
                #2进制文件
                open(targetF, "wb").write(open(sourceF, "rb").read())
                print(u"%s %s 复制完毕" %
                      (time.strftime('%Y-%m-%d %H:%M:%S',
                                     time.localtime(time.time())), targetF))
            else:
                print(u"%s %s 已存在，不重复复制" %
                      (time.strftime('%Y-%m-%d %H:%M:%S',
                                     time.localtime(time.time())), targetF))

        if os.path.isdir(sourceF):
            copyFiles(sourceF, targetF)


import sys
import subprocess


def copyWithSubprocess(sourceDir, targetDir):
    platform = sys.platform
    if platform.startswith("win"):
        # sourceF = os.path.join(sourceDir, f)
        # print(sourceF)
        # targetF = os.path.join(targetDir, f)
        print(sourceDir)
        print(targetDir)
        cmd = 'xcopy %s %s /s /e' % (sourceDir, targetDir)
        print(cmd)
        subprocess.call(cmd)
        print(u"%s %s 复制完毕" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), targetF))

if __name__ == "__main__":
    copyWithSubprocess(
        sourceDir,
        bakDir + '\\' + time.strftime('%Y%m%d', time.localtime(time.time())))
# try:
#     import psyco
#     psyco.profile()
# except ImportError:
#     pass
# copyFiles(
#     sourceDir,
#     bakDir + '\\' + time.strftime('%Y%m%d', time.localtime(time.time())))
