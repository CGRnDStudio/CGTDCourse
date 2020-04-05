==============================
Maya线性工作流工具
==============================

核心思想 
数据类型，对应的特性，属性与方法
listAttr getAttr setAttr
检测插件&加载插件
pymel pythonic
参数设置的两种方案
实例化对象
模块的导入导出 sys.path
设置AOV

管中窥豹：延伸阅读
cmds VS pymel
pymel第三方文档
Maya中有哪些扩展接口
MEL command & function
import maya.cmds as cmds
import maya.mel as mel
import pymel.core as pm
Python API 1.0
Python API 2.0
C++ API 

检测插件&加载插件

.. code-block:: python

    import pymel.core as pm

    if "mtoa" not in pm.pluginInfo(query=True, listPlugins=True):
        try:
            pm.loadPlugin("mtoa")
        except:
            pm.error("Fail to Load Arnold Render!!")
        pm.PyNode("defaultRenderGlobals").currentRender.set("arnold")


https://help.autodesk.com/cloudhelp/2018/JPN/Maya-Tech-Docs/PyMel/index.html

.. code-block:: python

    from pprint import pprint
    import pymel.core as pm

    # 返回所有节点
    pprint(pm.ls())
    # 实例化节点
    renderGlobals = pm.PyNode("defaultRenderGlobals")
    attrs = renderGlobals.listAttr()
    pprint(attrs)

    print(type(renderGlobals.currnetRenderer))
    print(dir(renderGlobals.currnetRenderer))
    renderGlobals.setAttr("currentRendererer", "arnold")
    renderGlobals.currentRenderer.set("arnold")
    pm.setAttr("defaultRenderGlobals.currentRenderer", "arnold")
    pm.PyNode("defaultRenderGlobals.currentRenderer").set("arnold")

    aiOptions = pm.PyNode("defaultArnoldRenderOptions")

    # defaultRenderGlobals
    # defaultArnoldRenderOptions
    # defaultArnoldFilter
    # defaultArnoldDriver

    pm.PyNode("defaultRenderGlobals.animation").set(True)

    import maya.cmds as cmds
    # cmEnabled
    # renderingSpaceName
    # viewTransformName
    # defaultInputSpaceName
    # colorManagePots
    cmds.colorManagementPrefs(e=True, parm=value)


    # 软件版本的兼容性
    import pymel.core as pm

    print(pm.about(version=True))

    import sys
    path = "D:/"
    path in sys.path or sys.path.insert(0, path)
    print(sys.path)

    from renderTools import linearWorkflowCheck
    reload(linearWorkflowCheck)
    linearWorkflowCheck.maya_ui()

.. code-block:: python

    from pprint import pprint
    import maya.cmds as cmds

    pprint(cmds.file(query = True, list = True, withoutCopyNumber = True))
