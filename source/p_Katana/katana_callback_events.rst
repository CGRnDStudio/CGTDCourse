=========================================
Katana回调事件处理机制
=========================================

回调和事件在很多软件都是存在一种处理机制，回调是添加到Katana环境中的一段Python代码，当Katana中发生各种事件（例如创建节点或加载脚本）时，它会自动运行。事件是由于用户操作或其他来源（例如单击鼠标或按下键）而发生的操作。事件处理程序是用于处理事件的例程，允许程序员编写将在事件发生时执行的代码。

.. code-block:: python

    print(dir(Callbacks))
    print(dir(Callbacks.Type))
    # ['Type', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'addCallback', 'delCallback']
    # ['__doc__', '__module__', 'exportAsset', 'finalize3DNodeChanges', 'onGafferLightCreated', 'onGafferMasterMaterialCreated', 'onGafferRigCreated', 'onGafferShaderSelected', 'onLiveRenderCommand', 'onLiveRenderUpdate', 'onLookFileMaterialActiveSet', 'onLookFileMaterialSet', 'onMasterMaterialAssigned', 'onNewScene', 'onNodeCreate', 'onNodeDelete', 'onRenderSetup', 'onSceneAboutToLoad', 'onSceneLoad', 'onSceneSave', 'onShutdown', 'onStartup', 'onStartupComplete', 'onTabCreated', 'postLiveGroupPublish', 'postLookFileBake', 'preLiveGroupPublish', 'preLookFileBake']

.. code-block:: python

    def sayHello(**kwargs):
        for i in kwargs.keys():
            print(i)

    Callbacks.addCallback(Callbacks.Type.onSceneLoad, sayHello)
