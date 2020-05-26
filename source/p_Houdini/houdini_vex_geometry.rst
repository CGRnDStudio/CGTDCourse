==============================
Houdini VEX：几何体函数
==============================

=============== ====================================================
addpoint()       添加点到几何体
addvertex()      添加顶点到几何体上的面
addprim()        添加面到几何体

removepoint()    删除点
removeprim()     删除面
removevertex()   删除顶点
=============== ====================================================

使用add创建一个四角锥或者Attribute Wrangle创建一个四角锥，注意面法线方向。

.. code-block:: python

    int p0 = addpoint(geoself(), {1, 0, 1});
    int p1 = addpoint(geoself(), {1, 0, -1});
    int p2 = addpoint(geoself(), {-1, 0, 1});
    int p3 = addpoint(geoself(), {-1, 0, -1});
    int p4 = addpoint(geoself(), {0, 1.5, 0});

    addprim(geoself(), "poly", p0, p1, p3, p2);
    addprim(geoself(), "poly", p2, p4, p0);
    addprim(geoself(), "poly", p0, p4, p1);
    addprim(geoself(), "poly", p1, p4, p3);
    addprim(geoself(), "poly", p3, p4, p2);

.. code-block:: python

    if (@P.x < 0) {
        removepoint(geoself(), @ptnum);
    }

.. code-block:: python

    for (int i = 0; i < chi("num"); i++) {
        addpoint(geoself(), set(0, 0, i * chf("size")));
    }

setprimintrinsic()
setvertexpoint(0, 2, 0, 0);

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
