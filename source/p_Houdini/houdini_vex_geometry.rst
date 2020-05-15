==============================
Houdini VEX：几何体函数
==============================

- int  addpoint(int geohandle, int point_number)
- int  addpoint(int geohandle, vector pos)

- int  removepoint(int geohandle, int point_number)
- int  removepoint(int geohandle, int point_number, int and_prims)

.. code-block:: python

    if (@P.x < 0) {
        removepoint(geoself(), @ptnum);
    }

    for (int i = 0; i < chi("num"); i++) {
        addpoint(geoself(), set(0, 0, i * chf("size")));
    }

几何体数据创建修改删除

创建
addpoint()

addvertex()

addprim()

修改
setprimintrinsic()
setvertexpoint(0, 2, 0, 0);

删除

removepoint()
removeprim()

primvertices()
primvertex()
primvertexcount()
primpoints()
primpoint()

pointprims()
pointvetices()
pointvertex()
vertexpoint()
vertexprev()
vertexnext()
vertexindex()
vertexprim()
vertexprimindex()

顶点序号

线性顶点序号

.. code-block:: python

    int lvt0 = pointvertex(0, 7);
    int lvt1 = pointvertex(0, lvt0);
    int lvt2 = pointvertex(0, lvt1);

    setvertexattrib(0, "Cd", -1, lvt0, {1, 0, 0});
    setvertexattrib(0, "Cd", -1, lvt1, {0, 1, 0});
    setvertexattrib(0, "Cd", -1, lvt2, {0, 0, 1});
