=============================
Python开发环境
=============================

解决两个问题
CG软件中在哪里可以执行代码?
学习print()函数
独立环境如何执行代码?

❏独立执行环境
❏DCC软件中的执行环境
❏IDE中的执行环境
❏print函数
❏关键字
❏转义字符
❏注释

❏VS Code安装、配置以及使用 下载地址： https://code.visualstudio.com/
❏Python 2.7.15安装 下载地址： https://www.python.org/downloads/
❏Git管理代码库 Git下载地址： https://git-scm.com/downloads
❏TortoiseGit 下载地址： https://tortoisegit.org/
❏掌握Markdown语法撰写文档
❏Git Bash结合ipython使用 ipython安装： pip install ipython pip install PySide
❏Python第三方库路径 C:\Python27\Lib\site-packages

Markdown语法
Linux操作指令
VS Code高级使用技巧
PEP8规范
Git指令
ipython高级使用技巧

TD日常工作内容
❏撰写流程规范、软件工具说明文档等
❏根据需求开发相应的软件工具或插件
❏检查并修正生产过程中出现的错误文件
❏维护公共服务系统，如渲染农场、存储设备、公共服务器等
❏向软件工具或插件的使用者演示其功能及操作方式
❏管理和维护生产素材、制作文件、输出序列、生产元数据

TD日常工作流程
选择集成开发环境（IDE）
❏VS Code轻量跨平台免费
❏VS Code基本配置以及用途
❏VS Code Python开发环境
❏VS Code调试以及断点调试 print是最简单的一种debug方法
❏VS Code实用快捷键

Ctrl+F2：批量选择相同字段并修改
Ctrl+D：逐一加选相同字段并修改
Alt+Z：自动换行查看
Ctrl+/：注释与反注释
Tab：
Shift+Tab：
Alt+Shift+左键：列模式编辑
Ctrl+H：替换
Ctrl+F：查找
F5：Debug
Ctrl+Shift+方向键：复制代码

PEP8代码规范
- 安装

https://pypi.org/project/pep8/

pip install pep8

pip install --upgrade pep8
- 向导

https://www.python.org/dev/peps/pep-0008/

.. code-block:: python

    #!/usr/bin/python
    # -*- coding: utf-8 -*-

    """ 写个简单统计运行时间的函数
    """

    import time

    def measure_time(func):

        def wrapped(*args, **kwargs):
            start = time.time()
            
            try:
                return func(*args, **kwargs)
            finally:
                runtime = time.time() - start
                print("Execution time: %.6f seconds" % runtime)
                
        return wrapped

    @measure_time
    def f(n):
        l = []
        for i in range(n):
            l.append(i)

    if __name__ == "__main__":
        f(1000000)

其他IDE简单介绍
VS Code
Eclipse
PyCharm
Atom
...

文本编辑器
Vim
Emacs
Sublime
Notepad++
....

管理自己的代码
- Git & TortoiseGit
- Github & Gitlab
- Gitlab创建私有代码仓库
- Gitlab Release版本
- Git最常用的操作指令

.. code-block:: python

    git clone URL
    git config --global user.name "Your Name"
    git config --global user.email "Your Email"
    git status
    gitk
    git add .
    git commit -m "Your Comment" -a
    git push origin master
    git pull origin master


- TortoiseGit界面化提交代码
- Github拉取代码并使用
- 反编译pyc文件 Easy Python Decompiler
- IPython & Gitbash

.. code-block:: bash

    # 更新pip
    python -m pip install --upgrade pip 
    # 安装ipython
    pip install ipython
    pip install *.whl

import this
import antigravity
dir(__builtin__)

解决一个中心问题：在哪里可以执行Python代码? 认识第一句代码，内置函数print?

Python 2.7 VS Python 3.7
https://www.liaoxuefeng.com/
Google文档
https://www.python.org/
https://docs.python.org/zh-cn/3.9/

python -V
pip安装第三方模块

pip install ipython
Path环境变量

Anaconda https://www.anaconda.com/distribution/#download-section
jupyter notebook
IPython
help()
cls

.. code-block:: python

    a = 100
    if isinstance(a, int):
        print("a is int")
    else:
        print("a is not int")

    help(isinstance)
    help(list)

    for i in range(1, 11):
        print(i)

    array = list()

    for i in range(1, 11):
        array.append(i)

    print(array)

列表生成式
array = [i for i in range(1, 11)]

range(1, 100, 2)
range(1, 100)[::2]
[i for i in range(1, 100) if i % 2 != 0]
[i for i in range(1, 100) if i % 2 != 0 and i < 50]

range(50, 10, -1)

help(map)

help(filter)

%ls
%cd D:
?
map?
exit

jupyter notebook

array = [i for i in range(1, 11) if i % 2 == 0 or i == 1]

def getList(min, max, step):
    return [i for i in range(min, max, step)]

getList(1, 100, 5)

https://docs.python.org/zh-cn/3.9/

入门教程
标准库参考
语言参考

# 注释
    缩进

a = u"ccccc"
b = "10"
c = """
This is a three single quote
This is a string %s : %s
""" % (a, b)

c = """
This is a three single quote
This is a string {0} : {0}
""".format(a, b)

print(type(a))
print(type(b))
print(c)

d = 1000
e = 3.14159
f = 0x400
g = 3.14e-2
print(d, e, f, g)

a = 1000L
print(type(a))

print(oct(100))
print(hex(100))
print(bin(100))
print(0.1234)
print(.1234)
print(3.14e-8)

mySet = {1, 2, 3, 4, 3, 3, 3, 1}
mySet.add(10)
mySet.add(1)
mySet = frozenset(mySet)
print(mySet)

生成器
(i for i in range(1, 10))

a = 99
b = 77
print(~a + 1)
print(~b + 1)

a = 2

print(a << 2)
print(a << 3)
print(bin(a << 1))
print(bin(a << 2))
print(bin(a << 3))



cmd执行代码
debug代码

Git
TortoiseGit

解决一个中心问题：如何存储自己编写的代码?

IPython
VS Code
Vim
notepad++
Sublime Text
PyCharm

Python执行环境
Python IDE(集成开发环境)

注释 # 

hello.py
hou.py

可以写代码的软件
VS Code

= 赋值
== 等于 ----->真假事件 

if 真假事件:
    do something
else:
    do something

自动补全

代码健壮性

量到质变
代码量 记忆碎片 内功心法
条件反射


解决一个中心问题：如何区分Python和VEX? Python代码有哪些明显的特征?

PEP8
Google
二进制
计算机编码
简单涉及一下基本数据类型

Python执行环境
Python IDE
Python基本数据类型 (Pythond语法规则或者代码规范)  PEP8代码规范 Google代码规范

Python VS VEX

语句块
Python有冒号，VEX没有冒号
VEX有分号 Python没有
Python import module

基本数据类型(五大类)
整型 int
浮点型 float
布尔值 bool  True&False 1&0 二进制 01010100 计算机编码(硬件环境) 0-9 二极管 电压高电压低 8位二进制==一个字节 16位二进制==2个字节 unicode?
字符串 string
None 假的事件 函数返回值默认是None
bool函数
id()

0-0
1-1
2-10
3-11
4-100
5-101
6-110
7-111
8-1000
9-1001
10-1010

八进制跟十六进制
0

8GB 1TB 8GB = 8*1024MB = 8*1024*1024KB = 8*1024*1024*1024字节 =8*1024*1024*1024*8二进制


注释
#
# TODO
docstring
如何写help帮助文档
Ctrl+/ 注释 反注释
Tab 代码缩进
多行注释
"""
"""
