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

CG Toolbox扩展编辑器配置

将HoudiniExprEditor插件配置到HOUDINI_PATH中

.. code-block:: python

    from HoudiniExprEditor import ParmWatcher
    reload(ParmWatcher)
    ParmWatcher.set_external_editor()
