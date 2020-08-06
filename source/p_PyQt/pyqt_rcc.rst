=============================
PyQt Designer安装与使用
=============================

------------------
基本概况
------------------

Houdini、Maya与Nuke中内置PySide2

了解PyQt的历史以及协议
PySide & PyQt4 & Qt4
PySide2 & PyQt5 & Qt5

https://github.com/mottosso

Qt.py如何使用?


PySide2安装&部署
PySide2层级结构
- QtCore 核心算法库
- QtGui 界面图形算法库
- QtWidgets 界面控件库
- uic ui文件到py文件的桥梁
- sip C++对象到Python转换库


Designer使用

setModel
QThread
QSQL

- 配置左下角托盘
- 修改图标
- 如何部署自己的app

- 编译qrc相对路径

创建resource.qrc
"C:\Python27\Scripts\pyside-uic.exe" -o deploy.py deploy.ui
"C:\Python27\Lib\site-packages\PySide\pyside-rcc.exe" -o resource_rc.py resource.qrc

loadUi

认识qss
下载qss
修改qss


------------------
参考文档
------------------

- https://www.riverbankcomputing.com/static/Docs/PyQt4/classes.html
- https://doc.bccnsoft.com/docs/PyQt5/class_reference.html
