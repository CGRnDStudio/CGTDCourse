==============================
Maya PyMEL
==============================

什么是pymel?

pymel 与mel以及cmds区别?


.. code-block:: python

    import pymel.core as pm
    import maya.cmds as cmds


- 返回类型不同

cmds只返回字符串

pymel返回实例对象，可以用type，dir以及help内置函数

.. code-block:: python

    # 通过pm.PyNode()将节点实例化

    resNode = pm.PyNode("defaultResolution")
    # 列出节点所有属性
    resNode.listAttr()
    resNode.width.set(720)
    resNode.width.get()
    pm.selected()

    Node Editor

    node.inputs()

    # 获取的是实例化对象，有属性和方法
    pm.sceneName()
    pm.env.minTime
    pm.env.maxTime
    pm.listCameras()

    import pymel.core as pm

    for k, v in pm.language.Env.envVars.items():
        print(k, v)


    fileName = pm.sceneName().splitext()[0].basename()
    startFrame = pm.env.minTime
    endFrame = pm.env.maxTime
    cameraName = "%s_f%03d_f%03d" % (fileName, startFrame, endFrame)
    cameraList = [cam for cam in pm.listCameras(p = True)]
    selPanel = pm.getPanel(withFocus = True)
    selCam = pm.modelPanel(selPanel, q=True, camera=True)
    cam = pm.PyNode(selCam)
    cam.rename(cameraName)

    node = pm.PyNode("defaultRenderGlobals")
    pm.listAttr(node)
    node.imageFilePrefix.set("<Scene>/<RenderLayer>")
    node.animation.set(1)
    node.startFrame.set(startFrame)
    node.endFrame.set(endFrame)
    pm.setAttr("defaultResolution.width", 1280)
    pm.setAttr("defaultResolution.height", 720)

https://help.autodesk.com/cloudhelp/2017/ENU/Maya-Tech-Docs/PyMel/