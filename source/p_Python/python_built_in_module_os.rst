=============================
Python内置模块：os
=============================

os.listdir
os.walk
os.path

模块大概分类
常用的内置模块
import os
import sys
import glob
import json
import yaml
import shutil
import re 正则表达式
import time
import datetime
import platform
import random
import subprocess
import xml.etree.ElementTree as ET
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

内置模块
DCC软件自带模块
第三方模块
自定义模块

Python模块搜索路径
当前工作路径 + sys.path

os
os.path
os.listdir
os.walk
os.environ


os.path module

import os

path = "C:/Users/huweiguo/Documents/maya/2018/maya.env"
os.path.basename(path)
os.path.dirname(path)
os.path.join("tmp", "data", os.path.basename(path))
path = "~/maya/2018/maya.env"
os.path.expanduser(path)
os.path.splitext(path)

尽可能使用os.path来操作文件路径的问题，最好不要使用字符串来构造自己的代码，主要是为了代码的可移植性，它可以很好的处理linux、mac以及windows文件路径的差异

.. code-block:: python

    #!/usr/bin/env python3.7
    import os

    def findFile(start, name):
        for relpath, dirs, files in os.walk(start):
            if name in files:
                fullPath = os.path.join(start, relpath, name)
                print(os.path.normpath(os.path.abspath(fullPath)))

    if __name__ == "__main__":
        findFile(sys.argv[1], sys.argv[2])

从文件夹中查找文件

.. code-block:: python

    with open("somefile", "wt") as f:
        f.write("Hello\n")

    with open("somefile", "xt") as f:
        f.write("Hello\n")

    import os
    if not os.path.exists("somefile"):
        with open("somefile", "wt") as f:
            f.write("Hello\n")
    else:
        print("File already exist!")

.. code-block:: python

    import os
    houVersion = "17.0"
    version = 2

    ###### Do not do this !!!!! ######
    # filepath = "C:\Users\huweiguo\Documents\houdini" + houVersion + "\tmp" + "\example_v0" + str(version) + ".py"
    # filepath = os.path.join("C:\Users\huweiguo\Documents\houdini", houVersion, "tmp", "example", str(version), ".py")
    ##################################
    # print(filepath)
    #
    # filepath = os.path.expanduser("~/Documents/houdini{0}/tmp/example_v{1:02}.py".format(houVersion, version))
    # filepath = os.path.normpath(filepath)
    # print(filepath)
    # print("This is a file ? :", os.path.isfile(filepath))
    # print("This is a directory ? :", os.path.isdir(r"c:\temp"))
    #
    #
    # tempFolder = 'temp_2'
    # cacheType = 'bgeo'
    # cacheName = 'waterSplash.bgeo.gz'
    # filepath = os.path.join(r"C:\nrojects/bla", tempFolder, cacheType, cacheName)
    # print(filepath)
    # print(os.path.normpath(filepath))

    # print(os.path.split(filepath))

    # print(os.path.dirname(filepath))

    # print(os.path.basename(filepath))

    #### PATH SEPARATOR #####
    HOUDINI_OTLSCAN_PATH = os.pathsep.join([os.path.expanduser('~/houdini12.1/otls'),
                                        '/houdini_install/houdini/otls',
                                        '/mnt/repo/houdini/otls',
                                        '/mnt/projects/xyzproject/otls'])
    print HOUDINI_OTLSCAN_PATH

    # t = "D:/Program"
    # l = []
    # print(os.listdir(t))

    # for f in os.listdir(t):
    #     l.append(os.path.normpath(os.path.join(t, f)))

    # print l


python中默认编码是unicode
s1.decode(“gb2312”) 将gb2312编码的字符串转换成unicode
s2.encode(“gb2312”) 将unicode编码的字符串转换成gp2312

from urllib.request import urlopen
# 正常网页是utf-8，所以要转unicode
import json
u = urlopen(网址)
resp = json.loads(u.read().decode("utf-8"))
from pprint import pprint
pprint(resp)

.. code-block:: python

    import os
    import sys
    import shutil
    import random
    import datetime
    import module as xxx
    from module import xxx as xx
    os.listdir()
    os.getcwd()
    os.mkdir()
    os.makedirs()
    r"\\\"自然字符串
    os.remove()
    os.rmdir()
    os.path模块功能操作文件夹
    os.path.isdir()
    os.path.isfile()
    os.path.split()
    os.path.splitext()
    os.path.splitdrive()
    os.path.join()
    os.path.normpath()
