==============================
Houdini VEX：点云函数
==============================


============== ================================================================
nearpoint()      # 查找离我最近的点，如果自己也在几何体中，则返回自己
nearpoints()     # 按范围查找最近的点，如果自己也在几何体中，数组中第一个元素是自己
neighbour()      # 查找
neighbours()     # 查找某一个点临近点 
============== ================================================================

新建Atttribute Wrangle创建随机点。

.. code-block:: python

    for (int i = 0; i < 1000; i++) {
        vector randPos = rand(i);
        // randPos.y = 0;
        addpoint(0, randPos);
    }

查找最近的两个点去连线。

.. code-block:: python

    int nearpt = nearpoints(0, @P, 1, 2)[1];

    if (@ptnum > nearpt) {
        addprim(0, "polyline", nearpt, @ptnum);
    }

查找附近多个点进行连线。

.. code-block:: python

    int nearpts[] = nearpoints(0, @P, 1, 10)[1:];

    foreach (int nearpt; nearpts) {
        if (@ptnum > nearpt) {
            addprim(0, "polyline", nearpt, @ptnum);
        }
    }

最简单的颜色通过小球来控制颜色传递。

.. code-block:: python

    int nearpt = nearpoint(1, @P, 0.5);

    if(nearpt != -1) {
        @Cd = {1, 0, 0};
    }

查找临近点。

.. code-block:: python

    int nbs[] = neighbours(0, @ptnum);

    foreach (int nb; nbs) {
        @Cd = v@Cd2;
        i@infected = 1;
    }


For Loop与Solver区别，For Loop循环不会继承前一帧的效果，Solver会继承上一帧的效果。

============== ================================================================
pcopen()
pcnumfound()
pciterate()
pcimport()
pcclose()
============== ================================================================

.. code-block:: python

    int handle = pcopen(0, "P", @P, 0.05, 10);
    i@num = pcnumfound(handle);




