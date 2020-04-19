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
