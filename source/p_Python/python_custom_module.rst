=============================
Python自定义模块
=============================

- 几种常见的模块导入方式
- 模块导入的搜索机制sys.path
- 缓存区sys.modules、pyc以及reload
- 查询模块路径__file__
- 模块中__name__的作用
- 模块帮助文档docstring（__doc__）


几种常见的模块导入方式

Python允许开发者通过导入外部程序块的方式来扩展自己的程序，这些可以被导入（import）并使用的程序块就是模块（module）

模块的基本单元是一个.py文件，Python的包在广义上也被称为模块（module）

以内置模块datetime为例

.. code-block:: python

    import datetime
    import datetime as dt
    print(dt.datetime.now())
    from datetime import datetime
    print(datetime.now())
    from datetime import *
    from datetime import datetime as ddt
    print(ddt.now())

模块导入的搜索机制sys.path，模块导入搜索路径是由多个目录路径组成的列表，第一个路径默认是当前模块所在的路径，模块搜索路径 = 当前工作路径 + sys.path列表内的所有路径。

- 何为环境变量PYTHONPATH?
- sys.path在环境变量中起什么作用?
- sys.path添加路径的两种方案以及区别?
- DCC软件如何管理sys.path?

.. code-block:: python

    import sys

    path in sys.path or sys.path.insert(0, path)

- 缓存区sys.modules、pyc以及reload
- import可以是属性方法类型，reload只能是模块
- 查询模块路径__file__

__file__属性是一个Python模块隐藏的默认属性，它描述了一个模块的完整路径。

- 模块中__name__的作用

__name__属性是所有Python模块自带的一个隐藏属性，用于标注模块在不同执行环境下的名称。当一个模块作为主模块运行（被Python解释器直接运行）时，__name__的值是"__main__"，否则，该模块的__name__属性值为此模块的名称。

- 模块帮助文档docstring（__doc__）

双三引号，docstring写在什么位置? help()内置函数与docstring的关系?

myFirstModule.py

.. code-block:: python 

    # -*- coding: utf-8 -*-
    #!/usr/bin/python

    """
    this is a doc string
    """

    a = 5

    def foo():
        print("this is foo function")

    print("hello, this is my first module")

    if __name__ == "__main__":
        print("this string is under main") 

main.py

.. code-block:: python

    # -*- coding: utf-8 -*-
    #!/usr/bin/python

    print("before import")
    import myFirstModule as mfm

    print("after import")
    print("my first module attr a is: ", mfm.a)
    print("my first module method foo is: ",  mfm.foo) 
    print(mfm.__name__)
    print(mfm.__file__)
    print(mfm.__doc__)
