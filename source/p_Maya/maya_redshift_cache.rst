==============================
Maya Redshift修改缓存路径
==============================

Maya Redshift插件默认缓存路径 ``%LOCALAPPDATA%\Redshift\Cache``，如果使用默认缓存路径，很快C盘空间就会爆掉，此处的LOCALAPPDATA是环境变量路径，可以通过命令行窗口输入下面指令得到路径。

.. code-block:: bash

    C:\Users\huweiguo>set LOCALAPPDATA
    LOCALAPPDATA=C:\Users\huweiguo\AppData\Local

    C:\Users\huweiguo>

在Maya渲染面板Render Settings中切换Redshift渲染选项，找到System>Global Preferences>Cache Folder，可以修改缓存文件夹路径。