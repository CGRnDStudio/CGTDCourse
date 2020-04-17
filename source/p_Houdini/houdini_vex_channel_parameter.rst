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

============== ====================== ====================
类型            HScript                VEX
int             ch                     chi()
float           ch                     chf()
string          ch                     chs()
vector                                 chv()
ramp            chramp                 chramp()
============== ====================== ====================

ch()通道函数默认类型是float，一般建议在VEX脚本中标明通道参数的具体类型。

.. code-block:: python

    float  chramp(string channel, float ramppos)

    float  chramp(string channel, float ramppos, float time)

    vector  chramp(string channel, float ramppos)

    vector  chramp(string channel, float ramppos, float time)

ramppos值域[0, 1]，任何可以区别开来的属性都可以借这个值域去映射，比如@ptnum / (@numpt - 1.0), sin(@ptnum), rand(@ptnum)。

---------------
参考文档
---------------

- http://www.sidefx.com/docs/houdini/ref/expression_cookbook
