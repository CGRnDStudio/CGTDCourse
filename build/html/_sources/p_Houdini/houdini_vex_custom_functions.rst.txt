==============================
Houdini VEX：自定义函数
==============================

函数是编程语言中最简单的一种封装，函数最重要的是参数和返回值，参数又有形式参数（简称形参）与实际参数（简称实参）之分。

.. code-block:: python

    int test(int a, b; string c) {
        if (a > b) {
            printf(c);
        }
    }

.. code-block:: python

    function int[] nb(int ptnum) {
        pass
    }

.. code-block:: python

    int[] nb(int ptnum) {
        pass
    }

.. code-block:: python

    void createGeo(vector pos){
        int p0 = addpoint(geoself(), pos + {1, 0, 1});
        int p1 = addpoint(geoself(), pos + {1, 0, -1});
        int p2 = addpoint(geoself(), pos + {-1, 0, 1});
        int p3 = addpoint(geoself(), pos + {-1, 0, -1});
        int p4 = addpoint(geoself(), pos + {0, 1.5, 0});

        addprim(geoself(), "poly", p0, p1, p3, p2);
        addprim(geoself(), "poly", p2, p4, p0);
        addprim(geoself(), "poly", p0, p4, p1);
        addprim(geoself(), "poly", p1, p4, p3);
        addprim(geoself(), "poly", p3, p4, p2);
    }

    createGeo(chv("pos"));