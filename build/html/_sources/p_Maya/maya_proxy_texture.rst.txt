==============================
Maya代理贴图获取方案
==============================

这里以Arnold ass代理和Redshift rs代理为例，我们如何获取它们的贴图路径。

我们知道代理的材质在导出之前就已经存在于代理文件中，不能通过节点参数获取。

.. code-block:: python

    import re
    import codecs


    def readFileCode_bag2(path):

        con = ""

        if os.path.exists(path):
            Arg = codecs.open(path, "r")
            con = Arg.read()
            Arg.close()

        return con

    getAllPath = []

    getAllRs = []
    getAllNodes = cmds.ls(type="RedshiftProxyMesh")

    tm = re.compile("(\\x00\\x00\\x00[A-Za-z]:/.*?\\x00)+")
    tm2 = re.compile("(\\x00\\x00\\x00//[0-9].*?\\x00)+")

    for node in getAllNodes:
        getPath = cmds.getAttr(node + ".fileName")

        if getPath and getPath not in getAllRs:
            getAllRs.append(getPath)

    for oneProxy in getAllRs:
        getCon = readFileCode_bag2(oneProxy)
        getResult = tm.findall(getCon)
        getResult2 = tm2.findall(getCon)

        for oneString in getResult:
            if oneString and "\\" not in oneString and "_map_auto" not in oneString and "/" in oneString:
                getPathMap = oneString.split("\x00\x00\x00")[1][:-1]
                if getPathMap and getPathMap not in getAllPath:
                    getAllPath.append(getPathMap)

        for oneString in getResult2:
            if oneString and "\\" not in oneString and "_map_auto" not in oneString and "/" in oneString:
                getPathMap = oneString.split("\x00\x00\x00")[1][:-1]
                if getPathMap and getPathMap not in getAllPath:
                    getAllPath.append(getPathMap)

    print(getAllPath)


