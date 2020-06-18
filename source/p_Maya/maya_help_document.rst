==============================
Maya帮助文档
==============================

- MEL Command & Function

.. code-block:: python

    import maya.cmds as cmds
    import maya.mel as mel
    import pymel.core as pm

- Maya Python API 1.0
- Maya Python API 2.0
- C++ API

Script Editor脚本编辑器面板用法

MEL Command VS Function

MEL命令基本语法 命令 参数 参数 参数 操作对象

从历史记录中提取MEL命令

help/whatIs方法

.. code-block:: python

    whatIs scale;
    whatIs polyCube;
    whatIs polySmooth;
    whatIs polyCleanupArgList;

MEL命令的CQEM模式

- C 新设置某个参数数值 直接使用 move -x -y -z
- Q 获取某个参数当前数值 前面加q, 后面不加值 xform -q -bb
- E 编辑已经存在的参数 前面加e, 后面加新值 joint -e -p 0 0 0
- M 多次调用当前参数 直接重复调用参数 curve -p 0 0 0 -p 0 1 0 -p…

.. code-block:: python

    ls
    listRelatives
    listConnections
    listAttr
    getAttr
    setAttr

很多MEL函数是不在帮助文档中的

global proc

两种函数 一种global function 一种helper function

Python分四种

包装MEL的maya.cmds
包装C++ API的maya.OpenMaya 只有C++的doc
Maya Python 1.0
Maya Python 2.0
import maya.api.OpenMaya as om

pymel

打印选择的物体

MEL强类型语言

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

    import maya.OpenMaya as om

    selslist = om.MSelectionList()
    om.MGlobal.getActiveSelection(selsList)

    for idx in range(0,  selsList.length()):
        dagPath = om.MDagPath()
        sels.getDagPath(idx, dagPath)
        print(dagPath.fullPathName())
        print(dagPath.partialPathName())
        print("%d : long-name : %s" % (idx, dagPath.fullPathName()))
    
pymel

第三方包装MEL Command的pythonic的包

https://help.autodesk.com/cloudhelp/2018/JPN/Maya-Tech-Docs/PyMel/index.html

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

MAttribute
MFn

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
- https://www.youtube.com/watch?v=GiWkXufclTY&t=13s
- https://knowledge.autodesk.com/support/maya/getting-started/caas/simplecontent/content/maya-documentation.html
- http://help.autodesk.com/view/MAYAUL/2018/CHS/

