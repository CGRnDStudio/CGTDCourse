==============================
Maya用户界面
==============================

Maya中自定义用户界面有很多种方案，MEL可以写用户界面，cmds也可以写用户界面，推荐使用内置的PySide2来写用户界面。

.. code-block:: python

    import maya.cmds as cmds

    win = "myFirstWindow"

    if cmds.window(win, q=1, exists=1):
        cmds.deleteUI(win, wnd=1)

    if cmds.windowPref(win, q=1, exists=1):
        cmds.windowPref(win, r=1)

    myWindow = cmds.window(win, w=400, h=300, t="My First Window Options:")

    cmds.columnLayout()

    for i in range(5):
        cmds.button(l="Button%d" % i, c="print(%d)" % i)

    cmds.showWindow(myWindow)
