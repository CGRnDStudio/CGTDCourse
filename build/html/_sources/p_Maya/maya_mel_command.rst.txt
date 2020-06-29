==============================
Maya MEL常用命令
==============================

ls命令

.. code-block:: python

    import maya.cmds as cmds

    cmds.ls()

    cmds.ls(sl=1)

    cmds.ls(typ=["mesh", "lambert"], l=1)

    cmds.ls(et="transform")

    cmds.ls(et="lambert")

    cmds.ls(ext="transform")

    cmds.ls("blendShape*")

    cmds.ls("blendShape?Set")

    cmds.ls("UUID")

rename命令

.. code-block:: python

    import maya.cmds as cmds

    cmds.rename(oldName, newName)

节点的层级关系

listConnections & listRelatives

.. code-block:: python

    import maya.cmds as cmds

    cmds.listRelatives(object, p=1)
    cmds.listRelatives(object, c=1)
    cmds.listRelatives(object, ad=1)
    cmds.listRelatives(object, ad=1, typ="joint", f=1)

parent & group

.. code-block:: python

    import maya.cmds as cmds

    cmds.parent(childObject, parentObject)

-------------------
案例&练习
-------------------

- 经常我们会遇到Shape节点和模型命名不匹配的问题，如何批量重命名？
