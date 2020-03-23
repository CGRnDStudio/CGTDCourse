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

他们围绕着一个方法来控制路径查询机制，可以修改 ``C:\Users\{用户名}\.nuke\init.py`` 文件。

.. code-block:: python

    import nuke

    nuke.pluginAddPath("插件路径")

menu.py文件中一般写自定义菜单的代码，这样在Nuke启动的时候会自动加载菜单，而菜单中的执行的代码一般都是此文件夹下的模块或包的文件以及图标或Gizmo文件。
init.py文件主要用来处理路径问题，如果不想gizmo和icons中文件通过gizmo/xxx1.gizmo来处理的话，可以在init.py写入如下脚本。

.. code-block:: python

    import nuke

    nuke.pluginAddPath("gizmo")
    nuke.pluginAddPath("icons")
