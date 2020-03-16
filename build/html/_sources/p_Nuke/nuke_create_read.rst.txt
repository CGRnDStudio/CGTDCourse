==============================
Nuke Python创建Read节点小技巧
==============================

用过Nuke的童鞋都知道我们可以拖拽mov或者文件夹素材到Nuke的Node Graph中，它可以自动分类这些素材形成几个Read节点，并自动识别素材的帧数范围以及Metadata关于素材的所有信息。

那么在编写工具的时候如果遇到需要使用代码来创建Read节点并读取素材该怎么办呢？正常思维能想到的就是先创建Read节点，然后设置节点上的file参数，尝试过之后你会发现得不到你想要的结果。正确的方式是通过节点参数实例的fromUserText方法来实现。

我们先执行下面的代码看下fromUserText方法的定义

.. code-block:: python

    import nuke
    readNode = nuke.nodes.Read()
    print(help(readNode["file"].fromUserText))

执行完之后会得到下面的帮助文档

.. code-block:: python

    # Result: Help on built-in function fromUserText:

    fromUserText(...)
        self.fromUserText(s) -> None.
        Assign string to knob, parses frame range off the end and opens file to get set the format.
        @param s: String to assign.
        @return: None.

    None

意味着我需要传输素材的一个路径进去，比如一个mov，可以这样创建Read节点

.. code-block:: python

    import nuke

    movPath = r"D:\tests_nuke_read\XX_XXX_v001.mov"
    readNode = nuke.nodes.Read()
    readNode["file"].fromUserText(movPath)

你会发现和拖拽进来的素材丝毫不差，那么如果是exr序列呢？可以尝试将.mov改成####.exr或者%04d.exr，这样都得不到正确的结果，我们想获取到正确的序列，需要通过nuke.getFileNameList方法来解析一个文件夹中有哪些序列，如果一个文件夹中存在三套序列，它将返回一个三个元素组成的列表，类似下面这样

.. code-block:: python

    import nuke

    exrPath = r"D:\tests_nuke_read\render"
    print(nuke.getFileNameList(exrPath))
    # Result: ['BillowySmoke1.####.exr 700-1300', 'finalRender_Smoke_Right_bg.####.exr 1-200', 'qiangjiaohuo.####.exr 100-700']

其中每个元素的结尾都标明了对应序列的帧数范围，这样我们去创建Read节点就好办了，可以一次性创建三个Read节点

.. code-block:: python

    import nuke

    exrPath = r"D:\tests_nuke_read\render"
    seqs = nuke.getFileNameList(exrPath)

    for seq in seqs:
        seqPath = "%s/%s" % (exrPath, seq)
        readNode = nuke.nodes.Read()
        readNode["file"].fromUserText(seqPath)

完美