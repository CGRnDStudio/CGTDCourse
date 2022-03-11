=========================================
Katana开发文档
=========================================

.. code-block:: python

    import Katana
    print(type(Katana))
    print(dir(Katana))
    # <type 'module'>
    # ['AssetAPI', 'AssetBrowser', 'AttrDump', 'BezierModule', 'CEL', 'CacheManager', 'Callbacks', 'CatalogAPI', 'CatalogManager', 'ChildProcess', 'ColorPaletteManager', 'ColorUtils', 'Configuration', 'Decorators', 'Documentation', 'DrawingModule', 'EnvUtils', 'ExpressionMath', 'FaceSelectionManager', 'FarmAPI', 'FarmManager', 'FileUtils', 'FnAttribute', 'FnGeolib', 'FnGeolibServices', 'FnKatImport', 'FormMaster', 'GeoAPI', 'Hints', 'Imath', 'Initialize', 'KatanaFeatures', 'KatanaFile', 'KatanaPrefs', 'KatanaResources', 'LayeredMenuAPI', 'LensDistortUtils', 'LiveRenderAPI', 'LogGLHandlers', 'LogGLHandlersOldLevel', 'LookFileBakeAPI', 'MachineInfo', 'Manifest', 'MediaCache', 'MediaCacheHandler', 'Naming', 'NodeDebugOutput', 'NodeGraphView', 'NodeMaster', 'NodegraphAPI', 'Nodes2DAPI', 'Nodes3DAPI', 'NonUIPluginManager', 'OCIO', 'OpenEXR', 'OpenGL', 'PluginSystemAPI', 'Plugins', 'PrefNames', 'PyFCurve', 'PyRerenderEventMapper', 'PyScenegraphAttr', 'PyXmlIO', 'QT4Browser', 'QT4Color', 'QT4FormWidgets', 'QT4GLLayerStack', 'QT4Panels', 'QT4Widgets', 'QTFCurve', 'Qt', 'QtCore', 'QtDesigner', 'QtGui', 'QtMultimedia', 'QtNetwork', 'QtOpenGL', 'QtSql', 'QtSvg', 'QtTest', 'QtWidgets', 'QtXml', 'QtXmlPatterns', 'RegisterToCamera', 'RenderManager', 'RenderingAPI', 'RerenderEventMapper', 'ResolutionTable', 'ResourceFiles', 'ScenegraphAttr', 'ScenegraphBookmarkManager', 'ScenegraphManager', 'Shelves', 'StartupScripts', 'SuperToolPlugins', 'UI4', 'UndoEntries', 'UniqueName', 'UserNodes', 'Utils', 'Vecmath', 'ViewerAPI', 'VirtualKatana', 'Widgets', 'WorkQueue', 'WorkingSet', 'WorkingSetClient', 'WorkingSetManager', '__builtins__', '__path__', 'binascii', 'cStringIO', 'copy', 'ctypes', 'datetime', 'enum', 'fnmatch', 'gc', 'glob', 'hotshot', 'itertools', 'logging', 'math', 'multiprocessing', 'operator', 'os', 'pprint', 're', 'select', 'shutil', 'signal', 'socket', 'stat', 'string', 'struct', 'subprocess', 'sys', 'tempfile', 'thread', 'time', 'traceback', 'update', 'urllib', 'version', 'weakref', 'xml']

- KatanaFile：文件操作模块
- RenderManager：渲染输出模块

源代码：C:\Program Files\Katana3.5v2\bin\python

.. code-block:: python

    print(KatanaFile.__file__)
    print(NodegraphAPI.__file__)
    print(RenderManager.__file__)

    # C:\Program Files\Katana3.5v2/bin/python\PyUtilModule\KatanaFile.pyc
    # C:\Program Files\Katana3.5v2/bin/python\NodegraphAPI\__init__.pyc
    # C:\Program Files\Katana3.5v2/bin/python\PyUtilModule\RenderManager\__init__.pyc

.. code-block:: python

    renderNode = NodegraphAPI.GetNode("Render")
    renderSettings = RenderManager.RenderingSettings()

    for frame in range(1, 6):
        print("-" * 80)
        renderSettings.frame = frame
        RenderManager.StartRender("diskRender", node=renderNode, settings=renderSettings)

批量修改某一类型节点参数

.. code-block:: python

    import NodegraphAPI

    print(dir(NodegraphAPI))

    nodes = NodegraphAPI.GetAllNodesByType("Alembic_In")

    for node in nodes:
        print(node)
        parm = node.getParameter("abcAsset")
        oldPath = parm.getValue(0)
        newPath = oldPath.replace("D:/cache/", "Z:/cache/")
        parm.setValue(newPath, 0)


创建节点，自动组装

.. code-block:: python

    rootNode = NodegraphAPI.GetRootNode()

    print(rootNode)

    print(dir(rootNode))

    primNode = NodegraphAPI.CreateNode("PrimitiveCreate", rootNode)

    print(primNode)

    mergeNode = NodegraphAPI.CreateNode("Merge", rootNode)

    print(mergeNode)

    print(dir(mergeNode))

    print(help(mergeNode.addInputPort))

    port = mergeNode.addInputPort("i11")

    print(port)
    print(dir(port))
    print(dir(primNode))
    port.connect(primNode.getOutputPorts()[0])


    node = NodegraphAPI.GetNode("InChar")

    print(node)

    print(node.getBaseType())
    print(node.getParameter("type").getValue(0))

    print(mergeNode.getInputPorts())

    import NodegraphAPI

    node = NodegraphAPI.GetNode("Material_Stack")

    print(type(node))
    print(dir(node))

    node.getChildNodes()

    material = NodegraphAPI.CreateNode("Material", NodegraphAPI.GetRootNode())

    node.buildChildNode(material)

    print(dir(material))

    print(dir(NodegraphAPI))

    material = NodegraphAPI.CreateNode("Material")
    material.setParent(NodegraphAPI.GetRootNode())

    print(material)

    print(NodegraphAPI.GetAllNodes())


参考文档：

- https://learn.foundry.com/katana/3.2/dev-guide/py-modindex.html
- https://learn.foundry.com/katana/dev-guide/index.html
