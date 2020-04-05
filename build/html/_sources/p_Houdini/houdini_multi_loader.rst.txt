==============================
Houdini批量导入工具
==============================

.. code-block:: python

    import os

    obj_dir = hou.ui.selectFile(title="Select Obj Directory", file_type=hou.fileType.Directory)
    obj_dir_expanded = hou.expandString(obj_dir)

    obj_files = os.listdir(obj_dir_expanded)

    file_nodes = []
    loader = hou.node("/obj").createNode("geo", "OBJ_Loader")

    for obj in obj_files:
        obj_file_node = loader.createNode("file", obj)
        obj_file_node.parm("file").set(obj_dir + obj)
        obj_file_node.parm("missingframe").set(1)

        file_nodes.append(obj_file_node)

    merge_objs = loader.createNode("merge", "OBJ_Merger")

    for node in file_nodes:
        merge_objs.setNextInput(node)

    loader.layoutChildren()

    merge_objs.setDisplayFlag(True)
    merge_objs.setRenderFlag(True)
