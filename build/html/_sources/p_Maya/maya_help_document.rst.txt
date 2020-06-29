==============================
Maya帮助文档
==============================

Maya帮助文档中开发的部分需要理解的是MEL Command以及Python Command文档部分的用法，包括案例，包括两种命令的切换。

Maya中编程语言分类大概有如下几种：

- MEL类：命令、函数、表达式
- Python类：cmds、pymel、Maya Python API 1.0、Maya Python API 2.0
- C++类：C++ API（不阐述）

- Script Editor

脚本编辑器可以通过菜单Windows>General Editors>Script Editor来打开，或者右下角脚本编辑器快捷按钮打开。

脚本编辑器中可以编写MEL和Python两种脚本语言，可以通过鼠标右键热盒菜单创建与删除面板。

- MEL Command

MEL命令基本语法：命令 -标签 -标签 -标签 操作对象;

从脚本编辑器的历史记录中提取MEL命令方法。

help/whatIs方法

.. code-block:: python

    whatIs scale;
    whatIs polyCube;
    whatIs polySmooth;
    whatIs polyCleanupArgList;

MEL命令的CQEM模式

- C 直接使用 新设置某个参数数值 move -x 1;
- Q 可以获取对象的当前参数 前面加q, 后面不加值 xform -q -bb;
- E 可以编辑对象的现有参数 前面加e, 后面加新值 joint -e -p 0 0 0;
- M 可以在一次命令下使用多次 直接重复调用参数 curve -p 0 0 0 -p 0 1 0 -p…;

.. code-block:: python

    ls
    listRelatives
    listConnections
    listAttr
    getAttr
    setAttr

- MEL Function

很多MEL函数是不在帮助文档中的，存在两种MEL函数，一种是global function，另一种是helper function，helper函数大多是mel文件中调用，与global函数作用域不同。

- Python

    - 封装MEL的伪Python代码maya.cmds
    - 第三方更Pythonic的封装PyMEL
    - Maya Python 1.0（封装C++ API，只有C++文档）
    - Maya Python 2.0（封装C++ API，只有C++文档）

cmds是官方出的一种简单封装MEL指令伪Python代码，没有按Python数据类型统一性来封装，MEL与cmds切换起来相对简单，写cmds实际就是在写MEL指令，文档中右上角可以通过MEL version或者Python version随意切换，MEL中的flag在Python中就是args。

pymel是第三方按Python统一性来封装的Python API，但是导入模块相对需要花一部分时间。

.. code-block:: python

    import maya.cmds as cmds
    import maya.mel as mel
    import pymel.core as pm
    import maya.api.OpenMaya as om

MEL是一种强类型语言

.. code-block:: bash

    string $sels[] = `ls -sl`;
    print($sels);

    string $sels[] = `ls -sl -l`;
    int $count = 1;

    for ($sel in $sels) {
        print((string)$count + " : " + $sel + "\n");
        $count++;
    }

.. code-block:: python

    import maya.cmds as cmds

    sels = cmds.ls(sl=True, l=True)

    for i, sel in enumerate(sels):
        print(str(i) + " : " + sel + "\n")

.. code-block:: python

    import maya.OpenMaya as om

    selslist = om.MSelectionList()
    om.MGlobal.getActiveSelection(selsList)

    for idx in range(0,  selsList.length()):
        dagPath = om.MDagPath()
        sels.getDagPath(idx, dagPath)
        print(dagPath.fullPathName())
        print(dagPath.partialPathName())
        print("%d : long-name : %s" % (idx, dagPath.fullPathName()))

第三方包装MEL的pythonic的包

.. code-block:: python

    import pymel.core as pm

    sels = pm.ls()

    for sel in sels:
        print(sel.longName())
        print(sel.shortName())
        print("-----------------")
        print(sel.tx.get())
        print(sel.ty.get())
        print(sel.tz.get())
        sel.tx.set(0)
        sel.ty.set(0)
        sel.tz.set(0)

.. code-block:: python

    import maya.OpenMaya as om

    selsList = om.MSelectionList()
    om.MGlobal.getActiveSelectionList(selsList)

    for idx in range(0, selsList.length()):
        mobject = om.MObject()
        selsList.getDependnode(idx, mobject)
        print(mobject.apiTypeStr())

        if mobject.apiType() == om.MFn.kTransform:
            print("This is a transform!")
        elif mobject.apiType() == om.MFn.kMesh:
            print("This is a mesh!")
        else:
            pass

        fnDependNode = om.MFnDependencyNode(mobject)
        print(fnDependnode.name())

----------------------
参考文档
----------------------

- https://vfxplatform.com/
- https://www.youtube.com/watch?v=GiWkXufclTY
- https://knowledge.autodesk.com/support/maya/getting-started/caas/simplecontent/content/maya-documentation.html
- http://help.autodesk.com/view/MAYAUL/2020/CHS/
- http://help.autodesk.com/view/MAYAUL/2020/CHS/?guid=__PyMel_index_html
- http://help.autodesk.com/view/MAYAUL/2020/CHS/?guid=Maya_SDK_MERGED_cpp_ref_index_html
