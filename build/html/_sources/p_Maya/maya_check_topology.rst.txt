==============================
Maya检查拓扑结构
==============================

Maya Animation菜单中Deform>Blend Shape工具的原理就是依据两个物体的拓扑结构相同。

拓扑结构相同可以决定缓存融合，BlendShape变形方面的制作流程。

- 点数相同
- 面数相同
- 点与面的关系

.. code-block:: python

    # get model points
    import pymel.core as pm
    import maya.OpenMaya as om

    def getGeoPoints(geo):
        geoNode = pm.PyNode(geo)
        iter = om.MItMeshVertex(geoNode.__apiobject__())

        while not iter.isDone():
            print(iter.index())
            iter.next()

    if __name__ == "__main__":
        sels = pm.ls(sl=1)
        getGeoPoints(sels[0])

.. code-block:: python

    # set string io
    from StringIO import StringIO
    import pymel.core as pm
    import maya.OpenMaya as om

    def getGeoPoints(geo):

        pointsInfo = StringIO()
        geoNode = pm.PyNode(geo)
        iter = om.MItMeshVertex(geoNode.__apiobject__())

        while not iter.isDone():
            pointsInfo.write(str(iter.index()))
            pointsInfo.write("\n")
            # print(iter.index())
            iter.next()

        print(pointsInfo.getvalue())

    if __name__ == "__main__":
        sels = pm.ls(sl=1)
        getGeoPoints(sels[0])

.. code-block:: python

    # get face id
    from StringIO import StringIO
    import pymel.core as pm
    import maya.OpenMaya as om

    def getGeoPoints(geo):

        pointsInfo = StringIO()
        geoNode = pm.PyNode(geo)
        faceID = om.MIntArray()
        iter = om.MItMeshVertex(geoNode.__apiobject__())

        while not iter.isDone():
            iter.getConnectedFaces(faceID)
            pointsInfo.write(str(iter.index()))
            pointsInfo.write(" ")
            pointsInfo.write(" ".join([str(i) for i in faceID]))
            pointsInfo.write("\n")
            # print(iter.index())
            iter.next()

        print(pointsInfo.getvalue())

    if __name__ == "__main__":
        sels = pm.ls(sl=1)
        getGeoPoints(sels[0])

.. code-block:: python

    # check md5
    import md5
    from StringIO import StringIO
    import pymel.core as pm
    import maya.OpenMaya as om

    def getGeoPoints(geo):

        pointsInfo = StringIO()
        geoNode = pm.PyNode(geo)
        faceID = om.MIntArray()
        iter = om.MItMeshVertex(geoNode.__apiobject__())

        while not iter.isDone():
            iter.getConnectedFaces(faceID)
            pointsInfo.write(str(iter.index()))
            pointsInfo.write(" ")
            pointsInfo.write(" ".join([str(i) for i in faceID]))
            pointsInfo.write("\n")
            # print(iter.index())
            iter.next()

        return md5.new(pointsInfo.getvalue()).hexdigest()

    if __name__ == "__main__":
        sels = pm.ls(sl=1)
        print(getGeoPoints(sels[0]))
