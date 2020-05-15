==============================
Nuke中心化配置插件
==============================

插件是否可以中心化，取决于插件是否按扩展开发的层级结构来处理，如果按照规范来开发的插件，可以通过修改 ``C:\Users\{用户名}\.nuke\init.py`` 文件来中心化插件。

.. code-block:: python

    import nuke

    nuke.pluginAddPath("插件路径")

举个例子，可以从网络上下载一个插件

https://github.com/Psyop/Cryptomatte

下载完将其解压到D盘，可以通过下面代码将插件部署到Nuke。

.. code-block:: python

    import nuke

    nuke.pluginAddPath("D:/Cryptomatte")