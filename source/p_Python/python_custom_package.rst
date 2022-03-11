=============================
Python自定义包
=============================

- 包的唯一标识__init__.py
- 查询包路径__path__
- 包的层级结构
- 通配导入__all__
- 包的相对路径导入

包（package）是将一些模块组织在一起构成一个更大规模的模块，也是Python中对模块的更高一级的抽象。Python允许用户把目录当成模块看待，目录中不同模块文件，就变成了包里面的子模块。一个包可以由一个或多个模块或子包构成的模块，包目录下不但可以包含作为子模块的py文件，还可以包含子目录，这些子目录也可以是Python的包。

- __init__.py文件的作用?

当一个文件夹中存在一个__init__.py文件时，这个文件夹就会被Python解释器识别为一个包。__init__.py除了标识一个文件夹是包的作用以外，它还可以执行一些初始化操作。在使用import导入一个模块的时候，__init__.py文件会首先被执行。因此__init__.py中可以写一些初始化的代码，比如导入其他依赖的Python模块。

- 如何验证__init__.py是优先被导入的?

绝大部分时候让__init__.py文件空着就好。

- 查询包路径__path__

__path__是一个包自带的隐藏属性，它描述一个包的完整路径，也是包的一个标识。

- 包的层级结构

封装成包是很简单的。在文件系统上组织你的代码，并确保每个目录都定义了一个__init__.py文件。

.. code-block:: python

    chooseTask/
        __init__.py
        ui/
            __init__.py
            resource.py
        config/
            __init__.py
            user.py
            sg.py
        mainWin.py

有了上面的层级结构，你可以执行各种import语句

包的相对路径导入

Python自定义包的相对导入问题?

Python 2.x和3.x包导入的区别

相对导入对执行方式是有一定的要求，不同执行方式可能会报一种不是错误的错误

假设现在有一个myPackage的包

.. code-block:: python

    myPackage/
        __init__.py
        aaa/
            __init__.py
            spam.py
            grok.py
        bbb/
            __init__.py
            bar.py

如果模块myPackage.aaa.spam要导入同目录下的模块grok

.. code-block:: python

    # myPackage/aaa/spam.py
    from . import grok

如果模块myPackage.aaa.spam要导入不同目录下的模块bbb.bar

.. code-block:: python

    # myPackage/aaa/spam.py
    from ..bbb import bar

.. code-block:: python

    # -*- coding: utf-8 -*-
    #!/usr/bin/python

    """
    this is a doc string of test pack
    """

    a = 1
    b = 2

    def foo():
        print("fool")
