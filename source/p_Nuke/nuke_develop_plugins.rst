==============================
Nuke扩展开发插件的层级结构
==============================

扩展开发的层级结构大概如下：

.. code-block:: python

    package1
        __init__.py
        module1.py
    package2
        __init__.py
        module2.py
    gizmo
        xxx1.gizmo
        xxx2.gizmo
    icons
        xxx1.png
        xxx2.svg
    xxx1.gizmo
    xxx1.png
    module1.py
    module2.py
    init.py
    menu.py

他们围绕着一个方法来控制路径查询机制，可以修改C:\Users\{用户名}\.nuke\init.py文件。

.. code-block:: python

    import nuke

    nuke.pluginAddPath("插件路径")


