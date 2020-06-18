==============================
Maya命令行脚本
==============================

作为TD掌握命令行后台处理问题是及其重要的一项技能，大部分可执行程序都提供命令行执行参数，以便让计算机完成一些自动化工作。

- mayapy
- mayabatch
- maya
- render
- kick（arnold）

通过-h标签查看命令行各参数作用以及后台命令工作原理。

.. code-block:: python

    "C:\Program Files\Autodesk\Maya2016\bin\mayapy.exe" -h
    "C:\Program Files\Autodesk\Maya2018\bin\maya.exe" -h
    "C:\Program Files\Autodesk\Maya2018\bin\mayabatch.exe" -h
    "C:\Program Files\Autodesk\Maya2018\bin\Render.exe" -h

mayapy后面可以接.py文件运行，然后通过sys.argv来获取额外参数，比如写一个testMayapy.py，内容如下

.. code-block:: python

    import sys
    print(sys.argv)


模块文件后面跟的额外参数会以字符串的形式通过sys.argv打包成列表，这样我们可以传入一个Maya文件来分析贴图数据，效果是这样的，在命令行窗口检测Maya文件贴图数据是否丢失工具，打开命令行命令，输入

.. code-block:: python

    "C:\Program Files\Autodesk\Maya2016\bin\mayapy.exe" D:\centralizeTools\maya\env\2018\scripts\checkTools\relationship_check.py Z:\YYDTENN\Production\Department\LGT\EP01\sc006\YY_CG_sc006_lgt_color_v001_01.ma

.. code-block:: python

    #!/usr/bin/python
    # -*- coding: utf-8 -*-

    """
    This standalone maya script can be check out reference & texture relationship
    """

    import os
    import sys
    import logging
    import maya.standalone
    import maya.cmds as cmds
    maya.standalone.initialize()

    # logging.basicConfig(level=logging.WARNING, format="\nandy%(asctime)s - %(levelname)s - %(message)s\n")
    logging.basicConfig(format="%(asctime)s %(levelname)-8s %(message)s",
                        level=logging.WARNING, datefmt="%Y-%m-%d %H:%M:%S")


    def main(check_maya_file):
        """
        """
        if not os.path.isfile(check_maya_file):
            logging.warning("Failed because Maya file was not found! - %s" % check_maya_file)

        logging.info("START CHECK - %s" % check_maya_file)
        cmds.file(check_maya_file, open=True, pmt=False)
        logging.info("# Maya Version : %s" % cmds.about(v=True))
        # logging.info("# Arnold Version : %s" % cmds.pluginInfo("mtoa", q=True, v=True))

        # Check reference relationship
        for ref in cmds.file(q=True, r=True):
            refNode = cmds.referenceQuery(ref, referenceNode=True)
            logging.info("Check reference : %s" % refNode)
            # referenced_file = cmds.referenceQuery(reference, f=True, wcn=True)
            logging.info("Check reference path - %s" % ref)

            if not os.path.isfile(ref):
                logging.error("[!] The reference was not exists! : %s" % ref)

            if not cmds.referenceQuery(refNode, isLoaded=True):
                logging.error("[!] The reference was not loaded! : %s" % refNode)

            logging.info("> Check OK .")

        # Try to get "PROJECTWORKS" environment variable
        projectworks = os.environ.get("PROJECTWORKS", 0)

        if not projectworks:
            logging.error("The environment variable - \"PROJECTWORKS\" is undefined! Please to check out Maya.env file.")

        # Check texture file
        for texture in cmds.ls(type="file"):
            logging.info("Check Textures - %s" % texture)
            tex_name = cmds.getAttr(texture + ".fileTextureName")

            if not tex_name:
                logging.warning("The %s is no texture." % texture)
                continue

            logging.info("Check Texture Path - %s" % tex_name)

            if tex_name.startswith("$"):
                replace_name = tex_name.replace("$PROJECTWORKS", projectworks)
                tex_name = replace_name
            if not os.path.isfile(tex_name):
                logging.warning("The texture was not found! - %s" % tex_name)


    if __name__ == "__main__":
        main(sys.argv[1])

-------------------------------
参考文档
-------------------------------

- http://help.autodesk.com/view/MAYAUL/2020/ENU/
