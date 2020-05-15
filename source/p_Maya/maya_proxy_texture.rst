==============================
Maya代理文件贴图获取方案
==============================

获取Redshift渲染器rs代理文件所有贴图路径代码:

.. code-block:: python

    import re
    import codecs
    from pprint import pprint

    import maya.cmds as cmds

    def readFileCode_bag2(path):

        con = ""

        if os.path.exists(path):
            Arg = codecs.open(path, "r")
            con = Arg.read()
            Arg.close()

        return con

    getAllRs = []
    getAllNodes = cmds.ls(type="RedshiftProxyMesh")

    tm = re.compile("(\\x00\\x00\\x00[A-Za-z]:/.*?\\x00)+")
    tm2 = re.compile("(\\x00\\x00\\x00//[0-9].*?\\x00)+")

    for node in getAllNodes:
        getPath = cmds.getAttr(node + ".fileName")

        if getPath and getPath not in getAllRs:
            getAllRs.append(getPath)

    for oneProxy in getAllRs:
        getAllPath = []
        print(oneProxy)
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

        pprint(getAllPath)

获取Arnold渲染器ass代理文件所有贴图路径代码:

.. code-block:: python

    from pprint import pprint
    import maya.cmds as cmds

    import arnold as ar


    # 分析ass代理文件贴图路径
    getAllAss = []
    getAllNodes = cmds.ls(type="aiStandIn")

    for node in getAllNodes:
        getPath = cmds.getAttr(node + ".dso")

        if getPath and getPath not in getAllAss:
            getAllAss.append(getPath)

    for ass in getAllAss:
        getAllPath = []
        print(ass)
        ar.AiBegin()
        ar.AiMsgSetConsoleFlags(ar.AI_LOG_ALL)
        ar.AiASSLoad(ass, ar.AI_NODE_ALL)
        iterator = ar.AiUniverseGetNodeIterator(ar.AI_NODE_ALL)

        while not ar.AiNodeIteratorFinished(iterator):
            node = ar.AiNodeIteratorGetNext(iterator)

            if ar.AiNodeIs(node, "MayaFile") or ar.AiNodeIs(node, "image"):
                getPath = ar.AiNodeGetStr(node, "filename")

                if getPath and getPath not in getAllPath:
                    getAllPath.append(getPath)

        ar.AiNodeIteratorDestroy(iterator)
        ar.AiEnd()
        pprint(getAllPath)
