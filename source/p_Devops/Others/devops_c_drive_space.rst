=========================================
C盘空间清理几个方案
=========================================

- SpaceSniffer

SpaceSniffer工具非常好用，可以很方便查看具体文件夹以及文件大小分布情况，从而可以知道哪些文件占用了磁盘空间。

- %tmp%

Windows系统中通过 ``Win+R`` 键打开运行面板，输入 ``%tmp%`` 确定可以打开C盘产生的临时文件，文件夹 ``C:\Users\{USERNAME}\AppData\Local\Temp`` 中的文件都可以删除，提示占用勾选全部跳过即可。

- Redshift

Redshift贴图缓存文件路径默认是在C盘 ``$LOCALAPPDATA\Cache``，如果不更改而使用，会逐渐占用很多C盘空间，建议设置在D盘路径或者定期清理，路径在 ``C:\Users\{USERNAME}\AppData\Local\Redshift\Cache``

- hiberfil.sys

hiberfil.sys是Windows系统休眠文件，往往占用很大的磁盘空间，如果你会重装系统就直接通过下面的命令关闭休眠功能，这样可以删除hiberfil.sys文件。

.. code-block:: bash

    powercfg -h off

重新启用休眠功能可以使用下面的指令。

.. code-block:: bash

    powercfg -h on
