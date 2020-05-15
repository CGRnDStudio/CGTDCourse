==============================
Nuke模块：nuke
==============================

- 一般方法

.. code-block:: python

    import nuke

    print(nuke)
    print(type(nuke))
    print(nuke.__file__)
    print(dir(nuke))
    # Result: <module 'nuke' from 'C:/Program Files/Nuke10.5v1/plugins\nuke\__init__.pyc'>
    <type 'module'>
    C:/Program Files/Nuke10.5v1/plugins\nuke\__init__.pyc
    ['AColor_Knob', 'ADD_VIEWS', 'AFTER_CONST', 'AFTER_LINEAR', 'ALL', 'ALWAYS_SAVE', 'AnimationCurve', 'AnimationKey', 'Array_Knob', 'Axis_Knob', 'BBox_Knob', 'BEFORE_CONST', 'BEFORE_LINEAR', 'BREAK', 'BackdropNode', 'BeginTabGroup_Knob', 'Bitmask_Knob', 'Boolean_Knob', 'Box', 'Box3_Knob', 'CATMULL_ROM', 'CONSTANT', 'CUBIC', 'CancelledError', 'CascadingEnumeration_Knob', 'ChannelMask_Knob', 'Channel_Knob', 'ColorChip_Knob', 'Color_Knob', 'ColorspaceLookupError', 'DISABLED', 'DONT_CREATE_VIEWS', 'DONT_SAVE_TO_NODEPRESET', 'DO_NOT_WRITE', 'Disable_Knob', 'Double_Knob', 'ENDLINE', 'EXE_PATH', 'EXPAND_TO_WIDTH', 'EXPRESSIONS', 'EditableEnumeration_Knob', 'EndTabGroup_Knob', 'Enumeration_Knob', 'EvalString_Knob', 'Eyedropper_Knob', 'FLOAT', 'FONT', 'File_Knob', 'FnPySingleton', 'Font_Knob', 'Format', 'Format_Knob', 'FrameRange', 'FrameRanges', 'FreeType_Knob', 'GEO', 'GUI', 'GeoSelect_Knob', 'Gizmo', 'GlobalsEnvironment', 'Group', 'HIDDEN_INPUTS', 'HORIZONTAL', 'Hash', 'Help_Knob', 'Histogram_Knob', 'IArray_Knob', 'IMAGE', 'INPUTS', 'INT16', 'INT8', 'INTERACTIVE', 'INVALIDHINT', 'INVISIBLE', 'Info', 'Int_Knob', 'KNOB_CHANGED_RECURSIVE', 'Keyer_Knob', 'Knob', 'KnobType', 'LINEAR', 'LOG', 'Layer', 'Link_Knob', 'LinkableKnobInfo', 'LookupCurves_Knob', 'Lut', 'MATCH_CLASS', 'MATCH_COLOR', 'MATCH_LABEL', 'MONITOR', 'Menu', 'MenuBar', 'MenuItem', 'MultiView_Knob', 'Multiline_Eval_String_Knob', 'NODIR', 'NO_ANIMATION', 'NO_CHECKMARKS', 'NO_MULTIVIEW', 'NO_POSTAGESTAMPS', 'NO_UNDO', 'NUKE_VERSION_DATE', 'NUKE_VERSION_MAJOR', 'NUKE_VERSION_MINOR', 'NUKE_VERSION_PHASE', 'NUKE_VERSION_PHASENUMBER', 'NUKE_VERSION_RELEASE', 'NUKE_VERSION_STRING', 'NUM_CPUS', 'NUM_INTERPOLATIONS', 'Node', 'NodeConstructor', 'Nodes', 'Obsolete_Knob', 'OneView_Knob', 'OutputContext', 'PLUGIN_EXT', 'PREPEND', 'PROFILE_ENGINE', 'PROFILE_REQUEST', 'PROFILE_STORE', 'PROFILE_VALIDATE', 'PYTHON', 'Panel', 'PanelNode', 'Password_Knob', 'Precomp', 'ProgressTask', 'Pulldown_Knob', 'PyCustom_Knob', 'PyScript_Knob', 'PythonCustomKnob', 'PythonKnob', 'READ_ONLY', 'REPLACE', 'REPLACE_VIEWS', 'Radio_Knob', 'Range_Knob', 'Root', 'RunInMainThread', 'SAVE_MENU', 'SCRIPT', 'SMOOTH', 'STARTLINE', 'STRIP_CASCADE_PREFIX', 'Scale_Knob', 'SceneView_Knob', 'Script_Knob', 'String_Knob', 'TABBEGINCLOSEDGROUP', 'TABBEGINGROUP', 'TABENDGROUP', 'TABKNOB', 'THREADS', 'TO_SCRIPT', 'TO_VALUE', 'Tab_Knob', 'Text_Knob', 'ToolBar', 'Transform2d_Knob', 'USER_SET_SLOPE', 'UV_Knob', 'Undo', 'Unsigned_Knob', 'VIEWER', 'VIEW_NAMES', 'View', 'ViewView_Knob', 'Viewer', 'ViewerProcess', 'ViewerWindow', 'WH_Knob', 'WRITE_ALL', 'WRITE_NON_DEFAULT_ONLY', 'WRITE_USER_KNOB_DEFS', 'XYZ_Knob', 'XY_Knob', '__all__', '__builtins__', '__doc__', '__file__', '__filterNames', '__name__', '__package__', '__path__', 'activeViewer', 'addAfterBackgroundFrameRender', 'addAfterBackgroundRender', 'addAfterFrameRender', 'addAfterRecording', 'addAfterRender', 'addAfterReplay', 'addAutoSaveDeleteFilter', 'addAutoSaveFilter', 'addAutoSaveRestoreFilter', 'addAutolabel', 'addBeforeBackgroundRender', 'addBeforeFrameRender', 'addBeforeRecording', 'addBeforeRender', 'addBeforeReplay', 'addDefaultColorspaceMapper', 'addFavoriteDir', 'addFilenameFilter', 'addFormat', 'addKnobChanged', 'addNodePresetExcludePaths', 'addOnCreate', 'addOnDestroy', 'addOnScriptClose', 'addOnScriptLoad', 'addOnScriptSave', 'addOnUserCreate', 'addRenderProgress', 'addSequenceFileExtension', 'addToolsetExcludePaths', 'addUpdateUI', 'addValidateFilename', 'addView', 'afterBackgroundFrameRender', 'afterBackgroundFrameRenders', 'afterBackgroundRender', 'afterBackgroundRenders', 'afterFrameRender', 'afterFrameRenders', 'afterRecording', 'afterRender', 'afterRenders', 'afterReplay', 'allNodes', 'animation', 'animationEnd', 'animationIncrement', 'animationStart', 'animations', 'applyPreset', 'applyUserPreset', 'ask', 'askWithCancel', 'autoSaveDeleteFilter', 'autoSaveDeleteFilters', 'autoSaveFilter', 'autoSaveFilters', 'autoSaveRestoreFilter', 'autoSaveRestoreFilters', 'autolabel', 'autolabels', 'autoplace', 'autoplaceSnap', 'beforeBackgroundRender', 'beforeBackgroundRenders', 'beforeFrameRender', 'beforeFrameRenders', 'beforeRecording', 'beforeRender', 'beforeRenders', 'beforeReplay', 'cacheUsage', 'callbacks', 'canCreateNode', 'cancel', 'center', 'channels', 'choice', 'clearDiskCache', 'clearRAMCache', 'clone', 'cloneSelected', 'collapseToGroup', 'colorspaces', 'connectNodes', 'connectViewer', 'createNode', 'createScenefileBrowser', 'createToolset', 'critical', 'curveknob', 'curvelib', 'debug', 'defaultColorspaceMapper', 'defaultFontPathname', 'defaultLUTMappers', 'defaultNodeColor', 'delete', 'deletePreset', 'deleteUserPreset', 'deleteView', 'dependencies', 'dependentNodes', 'display', 'endGroup', 'env', 'error', 'execute', 'executeBackgroundNuke', 'executeInMain', 'executeInMainThread', 'executeInMainThreadWithResult', 'executeMultiple', 'executing', 'exists', 'expandSelectedGroup', 'expr', 'expression', 'extractSelected', 'filename', 'filenameFilter', 'filenameFilters', 'forceClone', 'forceLoad', 'fork', 'formats', 'frame', 'fromNode', 'geo', 'getAllUserPresets', 'getClipname', 'getColor', 'getColorspaceList', 'getDeletedPresets', 'getFileNameList', 'getFilename', 'getFonts', 'getFramesAndViews', 'getInput', 'getNodeClassName', 'getNodePresetExcludePaths', 'getNodePresetID', 'getOcioColorSpaces', 'getPaneFor', 'getPresetKnobValues', 'getPresets', 'getPresetsMenu', 'getReadFileKnob', 'getRenderProgress', 'getToolsetExcludePaths', 'getUserPresetKnobValues', 'getUserPresets', 'hotkeys', 'import_module', 'inputs', 'invertSelection', 'knob', 'knobChanged', 'knobChangeds', 'knobDefault', 'knobTooltip', 'layers', 'licenseInfo', 'load', 'loadToolset', 'localisationEnabled', 'localiseFiles', 'localization', 'makeGroup', 'math', 'maxPerformanceInfo', 'memory', 'menu', 'message', 'modified', 'nodeCopy', 'nodeDelete', 'nodePaste', 'nodes', 'nodesSelected', 'nuke', 'numvalue', 'oculaPresent', 'ofxAddPluginAliasExclusion', 'ofxMenu', 'ofxPluginPath', 'ofxRemovePluginAliasExclusion', 'onCreate', 'onCreates', 'onDestroy', 'onDestroys', 'onScriptClose', 'onScriptCloses', 'onScriptLoad', 'onScriptLoads', 'onScriptSave', 'onScriptSaves', 'onUserCreate', 'onUserCreates', 'openPanels', 'os', 'overrides', 'pan', 'performanceProfileFilename', 'pluginAddPath', 'pluginAppendPath', 'pluginExists', 'pluginInstallLocation', 'pluginPath', 'plugins', 'rawArgs', 're', 'recentFile', 'redo', 'removeAfterBackgroundFrameRender', 'removeAfterBackgroundRender', 'removeAfterFrameRender', 'removeAfterRecording', 'removeAfterRender', 'removeAfterReplay', 'removeAutoSaveDeleteFilter', 'removeAutoSaveFilter', 'removeAutoSaveRestoreFilter', 'removeAutolabel', 'removeBeforeBackgroundRender', 'removeBeforeFrameRender', 'removeBeforeRecording', 'removeBeforeRender', 'removeBeforeReplay', 'removeDefaultColorspaceMapper', 'removeFavoriteDir', 'removeFilenameFilter', 'removeFilenameValidate', 'removeKnobChanged', 'removeOnCreate', 'removeOnDestroy', 'removeOnScriptClose', 'removeOnScriptLoad', 'removeOnScriptSave', 'removeOnUserCreate', 'removeRenderProgress', 'removeUpdateUI', 'render', 'renderProgress', 'renderProgresses', 'rescanFontFolders', 'resetPerformanceTimers', 'restoreWindowLayout', 'resumePathProcessing', 'root', 'rotopaint', 'runIn', 'sample', 'saveEventGraphTimers', 'saveToScript', 'saveUserPreset', 'saveWindowLayout', 'scriptClear', 'scriptClose', 'scriptExit', 'scriptName', 'scriptNew', 'scriptOpen', 'scriptReadFile', 'scriptReadText', 'scriptSave', 'scriptSaveAndClear', 'scriptSaveAs', 'scriptSource', 'script_directory', 'scripts', 'selectAll', 'selectConnectedNodes', 'selectPattern', 'selectSimilar', 'selectedNode', 'selectedNodes', 'setPreset', 'setReadOnlyPresets', 'setUserPreset', 'show', 'showBookmarkChooser', 'showCreateViewsDialog', 'showDag', 'showInfo', 'showSettings', 'splayNodes', 'startEventGraphTimers', 'startPerformanceTimers', 'stopEventGraphTimers', 'stopPerformanceTimers', 'stripFrameRange', 'suspendPathProcessing', 'sys', 'tabClose', 'tabNext', 'tcl', 'thisClass', 'thisGroup', 'thisKnob', 'thisNode', 'thisPane', 'thisParent', 'thisView', 'threading', 'toNode', 'toggleFullscreen', 'toggleViewers', 'toolbar', 'tprint', 'traceback', 'types', 'undo', 'untitled', 'updateUI', 'updateUIs', 'usingOcio', 'usingPerformanceTimers', 'utils', 'validateFilename', 'validateFilenames', 'value', 'views', 'waitForThreadsToFinish', 'warning', 'zoom', 'zoomToFitSelected']

    # 获取全局属性
    print(nuke.root())
    # 返回所有选中节点实例的列表
    print(nuke.selectedNodes())
    # 返回名字为Write1的节点实例
    print(nuke.toNode("Write1"))
    # 返回当前节点实例
    print(nuke.thisNode())
    # 创建节点实例两种方案，NodeClass是节点类型，可以通过在具体节点上按i键或者通过Class()方法查看节点类型
    print(nuke.createNode("NodeClass"))
    print(nuke.nodes.NodeClass())
    # 返回某一类型所有节点实例列表
    print(nuke.allNodes("NodeClass"))
    # 返回所有插件路径
    print(nuke.pluginPath())

- Callback函数

.. code-block:: python

    nuke.addAfterRender()
    nuke.addOnUserCreate()
    nuke.addKnobChange()


- 节点实例对象属性与方法

nuke模块中有很多函数可以返回节点实例对象，下面是一些常用的函数。

.. code-block:: python

    nuke.selectedNodes()
    nuke.toNode()
    nuke.thisNode()
    nuke.createNode()
    nuke.nodes.Read()

有了节点实例对象就可以获取关于节点数据类型属性以及方法。

['Class', '__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__getitem__', '__hash__', '__init__', '__len__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'addKnob', 'allKnobs', 'autoplace', 'bbox', 'canSetInput', 'channels', 'clones', 'connectInput', 'deepSample', 'deepSampleCount', 'dependencies', 'dependent', 'error', 'fileDependencies', 'firstFrame', 'forceUpdateLocalization', 'forceValidate', 'format', 'frameRange', 'fullName', 'getNumKnobs', 'hasError', 'height', 'help', 'hideControlPanel', 'input', 'inputs', 'isLocalizationOutdated', 'isLocalized', 'isSelected', 'knob', 'knobs', 'lastFrame', 'linkableKnobs', 'localizationProgress', 'maxInputs', 'maxOutputs', 'maximumInputs', 'maximumOutputs', 'metadata', 'minInputs', 'minimumInputs', 'name', 'numKnobs', 'opHashes', 'optionalInput', 'performanceInfo', 'pixelAspect', 'proxy', 'readKnobs', 'redraw', 'removeKnob', 'resetKnobsToDefault', 'rootNode', 'running', 'sample', 'screenHeight', 'screenWidth', 'selectOnly', 'setInput', 'setName', 'setSelected', 'setTab', 'setXYpos', 'setXpos', 'setYpos', 'showControlPanel', 'showInfo', 'shown', 'treeHasError', 'upstreamFrameRange', 'width', 'writeKnobs', 'xpos', 'ypos']

.. code-block:: python

    # 返回节点类型
    node.Class()
    # 节点在节点网络中的位置相关方法
    setXYpos, setXpos, setYpos, xpos, ypos
    # 添加自定义参数
    addKnob

- 参数实例对象属性与方法

获取节点参数实例对象有下面两种常用的方法。

.. code-block:: python

    node["<parm_name>"]
    node.knob("<parm_name>")
    nuke.thisKnob()

有了节点参数实例对象就可以获取关于参数数据类型属性以及方法。

['Class', '__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'clearAnimated', 'clearFlag', 'critical', 'debug', 'enabled', 'error', 'evaluate', 'fromScript', 'fromUserText', 'fullyQualifiedName', 'getDerivative', 'getEvaluatedValue', 'getFlag', 'getIntegral', 'getKeyIndex', 'getKeyList', 'getKeyTime', 'getNthDerivative', 'getNumKeys', 'getText', 'getValue', 'getValueAt', 'hasExpression', 'isAnimated', 'isKey', 'isKeyAt', 'label', 'name', 'node', 'removeKey', 'removeKeyAt', 'setAnimated', 'setEnabled', 'setExpression', 'setFlag', 'setLabel', 'setName', 'setText', 'setTooltip', 'setValue', 'setValueAt', 'setVisible', 'splitView', 'toScript', 'tooltip', 'unsplitView', 'value', 'visible', 'warning']

.. code-block:: python

    # 返回参数类型
    parm.Class()
    # 读取写入操作相关方法
    getValue, getValueAt, setValue, setValueAt, value


----------------------
参考文档
----------------------

- https://www.foundry.com/products/nuke/developers
