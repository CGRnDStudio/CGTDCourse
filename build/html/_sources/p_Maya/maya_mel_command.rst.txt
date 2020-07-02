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

    cmds.parent(childObject, w=1)
    cmds.parent(cmds.ls(sl=1), n="newGrp")

世界坐标 & 物体坐标 (相对与绝对)

move & rotate & scale & xform

.. code-block:: python

    import maya.cmds as cmds

    cmds.move(0, 0, 0, object, r=1)

    cmds.rotate(0, 30, 0, object, a=1)

    cmds.scale(1, 1, 1, object, r=1)

    cmds.scale(1, 1, 1, object, a=1)

    cmds.xform(object, q=1, t=1)
    cmds.xform(object, t=(0, 0, 0))

    cmds.xform(object, q=1, ro=1)
    cmds.xform(object, ro=(0, 0, 0))

    cmds.xform(object, q=1, t=1, ws=1)
    cmds.xform(object, t=(0, 0, 0), ws=1)

    cmds.xform(object, q=1, ro=1, ws=1)
    cmds.xform(object, ro=(0, 0, 0), ws=1)

创建节点

.. code-block:: python

    import maya.cmds as cmds

    cmds.polySphere()
    cmds.circle()
    cmds.curve()
    cmds.joint(p=(0, 0, 0))
    cmds.createNode("joint")

获取节点类型与属性

.. code-block:: python

    import maya.cmds as cmds

    cmds.nodeType(object)
    cmds.listAttr(object)
    cmds.listAttr(object, k=1)
    cmds.listAttr(object, ud=1)
    cmds.getAttr()
    cmds.setAttr()
    cmds.setAttr(attribute, value, typ="string")

属性连接与断开

Windows>General Editors>Connection Editor

Windows>Node Editor

Windows>General Editors>Hypergraph: Hierarchy

Windows>General Editors>Hypergraph: Connections

查看节点技术文档

.. code-block:: python

    import maya.cmds as cmds

    cmds.connnectAttr(attr1, attr2)
    cmds.disconnectAttr(attr1, attr2)

    cmds.connnectAttr(attr1, attr2, f=1)
    cmds.connnectAttr("pCubeShape1.outMesh", "pSphereShape1.inMesh", f=1)

获取节点的连接

.. code-block:: python

    import maya.cmds as cmds

    # 上游节点
    cmds.listConnections(object, s=1, d=0)
    # 下游节点
    cmds.listConnections(object, s=0, d=1)
    # 节点属性
    cmds.listConnections(object, s=0, d=1, p=1)

-------------------
案例&练习
-------------------

- 经常我们会遇到Shape节点和模型命名不匹配的问题，如何批量重命名？
