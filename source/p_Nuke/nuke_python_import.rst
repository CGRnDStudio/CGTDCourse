================================
Nuke Python导入nk文件的几种方式
================================

基于流程的话经常要通过代码来处理nk文件导入导出的问题，下面总结一些用法，不能以偏概全。

.. code-block:: python

    import nuke

    path = "D:/blablabla.nk"

    # 清空当前场景
    nuke.scriptClear()
    # 打开nk文件，如果当前场景为空，会直接打开此nk文件，如果场景不为空，则会另开Nuke软件打开，功能同菜单File>Open Comp...
    nuke.scriptOpen(path)
    # 在当前场景中导入nk文件中所有节点，不管当前场景是否为空，导入成功导入的所有节点会是选择状态，功能同菜单File>Insert Comp Nodes...
    nuke.nodePaste(path)
    # 在当前场景中导入nk文件中所有节点，不管当前场景是否为空，导入成功没有节点是被选中状态。
    nuke.scriptReadFile(path)
    # 同上
    nuke.scriptReadText(path)
    # 同上
    nuke.scriptSource(path)
    # 将当前场景文件存储到path设置的路径，功能同菜单File>Save Comp
    nuke.scriptSave(path)
    # 功能同菜单File>Save Comp As...
    nuke.scriptSaveAs()
    nuke.scriptSaveAndClear()
    # 功能同菜单File>Close Comp
    nuke.scriptClose()
    # 功能同菜单File>Quit
    nuke.scriptExit()
    # 新建Nuke，功能同菜单File>New Comp...
    nuke.scriptNew()
