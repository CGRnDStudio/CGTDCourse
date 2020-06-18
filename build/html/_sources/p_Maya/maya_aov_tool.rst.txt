==============================
Maya AOV分层工具
==============================

AOV（Arbitrary Output Variables），可以通过Arnold Python API添加修改删除AOV。

.. code-block:: python

    import mtoa

    print(mtoa.__file__)
    print(type(mtoa))
    print(dir(mtoa))

    # ['__builtins__', '__doc__', '__file__', '__name__', '__package__', '__path__', 'aovs', 'api', 'callbacks', 'cmds', 'convertShaders', 'core', 'denoise', 'hooks', 'licensing', 'lightFilters', 'lightManager', 'makeTx', 'melUtils', 'renderToTexture', 'txManager', 'ui', 'utils']

    from mtoa import aovs

    aovName = "beauty"
    newAov = aovs.AOVInterface()
    print(dir(newAov))

    # ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_aovAttr', '_node', '_removeAOVNode', 'addAOV', 'getAOVNode', 'getAOVNodes', 'getAOVs', 'nextAvailableAttr', 'node', 'removeAOV', 'removeAOVs', 'renameAOVs']

    newAov.addAOV(aovName)
    print(help(newAov.addAOV))

    Help on method addAOV in module mtoa.aovs:

    addAOV(self, aovName, aovType=None, aovShader=None) method of mtoa.aovs.AOVInterface instance
        add an AOV to the active list for this AOV node
        
        returns the created AOV node

    None

addAOV方法有三个形参，两个缺省参数，所以至少传入aovName，aovType和aovShader可以缺省。

获取与移除AOV

.. code-block:: python

    from mtoa import aovs

    newAov = aovs.AOVInterface()
    allAovs = newAov.getAOVs()
    print(allAovs)
    newAov.removeAOVs(allAovs)
