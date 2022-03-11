=========================================
Katana开发环境
=========================================

Katana中支持三种语言编程：Python，Lua和C++。Python应用于工作流非常方便，Lua用于OpScript节点。

Katana中选择菜单Tabs>Python即可打开Katana脚本编辑器。

API文档在Help>API Reference>Python APIs。

.. code-block:: python

    print(KatanaFile.__file__)
    print(type(KatanaFile))
    print(dir(KatanaFile))
    # C:\Program Files\Katana3.5v2/bin/python\PyUtilModule\KatanaFile.pyc
    # <type 'module'>
    # ['AllowFileOverwrite', 'AssetAPI', 'Callbacks', 'Configuration', 'CrashSave', 'CrashSaveDisable', 'CrashSaveEnable', 'CreateSceneAsset', 'Export', 'FileUtils', 'GetCrashActions', 'GetCrashTime', 'GetKatanaXMLElement', 'GetNextCrashFileName', 'GetViableCrashFiles', 'Import', 'IsFileDirty', 'IsFileSavedAsAsset', 'Load', 'MAX_CRASH_FILES', 'New', 'NodegraphAPI', 'Nodes2DAPI', 'Nodes3DAPI', 'Paste', 'PopFileDirtyState', 'PostCreateSceneAsset', 'PushFileDirtyState', 'RegisterPasteHandler', 'Revert', 'Save', 'ScenegraphBookmarkManager', 'SetFileDirty', 'UndoEntries', 'Utils', 'WasFileLoadedFromCrashFile', 'WasFileVersionedOnLoad', '_CleanupRenderNodes', '_ContainsModifiedLiveGroupNodes', '_CrashActions', '_CrashDisable', '_CrashFilePreviouslySaved', '_CrashHandlerUndoCB', '_CrashIndex', '_CrashSaveImpl', '_EvaluateFilename', '_ExportNodesToFile', '_FileDirty', '_FileDirtyStates', '_FileLoadedFromCrashFile', '_FileVersionedOnLoad', '_FindRenderNodes', '_LastCrashSave', '_RestoreFileDirty', '_SaveAndPublish', '_SaveFile', '_SaveFileDirty', '_SetKatanaSceneNameAndSourceFile', '__PasteHandlers', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'log', 'logging', 'operator', 'os', 'stat', 'time', 'xml']

参考文档：

- https://learn.foundry.com/katana/3.5/dev-guide/index.html
- https://support.foundry.com/hc/zh-cn/articles/360001288699-Q100443-Katana%E4%B8%AD%E7%9A%84%E8%84%9A%E6%9C%AC%E5%92%8C%E7%BC%96%E7%A8%8B
