==============================
Houdini接口hou模块
==============================

hou模块可以分为三大类sub-modules、classes、functions。

* sub-modules：首字母小写，不带括号为module，module可能又有classes以及functions。
* classes：首字母大写，不带括号为class。class必须实例化使用，class的属性以及方法必须通过实例化对象调用。
* functions：首字母小写，带括号为function。

Houdini Python API不止一个hou模块，还有其它模块在安装路径$HFS\houdini\python2.7libs，如hutil、toolutils、husd、kramautils等，这些模块在帮助文档中并没有提到，只能从源代码docstring中查询一些帮助。

抑或通过下面三个内置函数的通用心法来使用：

* type() # 查看对象的类型
* dir() # 查看对象的属性与方法
* help() # 查看具体方法的帮助

-------------------
sub-modules
-------------------

# hou.hipFile

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
    

-------------------
functions
-------------------

.. code-block:: python

    import hou

    # 获取环境变量值
    hou.expandString("$HIPNAME")
    # 获取节点实例对象
    hou.node("/obj")
    # 获取所有选择节点
    hou.selectedNodes()



-------------------
举例
-------------------

.. code-block:: python

    # 函数
    hou.node()
    hou.selectedNodes()
    hou.fileReferences()
    hou.pwd()
    hou.parm()
    hou.homeHoudiniDirectory()
    hou.applicationVersion()
    hou.applicationVersionString()
    hou.homeHoudiniDirectory()
    # 模块
    hou.session
    hou.ui
    hou.qt
    # 类
    hou.Node
    hou.Parm
    hou.Color

-------------------
案例
-------------------

.. code-block:: python

    # 获取当前帧范围
    def getFrameRange(**kwargs):
        """
        getFrameRange will return a tuple of (fin, fout)
        :returns: Returns the frame range in the form (fin, fout)
        :rtype: tuple[int, int]
        """
        currentIn, currentOut = hou.playbar.playbackRange()
        return (currentIn, currentOut)

.. code-block:: python

    # 设置当前帧范围以及帧速率
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

.. code-block:: python

    import toolutils

    scene_viewer = toolutils.sceneViewer()
    selected_objects = scene_viewer.selectObjects("Select a camera and press Enter", allowed_types = ["cam"])
    print(selected_objects)

案例：将某个文件夹中所有abc导入到Houdini中。

.. code-block:: python

    pass

-------------------
参考文档
-------------------

https://www.sidefx.com/docs/houdini/hom/index.html
https://www.sidefx.com/docs/houdini/hom/hou/index.html
https://www.sidefx.com/docs/houdini/hom/intro.html
https://www.sidefx.com/docs/houdini/hom/hou/Node.html
https://www.sidefx.com/docs/houdini/hom/hou/Parm.html
https://www.sidefx.com/docs/houdini/hom/hou/hipFile.html
https://www.sidefx.com/docs/houdini/hom/hou/ui.html