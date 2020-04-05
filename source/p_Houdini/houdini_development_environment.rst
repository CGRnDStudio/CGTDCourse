==============================
Houdini搭建VS Code开发环境
==============================

* 安装VS Code
* 安装Python插件
* 安装VEX插件
* 配置VS Code

.. code-block:: python

    {
    "python.linting.pylintEnabled": false,
    "python.linting.pep8Enabled": true,
    "editor.renderWhitespace": "all",
    "editor.mouseWheelZoom": true,
    "editor.rulers": [79, 120, 150],
    "editor.tabSize": 4,
    "window.title": "${activeEditorLong}",
    "python.pythonPath": "C:/Python27/python.exe"
    }

* 下载Houdini Expression Editor

.. code-block:: python

    https://cgtoolbox.com/

* 配置HOUDINI_PATH，安装Houdini Expression Editor
* 配置扩展编辑器快捷键

.. code-block:: python

    Ctrl+Shift+Alt+LM

Python Shell
Python Source Editor & hou.session
CG Toolbox扩展编辑器配置
VS Code开发环境配置
Python & VEX插件安装
认识Houdini扩展开发层级结构
HOUDINI_PATH & sys.path
创建工具架工具导入模块打印Hello World
创建自定义Desktop
Presets & Gallery
FBres 自定义分辨率配置
jump.pref结合环境变量使用
配置HotkeyOverrides文件自定义快捷键 Ctrl+Shift+Alt+左键
配置radialmenu文件自定义热盒
配置ExampleMenu.xml自定义主菜单 & MainMenuCommon.xml

http://cgtoolbox.com/


Python Shell

Python Source Editor


将HoudiniExprEditor插件配置到HOUDINI_PATH中
from HoudiniExprEditor import ParmWatcher
reload(ParmWatcher)
ParmWatcher.set_external_editor()
