==============================
Maya自定义插件
==============================


代码所存在的问题
类名大驼峰的写法
代码不符合PEP8规范
代码单引号双引号统一
代码使用Git管理测试上线
varName != None改成not varName
docstring和注释需要规范


如何编写一个简单的.py插件工具
如何在启动的时候
Maya扩展开发的层级结构

插件环境变量部署

.. code-block:: bash

    # C:\Program Files\Autodesk\Maya2017\modules\hprender.mod
    + hpRender any C:/Users/huweiguo/Documents/.RENDER_ROOT/MayaPlugin/Setup/2017
    PATH +:= bin

PATH +:= bin意味着将路径C:/Users/huweiguo/Documents/.RENDER_ROOT/MayaPlugin/Setup/2017/bin路径添加到PATH环境变量中，这里的加bin文件夹并没有任何作用，可以删除

扩展开发层级结构

plug-ins中添加需要加载的插件
scripts中写菜单工具执行的模块代码

Maya环境变量
MAYA_PLUG_IN_PATH 插件文件位置
MAYA_MODULE_PATH mod文件位置
MAYA_SCRIPT_PATH 脚本文件位置
XBMLANGPATH 图标文件位置

Maya.env配置的案例

.. code-block:: bash

    MTOAROOT = \\server\manager\thirdParty\maya\mtoa\3.1.2.1\2018

    REDSHIFT_COREDATAPATH = \\server\manager\thirdParty\maya\Redshift\2.5.48

    QAULOTH_PATH = \\server\manager\thirdParty\maya\Qualoth

    REDSHIFT_PLUG_IN_PATH = %REDSHIFT_COREDATAPATH%\Plugins\Maya\2018\nt-x86-64
    REDSHIFT_SCRIPT_PATH = %REDSHIFT_COREDATAPATH%\Plugins\Maya\Common\scripts
    REDSHIFT_XBMLANGPATH = %REDSHIFT_COREDATAPATH%\Plugins\Maya\Common\icons
    REDSHIFT_RENDER_DESC_PATH = %REDSHIFT_COREDATAPATH%\Plugins\Maya\Common\rendererDesc
    REDSHIFT_CUSTOM_TEMPLATE_PATH = %REDSHIFT_COREDATAPATH%\Plugins\Maya\Common\scripts\NETemplates
    REDSHIFT_MAYAEXTENSIONSPATH = %REDSHIFT_PLUG_IN_PATH%\extensions
    REDSHIFT_PROCEDURALSPATH = %REDSHIFT_COREDATAPATH%\Procedurals

    MAYA_MODULE_PATH = %MAYA_MODULE_PATH%;%MTOAROOT%
    PATH = %PATH%;%MTOAROOT%\bin;%REDSHIFT_COREDATAPATH%\bin
    MAYA_RENDER_DESC_PATH = %MAYA_RENDER_DESC_PATH%;%MTOAROOT%;%REDSHIFT_RENDER_DESC_PATH%
    PYTHONPATH = %PYTHONPATH%;%MTOAROOT%\scripts;%REDSHIFT_SCRIPT_PATH%
    solidangle_LICENSE = 5053@farm.do-vfx.com
    MAYA_PLUG_IN_PATH = %REDSHIFT_PLUG_IN_PATH%;%QAULOTH_PATH%\bin
    MAYA_SCRIPT_PATH = %REDSHIFT_SCRIPT_PATH%;%QAULOTH_PATH%\script
    XBMLANGPATH = %REDSHIFT_XBMLANGPATH%
    MAYA_CUSTOM_TEMPLATE_PATH = %REDSHIFT_CUSTOM_TEMPLATE_PATH%

    MAYA_DISABLE_CLIC_IPM = 1

来看下如何写个py的插件到插件管理器吧，分两步
注册插件
C:\Users\huweiguo\Documents\.RENDER_ROOT\MayaPlugin\Setup\2017\plug-ins
hpRender.py

如何创建自定义菜单

.. code-block:: python

    #!/usr/bin/python
    # -*- coding: utf-8 -*-
    
    """
    Custom menu plug-in
    """
    
    import os
    import sys
    
    import maya.cmds as cmds
    import maya.mel as mel
    import maya.OpenMayaMPx as omm
    
    
    def initializePlugin(mobject):
    """
    Initialize the script plug-in
    """
    mPlugin = omm.MFnPlugin(mobject, "tdUtils", "1.0", "any")
    
    if cmds.menu("menuTD", exists=1):
        cmds.deleteUI("menuTD", menu=1)
    
    gMainWindow = mel.eval("global string $gMainWindow;$temp = $gMainWindow")
    cmds.menu("menuTD", label="TD Tools", parent=gMainWindow,
                tearOff=1, allowOptionBoxes=1)
    cmds.menuItem(dividerLabel="General", divider=True)
    cmds.menuItem(label="Submit To Deadline", parent="menuTD",
                    command="print(100)")
    cmds.menuItem(dividerLabel="Step", divider=True)
    cmds.menuItem("menuRIG", label="RIG", parent="menuTD",
                    subMenu=True, tearOff=True)
    cmds.menuItem(label="Select Skin Joint", parent="menuRIG",
                    command="print(100)")
    
    
    def uninitializePlugin(mobject):
    """
    Uninitialize the script plug-in
    """
    mPlugin = omm.MFnPlugin(mobject)
    
    if cmds.menu("menuTD", exists=1):
        cmds.deleteUI("menuTD", menu=1)

sys.path模块导入机制
import hpMayaClient
reload(hpMayaClient)
hpMayaClient.client().main()

main函数的核心
checkList
检测客户端是否安装
检测C盘是否有读写权限
检测文件是否保存
检测每一层渲染层的渲染帧数范围，这块没必要用正则表达式，可以直接获取
cmds.getAttr("defaultRenderGlobals.startFrame")
分析渲染层的函数
如何获取当前场景中用到的所有插件
如何获取当前场景中用到的所有资产文件
cmds.file(query=True, list=True, withoutCopyNumber=True)
ver.ini检测Maya版本信息
检测插件版本C:\Users\huweiguo\Documents\.RENDER_ROOT\MayaPlugin\mayaPluginItems_2017.ini
检测每一层的渲染设置
UI
cmds.window
窗口如果存在删除
控件(button, text, intFieldGrp, checkBox, textFieldGrp, radioButtonGrp)
布局

PyQt重写界面
PySide & PyQt4
PySide2 & PyQt5
PyQt4和PyQt5 uic
pyside-uic

.. code-block:: python

    # Maya Dialog
    import sys
    import maya.OpenMayaUI as omui
    from PySide2 import QtCore
    from PySide2 import QtWidgets
    from shiboken2 import wrapInstance

    path = "D:/2019/centralizeTools/houdini/scripts/python"

    path in sys.path or sys.path.insert(0, path)
    from houQt import mainDialog


    def _get_maya_main_window():
        pointer = omui.MQtUtil.mainWindow()
        return wrapInstance(long(pointer), QtWidgets.QWidget)


    class WindowA(QtWidgets.QDialog, mainDialog.Ui_Dialog):
        def __init__(self, parent=None):
            super(WindowA, self).__init__(parent)
            self.setupUi(self)


    def show():
        dialog = WindowA(_get_maya_main_window())
        dialog.show()

    if __name__ == "__main__":
        show()

.. code-block:: python

    # Maya Main Window
    import sys
    import maya.OpenMayaUI as omui
    from PySide2 import QtCore
    from PySide2 import QtWidgets
    from shiboken2 import wrapInstance

    path = "D:/2019/centralizeTools/houdini/scripts/python"

    path in sys.path or sys.path.insert(0, path)
    from houQt import mainWin


    def _get_maya_main_window():
        pointer = omui.MQtUtil.mainWindow()
        return wrapInstance(long(pointer), QtWidgets.QWidget)


    class WindowB(QtWidgets.QMainWindow, mainWin.Ui_MainWindow):
        def __init__(self, parent=None):
            super(WindowB, self).__init__(parent)
            self.setupUi(self)


    def show():
        dialog = WindowB(_get_maya_main_window())
        dialog.show()

    if __name__ == "__main__":
        show()

    if cmds.window(WINDOW_NAME, exists=True, q=True):
        cmds.deleteUI(WINDOW_NAME)
