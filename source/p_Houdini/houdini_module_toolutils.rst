==============================
Houdini模块：toolutils
==============================

- 查询某一类型所有节点，比如查询所有的File Cache节点

.. code-block:: python

    import toolutils

    nodes = toolutils.findAllChildNodesOfType(hou.node("/obj"), "filecache", dorecurse=True)

    for node in nodes:
        print(node.path())

- 与Scene View窗口交互，比如只能选择相机得到结果。

.. code-block:: python

    import toolutils

    scene_viewer = toolutils.sceneViewer()
    selected_objects = scene_viewer.selectObjects("Select a camera and press Enter", allowed_types = ["cam"])
    print(selected_objects)

- 设置当前视图相机

.. code-block:: python

    >>> import toolutils
    >>> scene_view = toolutils.sceneViewer()
    >>> viewport = scene_view.curViewport()
    >>> viewport.setCamera(hou.node("/obj/cam1/"))
    >>> 

.. code-block:: python

    import toolutils

    kwargs["pane"] = None

    toolutils.createOrShowPythonPanel(kwargs, "attribmanager", "Attribute Manager", 4)

.. code-block:: python

    >>> import toolutils
    >>> 
    >>> scene_view = toolutils.sceneViewer()
    >>> 
    >>> scene_view
    <hou.SceneViewer panetab1>
    >>> scene_view.pwd()
    <hou.Node at /obj>
    >>> scene_view.pwd()
    <hou.ObjNode of type geo at /obj/geo1>
    >>> scene_view.curViewport()
    <hou.GeometryViewport persp1 of type Perspective>
    >>> 
    >>> viewport = scene_view.curViewport()
    >>> viewport
    <hou.GeometryViewport persp1 of type Perspective>
    >>> settings = viewport.settings()
    >>> settings
    <hou.GeometryViewportSettings>
    >>> 
    >>> settings.camera()
    >>> settings.camera()
    <hou.ObjNode of type cam at /obj/cam1>
    >>> 

