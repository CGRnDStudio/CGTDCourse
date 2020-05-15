=============================
Python文件操作
=============================

Python文件操作实际就是内存数据与硬盘文件数据IO的一个过程，Python提供基础的内置函数以及所谓的上下文管理器来读写文件，也提供了很多第三方库来操作文件解析文件。

* 内置函数open

通过open()读写文件一要注意获取的文件对象需要最后通过close()方法关闭，以释放内存空间，二要注意编码转换的问题，py3添加了编码的支持。

.. code-block:: python

    # py2
    open(name[,mode[,buffering]])

    # py3
    open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

.. code-block:: python

    f = open("somefile.txt", "rt")
    print(f)
    data = f.read()
    print(data)
    f.close()

* 上下文管理器

上下文管理协议为代码块提供了包含初始化和清理操作的安全上下文环境。即便代码块发生异常，清理操作也会被执行。

通过关键字with即可简单实现上下文管理器，上下文管理器with在语句块结束之后，文件会自动关闭，无需再编写close()方法，因此更推荐使用with open的写法。

.. code-block:: python

    with open("somefile.txt", "rt") as f:
        data = f.read()

    with open("somefile.txt", "rt") as f:
        for line in f:
            pass

    with open("somefile.txt", "wt") as f:
        f.write(text1)
        f.write(text2)

    with open("somefile.txt", "wt") as f:
        print(line1, file=f)
        print(line2, file=f)

.. code-block:: python

    with open("somefile.txt", "rt", encoding="gb2312") as f:
        pass

* 文件读写模式

rb

wt

* 文件对象的方法

read()

readlines()

write()

* 第三方库

.. code-block:: python

    import os
    import shutil
    import json
    import yaml

os模块是python与计算机操作系统交互的模块，它提供了一系列访问操作系统的相关功能。

.. code-block:: python

    import os
    # 当前路径
    os.getcwd()
    os.mkdir()
    os.listdir(os.getcwd())
    # os.chdir VS os.getcwd
    os.chdir()
    os.rmdir()
    os.makedirs()
    os.rename()
    os.removedirs()
    os.path.join()
    os.path.exists()
    os.path.dirname()
    os.path.split()
    os.path.splitext()
    os.path.splitdriver()
    os.path.isdir()
    os.path.isfile()

shutil模块是python内置的一个高级文件操作模块，提供了一些针对文件操作和文件采集相关的高级功能。在os模块相关功能基础上进行了升级，形成了一系列专门为文件操作而设计的功能集合。

.. code-block:: python

    import shutil
    filePath = "D:/test"
    newFilePath = "D:/test_new"
    # copy函数将一个文件拷贝到另一个路径下
    shutil.copy(filePath, newFilePath)
    # copy2函数除了拷贝文件外，还会将源文件的权限，最后访问时间，最后修改时间等拷贝到目标文件上
    newFilePath2 = "D:/test_new2"
    shutil.copy2(filePath, newFilePath2)
    shutil.move()
    shutil.rmtree()


json模块是用来解析字典容器与文件数据之间的模块，用来编写.json配置文件非常方便以容易处理。

load

dump

loads

dumps

yaml

xml
