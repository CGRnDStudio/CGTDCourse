==============================================================
ReadTheDocs+Sphinx+Github搭建写书环境
==============================================================

----------
安装Python
----------

作者使用的是Python 3.7.2，你可以选用更高的版本，未做测试。
上官网下载
安装的时候记得自定义安装路径选择C:\Python37

--------------------
配置环境变量Path
--------------------
这里为了以下指令能使用，需要将C:\Python37和C:\Python37\Scripts加入到用户变量或者系统变量Path
注意如果有安装Python其它版本注意Path的先后问题。

--------------------
安装Sphinx
--------------------
通过pip安装Sphinx，如果使用国外镜像源安装会非常慢，这里通过阿里云的镜像安装。
pip install sphinx
pip install sphinx-autobuild
pip install sphinx_rtd_theme
pip install recommonmark
pip install sphinx-markdown-tables

--------------------
初始化项目配置
--------------------
随便创建个文件夹，比如CGTDCourse
打开命令行窗口，将当前路径指到此文件夹，执行指令
sphinx-quickstart
写上项目名，作者名，版本号，其它默认
如果顺利完成则会产生两个文件夹和两个文件
找到source\conf.py文件，添加两行，将主页修改，不然后面ReadTheDocs编译遇到contents.rst问题
# The master toctree document.
master_doc = 'index'

修改主题风格
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

--------------------
创建案例文件
--------------------
主要以rst为格式的文件，创建个readme.rst，里面通过rst语法格式书写作者信息
在index.rst中配置readme

--------------------
清空编译项目
--------------------
make clean
make html

到此本地文档就完成了，可以打开build中index.html查看

--------------------
托管Github
--------------------
Github上创建一个项目CGTDCourse，将项目所有文件上传Github

-------------------------
ReadTheDocs配置自动编译
-------------------------
登陆ReadTheDocs官网，import这个Github项目之后构建，阅读文档即可