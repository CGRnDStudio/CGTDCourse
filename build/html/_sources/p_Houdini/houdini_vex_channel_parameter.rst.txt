==============================
Houdini VEX：通道参数
==============================

.. code-block:: python

    float dist = chf("dist");
    int num = chi("num");

    for (int n = 0; n < num; n++) {
        addpoint(0, set(n * dist, 0, 0));
    }

通道参数是Houdini本身就存在的一种自定义参数的方案，只不过这里用到了VEX代码中而已。

这里总结一些VEX关于通道的内置函数。

- ch()
- chi()
- chf()
- chs()
- chv()
- chramp()
