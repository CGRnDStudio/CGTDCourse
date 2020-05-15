==============================
Houdini VEX：可视化编程
==============================

方案一：通过PolyExtrude节点可视化数据。

- 创建一个Geometry。
- 创建一个Grid，Rows->100，Columns->100。
- 创建一个Attribute Wrangle。
- 创建一个Attribute Promote，Original Name->zscale，New Class->Primitive，Promotion Method->Maximum。
- 创建一个PolyExtrude，Divide Into->Individual Elements，Distance->1，Extrusion->Output Back，Local Control->Distance Scale。
- Attribute Wrangle节点中写入如下的代码可得到可视化结果。

.. code-block:: python

    f@zscale = @P.x;
    f@zscale = pow(@P.x, 2);
    f@zscale = sin(@P.x);
    f@zscale = floor(@P.x);
    f@zscale = frac(@P.x);
    f@zscale = abs(@P.x);
    f@zscale = abs(sin(@P.x));
    f@zscale = floor(sin(@P.x));
    f@zscale = pow(frac(@P.x), 2);

.. code-block:: python

    float temp = noise(@P);

    if (temp > 0.5) {
        f@zscale = 1;
    }

方案二：通过点颜色可视化数据。

.. code-block:: python

- 创建一个Geometry。
- 创建一个Grid，Rows->100，Columns->100。
- 创建一个Attribute Wrangle。

.. code-block:: python

    @Cd = {0, 0, 0};
    float temp = noise(@P);

    if (temp > 0.5) {
        @Cd.r = 1;
    }

- 创建一个Geometry。
- 创建一个Box。
- 创建一个。
- 创建一个Attribute Wrangle。

方案三：通过点位置可视化数据。

- 创建一个Geometry。
- 创建一个Line，Origin->-2.5, 0, 0，Direction->1, 0, 0，Length->5，Points->1000。
- 创建一个Attribute Wrangle。

.. code-block:: python

    @P.y = pow(@P.x);
