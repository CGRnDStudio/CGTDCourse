==============================
Houdini编程语言种类
==============================

Houdini中编程语言的种类
Python & VEX & HScript之间的区别和联系
Python的优缺点
VEX的优缺点
Python的执行环境种类
Python Shell
Python Source Editor & hou.session
Shelf Tools & Custom Menu
如何在工具架工具中编写Python代码
如何在自定义菜单中编写Python代码
Event Handler & Startup Scripts
123.py & 456.py & onCreated.py
Button Callback & HDA Scripts
Python Sops & Parameter Expressions

HScript, 
VEX, 
Python, 
Expression functions, 
openCL, 
HDK, 
C++


切换场景自动与手动更新工具架工具

.. code-block:: python

    def autoUpdate():
        """ Switch current auto update status
        """
        VIEW_UPDATE = "viewupdate %s %s.%s.world"
        currentDesktop = hou.ui.curDesktop()
        desktopName = currentDesktop.name()
        paneType = hou.paneTabType.SceneViewer
        paneTabName = currentDesktop.paneTabOfType(paneType).name()
        currentStatus = hou.hscript(VIEW_UPDATE % ("-c", desktopName, paneTabName))
        currentStatus = str(currentStatus)
        currentStatus = currentStatus[:-8]
        currentStatus = currentStatus[+16:]

        if currentStatus == "always":
            hou.hscript(VIEW_UPDATE % ("-u never", desktopName, paneTabName))
        else:
            hou.hscript(VIEW_UPDATE % ("-u always", desktopName, paneTabName))


Houdini Desktop设置 存储 默认启动 环境变量配置

@pscale = .5;
@N = rand(@ptnum);

For-Each Point

.. code-block:: python

    import os

    objectsPath = hou.node(".").parm("import").eval()

    folder = os.listdir(objectsPath)

    print(folder)

    rootNode = hou.node("../python_test")
    grid = rootNode.createNode("grid")
    wrangler = rootNode.createNode("attrbwrangle")
    wrangler.setInput(0, grid)

    switch = rootNode.create("switch")
    copy = rootNode.createNode("copytopoints")
    blockBegin = rootNode.createNode("block_begin", "begin")
    blockBegin

    blockEnd = rootNode.createNode("block_end", "end")
