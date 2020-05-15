=============================
Python IDE
=============================

IDE 的全称是：Integrated Development Environment，简称 IDE，也称为 Integration Design Environment、Integration Debugging Environment，翻译成中文叫做“集成开发环境”，在台湾那边叫做“整合開發環境”。它是一种辅助程序员开发用的应用软件。

IDE 通常包括程式语言编辑器、自动建立工具、通常还包括除错器。有些 IDE 包含编译器/直译器，如微软的 Microsoft Visual Studio，有些则不包含，如 Eclipse、SharpDevelop 等，这些 IDE 是通过调用第三方编译器来实现代码的编译工作的。有时 IDE 还会包含版本控制系统和一些可以设计圆形用戶界面的工具。许多支援物件导向的现代化 IDE 还包括了类別浏览器、物件检视器、物件结构图。虽然目前有一些IDE支援多种程式语言（例如 Eclipse、NetBeans、Microsoft Visual Studio），但是一般而言，IDE 主要还是针对特定的程式语言而量身打造（例如 Visual Basic）。

* 集成开发环境

    - Visual Studio Code
    - JetBrains PyCharm
    - Sublime Text 3

* 文本编辑器

    - Notepad++
    - Vim

* 交互式开发环境

    - IDLE
    - DreamPie
    - IPython

* VSCode配置

.. code-block:: bash

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

* VSCode快捷键

    - Ctrl + /：注释、反注释
    - Ctrl + F2：选中所有相同字段以便批量修改
    - Ctrl + D：逐个选中相同字段以便批量修改
    - Shift + Alt + LM：列模式编辑
    - Shift + Alt + ↑/↓：向上、向下复制

* VSCode好用的插件

    - Python
    - VEX
    - MayaCode
    - Code Runner
