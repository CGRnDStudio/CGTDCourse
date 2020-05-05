==============================
Houdini VEX：组
==============================

VEX打组

@group_name

npointsgroup() // 返回组中有多少个点
nprimitivesgroup()
nverticesgroup()

.. code-block:: python

    if (@P.x > 0) {
        @group_up = 1;
    }


组函数

setpointgroup()

inpointgroup()

expandgroup() 以数组的形式返回组中元素
