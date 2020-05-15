==============================
Houdini模块：hou
==============================

Houdini中有多少Python模块可以使用，可以通过下面的代码获取。

.. code-block:: python

    >>> help("modules")

从获取的结果可以看出，Python可用的模块不止一个hou，还有其它模块如hutil、toolutils、husd、kramautils等，这些模块在帮助文档中并没有提到，只能从源代码docstring中查询一些帮助。

hou模块按功能可以分为三大类子模块（sub-modules）、类（classes）、函数（functions）。

* 子模块（sub-modules）：首字母小写，不带括号为module，module里面可能又有classes以及functions。
* 类（classes）：首字母大写，不带括号为class。class必须实例化使用，实例的属性以及方法必须通过实例化对象调用。
* 函数（functions）：首字母小写，带括号为function。

----------------------
子模块（sub-modules）
----------------------

* hou.hipFile

.. code-block:: python

    import hou

    # 获取当前的文件名
    hou.hipFile.basename()
    # 获取文件的完整路径
    hou.hipFile.name()
    # 新建文件
    hou.hipFile.clear()
    # 判断当前文件是否有未保存的修改
    hou.hipFile.hasUnsavedChanges()
    # 保存文件
    hou.hipFile.save("D:/scene.hip")
    # 将选择节点保存成文件

* hou.session
* hou.ui

.. code-block:: python

    import hou

    hou.ui.displayMessage("Hello world!!!")
    hou.ui.selectFile(title="Select Obj Directory", file_type=hou.fileType.Directory)

* hou.qt
* hou.hotkeys

----------------------
类（classes）
----------------------

* hou.Node

.. code-block:: python

    import hou

    hou.node("/obj").createNode("geo")


* hou.Parm

----------------------
函数（functions）
----------------------

.. code-block:: python

    import hou

    # 获取环境变量值
    hou.expandString("$HIPNAME")
    # 获取节点实例对象
    hou.node("/obj")
    # 获取所有选择节点
    hou.selectedNodes()
    # 获取所有的外链资产文件
    hou.fileReferences()
    # 获取当前节点实例对象
    hou.pwd()
    # 获取节点参数实例对象
    hou.parm()
    # 获取文档文件夹路径
    hou.homeHoudiniDirectory()
    # 获取软件版本
    hou.applicationVersion()
    # 获取软件版本字符串
    hou.applicationVersionString()
    >>> hou.setSimulationEnabled(0)
    >>> hou.setSimulationEnabled(1)

-------------------
案例代码
-------------------

* 获取当前帧范围

.. code-block:: python

    def getFrameRange(**kwargs):
        """
        getFrameRange will return a tuple of (fin, fout)
        :returns: Returns the frame range in the form (fin, fout)
        :rtype: tuple[int, int]
        """
        currentIn, currentOut = hou.playbar.playbackRange()
        return (currentIn, currentOut)

* 设置当前帧范围以及帧速率

.. code-block:: python

    def setFrameRange(fin=None, fout=None, **kwargs):
        """
        setFrameRange will set the frame range using `fin` and `fout`
        
        :param int fin: fin for the current context
            (e.g. the current shot, current asset etc)
        :param int fout: fout for the current context
            (e.g. the current shot, current asset etc)
        """
        hou.script("tset `((%s-1)/$FPS)` `(%s/$FPS)`" % (fin, fout))
        hou.playbar.setPlaybackRange(fin, fout)

-------------------
参考文档
-------------------

https://www.sidefx.com/docs/houdini/hom/index.html
https://www.sidefx.com/docs/houdini/hom/intro.html
https://www.sidefx.com/docs/houdini/hom/hou/index.html
