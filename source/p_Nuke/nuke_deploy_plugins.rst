==============================
Nuke依据版本来加载不同插件
==============================

我们知道Nuke通常是通过此文件 ``C:\Users\{USERNAME}\.nuke\init.py`` 来添加插件路径。

.. code-block:: python

    import nuke

    nuke.pluginAddPath("插件1路径")
    nuke.pluginAddPath("插件2路径")

这里有个问题是不同的Nuke版本走的都是这个init.py文件来初始化插件工具，那么遇到不同版本中的插件该怎么办呢？

比如有个插件有两个版本，分别支持NukeX 10.5v1和NukeX 11.2v3，实际解决方案很简单，在加载前做个版本判断即可。

首先我们得知道通过什么来获取Nuke版本

.. code-block:: python

    import nuke

    for s in dir(nuke):

        if s.isupper():
            print(s, eval("nuke.%s" % s))

    # ('ADD_VIEWS', 0)
    # ('AFTER_CONST', 21)
    # ('AFTER_LINEAR', 22)
    # ('ALL', 1)
    # ('ALWAYS_SAVE', 1048576)
    # ('BEFORE_CONST', 19)
    # ('BEFORE_LINEAR', 20)
    # ('BREAK', 18)
    # ('CATMULL_ROM', 3)
    # ('CONSTANT', 1)
    # ('CUBIC', 4)
    # ('DISABLED', 128)
    # ('DONT_CREATE_VIEWS', 2)
    # ('DONT_SAVE_TO_NODEPRESET', 0)
    # ('DO_NOT_WRITE', 512)
    # ('ENDLINE', 8192)
    # ('EXE_PATH', 'C:/Program Files/Nuke10.5v1/Nuke10.5.exe')
    # ('EXPAND_TO_WIDTH', 0)
    # ('EXPRESSIONS', 1)
    # ('FLOAT', 5)
    # ('FONT', 4)
    # ('GEO', 16)
    # ('GUI', True)
    # ('HIDDEN_INPUTS', 4)
    # ('HORIZONTAL', 17)
    # ('IMAGE', 1)
    # ('INPUTS', 2)
    # ('INT16', 3)
    # ('INT8', 2)
    # ('INTERACTIVE', True)
    # ('INVALIDHINT', -1)
    # ('INVISIBLE', 1024)
    # ('KNOB_CHANGED_RECURSIVE', 134217728)
    # ('LINEAR', 2)
    # ('LOG', 4)
    # ('MATCH_CLASS', 0)
    # ('MATCH_COLOR', 2)
    # ('MATCH_LABEL', 1)
    # ('MONITOR', 0)
    # ('NODIR', 2)
    # ('NO_ANIMATION', 256)
    # ('NO_CHECKMARKS', 1)
    # ('NO_MULTIVIEW', 1073741824)
    # ('NO_POSTAGESTAMPS', False)
    # ('NO_UNDO', 524288)
    # ('NUKE_VERSION_DATE', 'Dec  6 2016')
    # ('NUKE_VERSION_MAJOR', 10)
    # ('NUKE_VERSION_MINOR', 5)
    # ('NUKE_VERSION_PHASE', '')
    # ('NUKE_VERSION_PHASENUMBER', 0)
    # ('NUKE_VERSION_RELEASE', 1)
    # ('NUKE_VERSION_STRING', '10.5v1')
    # ('NUM_CPUS', 48)
    # ('NUM_INTERPOLATIONS', 5)
    # ('PLUGIN_EXT', 'dll')
    # ('PREPEND', 8)
    # ('PROFILE_ENGINE', 3)
    # ('PROFILE_REQUEST', 2)
    # ('PROFILE_STORE', 0)
    # ('PROFILE_VALIDATE', 1)
    # ('PYTHON', 32)
    # ('READ_ONLY', 268435456)
    # ('REPLACE', 1)
    # ('REPLACE_VIEWS', 1)
    # ('SAVE_MENU', 33554432)
    # ('SCRIPT', 2)
    # ('SMOOTH', 0)
    # ('STARTLINE', 4096)
    # ('STRIP_CASCADE_PREFIX', 4)
    # ('TABBEGINCLOSEDGROUP', 2)
    # ('TABBEGINGROUP', 1)
    # ('TABENDGROUP', -1)
    # ('TABKNOB', 0)
    # ('THREADS', 48)
    # ('TO_SCRIPT', 1)
    # ('TO_VALUE', 2)
    # ('USER_SET_SLOPE', 16)
    # ('VIEWER', 1)
    # ('VIEW_NAMES', 'input/view_names')
    # ('WRITE_ALL', 8)
    # ('WRITE_NON_DEFAULT_ONLY', 16)
    # ('WRITE_USER_KNOB_DEFS', 4)

从代码获得的结果可以使用NUKE_VERSION_相关属性来获取当前NUKE版本。

.. code-block:: python

    # ('NUKE_VERSION_DATE', 'Dec  6 2016')
    # ('NUKE_VERSION_MAJOR', 10)
    # ('NUKE_VERSION_MINOR', 5)
    # ('NUKE_VERSION_PHASE', '')
    # ('NUKE_VERSION_PHASENUMBER', 0)
    # ('NUKE_VERSION_RELEASE', 1)
    # ('NUKE_VERSION_STRING', '10.5v1')

能获取Nuke当前使用的版本，init.py中加载插件代码就好处理了，不需要太精确就使用nuke.NUKE_VERSION_MAJOR，需要精确一些就用nuke.NUKE_VERSION_STRING。

.. code-block:: python

    import nuke

    ver = nuke.NUKE_VERSION_MAJOR

    if ver == 10:
        nuke.pluginAddPath("NukeX 10插件1路径")
        nuke.pluginAddPath("NukeX 10插件2路径")
    elif ver == 11:
        nuke.pluginAddPath("NukeX 11插件1路径")
        nuke.pluginAddPath("NukeX 11插件2路径")
    else:
        pass

.. code-block:: python

    import nuke

    ver = nuke.NUKE_VERSION_STRING

    if ver == "10.5v1":
        nuke.pluginAddPath("NukeX 10.5v1插件1路径")
        nuke.pluginAddPath("NukeX 10.5v1插件2路径")
    elif ver == "11.2v3":
        nuke.pluginAddPath("NukeX 11.2v3插件1路径")
        nuke.pluginAddPath("NukeX 11.2v3插件2路径")
    else:
        pass
