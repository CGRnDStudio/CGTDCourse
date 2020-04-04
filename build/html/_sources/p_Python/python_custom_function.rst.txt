=============================
Python自定义函数
=============================

函数是Python内建的一种封装，我们把大段代码拆成函数，通过一层一层的函数调用，就可以把复杂的任务分解成简单的任务，这种分解称为面向过程的程序设计。函数就是面向过程的程序设计的基本单元。Python提供了很多内置函数，比如print()，你也可以自己创建函数，这被叫做自定义函数。

------------------
函数的几个概念
------------------

* 基本语法

.. code-block:: python

    def 函数名(形式参数):
        函数体
        return 返回值

形式参数和返回值不是必须的，但函数都是有返回值的，如果没有使用关键字return返回值，则函数默认返回None。

* 形式参数(形参)

* 实际参数(实参)

* 返回值


------------------
形参的几种形式
------------------

* 缺省参数，又叫默认参数

* 可变参数 ``*args`` 

``*args``表示可变参数，就是传入的参数个数是可变的，可以是1个，2个到任意个或者0个。其实就是将传入的一堆参数打包成元组使用。

* 关键字参数 ``**kwargs``

``**kwargs``将传入的0个或者多个含参数名的参数打包成字典使用。

* 不同形式参数之间组合

------------------
作用域
------------------

在函数外部，locals()和globals()作用完全相同。而当在函数内部调用时，locals()则是获取当前函数堆栈中的名字空间，其中存储的时函数参数、局部变量等信息。

.. code-block:: python

    >>> locals()
    {'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
    >>> globals()
    {'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
    >>> locals() is globals()
    True
    >>> def func(a):
    ...     b = a % 2
    ...     print(locals())
    ...     print(locals() is globals())
    ...
    >>> func(5)
    {'a': 5, 'b': 1}
    False
    >>> locals() is globals()
    True

.. code-block:: python

    def f(arg1, arg2, arg3):
        print(arg1, arg2, arg3)
        
    def f(*args):
        print(type(args))
        print(args)
        
    f(3, 2, 1)

    def f(**kwargs):
        print(type(kwargs))
        print(kwargs)
        
    f(name="Andy", lang="Chinese")

    def f(*args, **kwargs):
        print(args)
        print(kwargs.items())

    f(1, 2, name="Andy", lang="Chinese")

    def setParms(**kwargs):

        for k,v in kwargs.items():
            print("Setting parameter {0} to {1}".format(k,v))
            
    setParms(streng=13, resistance=0.7, weigh=100)

    return

    def double_parm(**kwargs):
        return kwargs["weigh"] * 2

    print(double_parm(streng=13, resistance=0.7, weigh=100))

函数赋值

.. code-block:: python

    def double_parm(**kwargs):
        return kwargs["weigh"] * 2, kwargs["streng"]

    new_func = double_parm

    print(new_func(streng=13, resistance=0.7, weigh=100))

函数中套函数

.. code-block:: python

    def double_parm(**kwargs):
        
        def check(weight):
            if weight < 100:
                return False
            else:
                return True

        if check(kwargs["weigh"]):
            return kwargs["weigh"] * 2, kwargs["streng"] * 2
        else:
            return kwargs["weigh"] * 2, kwargs["streng"] * 4

    new_func = double_parm

    print(new_func(streng=13, resistance=0.7, weigh=60))

    import os
    from sys import version

    PATH = "/tmp/folder/name"


    # def localFunc():
    #     global version
    #     version = 13.3
    #     print("Local version", version)

    # localFunc()
    # print(version)


    # def getTempContent():
    #     tempdir = os.listdir("C:/")

    # getTempContent()
    # print(tempdir)


    def func1():
        print(mvar)
        print(PATH)


    def funcBase():
        mvar = 15
        func1()

    funcBase()

正则表达式

.. code-block:: python

    ### Various Sorting methods for lists and dicts
    import re
    import random
    import calendar
    from pprint import pprint
    files = ['tank_1_color_v0.rat',
            'tank_2_color_v5.rat',
            'tank_1_color_v3.rat',
            'tank_3_color_v1.rat',
            'tank_4_color_v2.rat',
            'tank_4_color_v4.rat',
            'tank_5_color_v1.rat',
            'tank_6_color_v6.rat']

    pat_num = re.compile('\D+_(\d+)_')
    pat_ver = re.compile('(\d+)\D+$')

    def sorter_num(elem):
        res = re.search(pat_num, elem)
        return res.groups()[0]

    def sorter_ver(elem):
        res = re.search(pat_ver, elem)
        return res.groups()[0]

    # pprint(sorted(files, key=sorter_num))
    # pprint(sorted(files, key=sorter_ver))

    s2 = "February January  May October August September April  November July March December"

    d = {}
    for i in range(1, 13):
        d[calendar.month_name[i]] = i
    def sorter(elem):
        return d[elem]
    # month_names = sorted(s2.split(), key=sorter)

    month_names = [calendar.month_name[i] for i in range(1, 13)]

    pprint(sorted(s2.split(), key=month_names.index))

处理路径

.. code-block:: python

    import os
    houVersion = '12.1'
    version = 2

    ###### Do not do this !!!!! #####
    filepath = "c:\Users\alex\Documents\houdini" + houVersion + "\tmp" + "\example_v0" + str(version) + ".py"
    filepath = os.path.join("c:\Users\\alex\Documents\houdini", houVersion, "tmp", "example", str(version), ".py")
    ####################################
    # print filepath
    #
    #
    filepath = os.path.expanduser('~/Documents/houdini{0}/tmp/example_v{1:02}.py'.format(houVersion, version))
    filepath = os.path.normpath(filepath)
    # print filepath
    # print 'This is a file ? :', os.path.isfile(filepath)
    # print 'This is a directory ? :', os.path.isdir(r"c:\temp")
    #
    #
    # tempFolder = 'temp_2'
    # cacheType = 'bgeo'
    # cacheName = 'waterSplash.bgeo.gz'
    # filepath = os.path.join(r"c:\nrojects//bla", tempFolder, cacheType, cacheName)
    # print filepath
    # print os.path.normpath(filepath)
    #####
    #
    ######
    # print os.path.split(filepath)
    #
    ######
    # print os.path.dirname(filepath)
    #
    #####
    # print os.path.basename(filepath)

    #### PATH SEPARATOR #####
    HOUDINI_OTLSCAN_PATH = os.pathsep.join([os.path.expanduser('~/houdini12.1/otls'),
                                        '/houdini_install/houdini/otls',
                                        '/mnt/repo/houdini/otls',
                                        '/mnt/projects/xyzproject/otls'])
    # print HOUDINI_OTLSCAN_PATH
    #
    #
    t = r'c:\temp'
    l = []
    #
    for f in os.listdir(t):
        l.append(os.path.normpath(os.path.join(t, f)))

    print l

形式参数
实际参数

默认值（缺省值）对函数重载的作用

len多态函数
len(“andy”)
len(range(10))
+运算符 多态性
100 + 200
“hello ” + “python”

Python函数没有重载的概念主要是因为动态语言特性以及缺省值

*args 如何打包参数
**kwargs 如何打包参数

复用性
可扩展性

def function(args):
    code
    return

def foo():
    print(“this is function”)

foo()

# 形式参数
def sayHello(name):
    print(“hello, ”, name)

sayHello(“andy”)

# 缺省参数

def sayHello(name=”andy”):
    print(“hello, ”, name)

sayHello()

# 形式参数>缺省参数>*args>**kwargs
# 可变参数
def sayHello(*names):
    print(names)

sayHello(“andy”, “tommy”)

# 顺序传参，关键字传参
def foo(a, b, c):
    print(“a is ”, a)
    print(“b is ”, b)
    print(“c is ”, c)

foo(1, 2, 3)
foo(a=1, b=2, c=3)
foo(b=2, c=3, a=1)
foo(1, c=3, b=2)

def sayHello(**names):
    print(names, type(names))

sayHello(name=”andy”, age=30)

def foo(a, b=1, *args, **kwargs):
    pass

# 返回值
def foo():
    return 5

a = foo()
print(a)

def foo(a):
    if a < 0:
        return
    return 100 + a

foo(9)
foo(-9)


作用域
内建作用域
全局作用域
闭包函数外的函数中
局部作用域

b = 5

def foo():
    global b
    b = 1
    print(b)


# 递归函数

def factorial(number):
    if not isinstance(number, int) or number <= 0:
        return
    result = 1
    for n in range(1, number + 1)
        result *= n
    return result

factorial(100)

def fact(number):
    if number == 1:
        return number
    return number * fact(number - 1)


# os.walk()
import os
from pprint import pprint

def walkFolders(folderPath):
    subFileList = []
    for subFileName in os.listdir(folderPath):
        subPath = os.path.join(folderPath, subFileName)
        if os.path.isfile(subPath):
            subFile = {“type”: “file”, “name”: subFileName}
            subFileList.append(subFile)
        else:
            subFolder = {“type”: “folder”, “name”: subFileName, “subFiles”: walkFolders(subPath)}
            subFileList.append(subFolder)
    return subFileList


闭包函数
闭包函数指的是在函数内定义的内部函数
