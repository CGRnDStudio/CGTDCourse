=====================================
ReadTheDocs+Sphinx+Github搭建写书环境
=====================================

-----------
安装Python
-----------

测试的操作系统 ``Windows 10 1809``，Python版本 ``3.7.2`` ，你可以选用py更高的版本，未做测试。上官网 https://www.python.org/ 下载。py3安装的时候记得自定义安装路径选择 ``C:\Python37`` ，默认路径是在当前用户文件夹，使用起来不太方便。

----------------
配置环境变量Path
----------------

这里为了下文命令能使用，需要将 ``C:\Python37`` 和 ``C:\Python37\Scripts`` 两个路径加入到用户变量或者系统变量Path中。注意如果有安装Python其它版本注意Path的先后问题，确保下文所调用的命令是文件夹 ``C:\Python37\Scripts`` 中的应用，如果确实搞不定这个，直接用绝对路径执行亦可。

-----------
安装Sphinx
-----------

通过pip安装Sphinx，如果使用国外镜像源安装会非常慢，可以通过阿里云的镜像安装。

.. code-block:: python

    pip install sphinx
    pip install sphinx-autobuild
    pip install sphinx_rtd_theme
    pip install recommonmark
    pip install sphinx-markdown-tables

或

.. code-block:: python

    pip install sphinx -i https://mirrors.aliyun.com/pypi/simple
    pip install sphinx-autobuild -i https://mirrors.aliyun.com/pypi/simple
    pip install sphinx_rtd_theme -i https://mirrors.aliyun.com/pypi/simple
    pip install recommonmark -i https://mirrors.aliyun.com/pypi/simple
    pip install sphinx-markdown-tables -i https://mirrors.aliyun.com/pypi/simple

--------------
初始化项目配置
--------------

在计算机中任何位置创建个文件夹，比如CGTDCourse。打开命令行窗口，将当前路径切换到此文件夹，执行命令。

.. code-block:: python

    sphinx-quickstart

写上项目名，作者名，版本号，其它默认，如果顺利完成则会产生两个文件夹和两个文件。找到 ``source\conf.py`` 配置文件，添加下面两行配置，将主页配置修改，否则后面ReadTheDocs构建文档时会遇到contents.rst错误。

.. code-block:: python

    # The master toctree document.
    master_doc = 'index'

修改下面两行以改变主题风格。

.. code-block:: python

    # html_theme = 'alabaster'
    html_theme = 'sphinx_rtd_theme'

------------
创建案例文件
------------

主要以rst为格式的文件，创建个readme.rst，里面通过rst语法格式书写作者信息，在index.rst中配置readme。具体内容可以研究文末参考文档。

------------
清空编译项目
------------

此时在命令行窗口继续执行下面的命令。

.. code-block:: python

    make clean
    make html

构建过程中如果报错，需要检查环境变量的设置以及配置或者文档写的语法不正确，到此本地文档就完成了，可以打开build中index.html查看。

-----------
托管Github
-----------

Github上创建一个项目CGTDCourse，将项目所有文件上传Github管理。

-----------------------
ReadTheDocs配置自动编译
-----------------------

登陆ReadTheDocs官网，import这个Github项目之后构建，构建成功阅读文档即可，之后在本地写的文章只要通过Git提交到代码仓库，ReadTheDocs会自动构建成在线文档。

--------
参考文档
--------

Sphinx+github+ReadtheDocs书写笔记: https://pengshiyu.blog.csdn.net/article/details/79388919
Python Cookbook 3rd Edition Documentation: https://github.com/yidao620c/python3-cookbook
