=========================================
Katana Python开发文档
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


-----------------------
参考文档
-----------------------

- https://learn.foundry.com/katana/3.2/dev-guide/py-modindex.html
