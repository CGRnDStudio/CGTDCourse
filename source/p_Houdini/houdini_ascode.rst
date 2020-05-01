=======================================
Houdini通过Python代码自定义节点参数
=======================================

.. code-block:: python

    node = hou.node("/out")

    mantra = node.createNode("ifd")

    #print(dir(mantra))
    #print(mantra.asCode())
    #
    #hou_parm_template = hou.ToggleParmTemplate("tpreframe", "tpreframe", default_value=True)
    #hou_parm_template_group.append(hou_parm_template)
    #hou_node.setParmTemplateGroup(hou_parm_template_group)

    exec_parm = mantra.parm("execute")
    print(exec_parm.asCode())
    print(exec_parm.parmTemplate().asCode())
