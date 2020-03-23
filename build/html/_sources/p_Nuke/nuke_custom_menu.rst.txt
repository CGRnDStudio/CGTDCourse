==============================
Nuke自定义菜单
==============================

Nuke自定义菜单是通过Python脚本来实现的，打开Windows>Script Editor查看nuke.menu帮助文档。

.. code-block::

    import nuke

    print(help(nuke.menu))

    # Result: Help on built-in function menu in module _nuke:

    menu(...)
        menu(name) -> Menu
        
        Find and return the Menu object with the given name. Current valid menus are:
        
        'Nuke'          the application menu
        'Pane'          the UI Panes & Panels menu
        'Nodes'         the Nodes toolbar (and Nodegraph right mouse menu)
        'Properties'    the Properties panel right mouse menu
        'Animation'     the knob Animation menu and Curve Editor right mouse menu
        'Viewer'        the Viewer right mouse menu
        'Node Graph'    the Node Graph right mouse menu
        'Axis'          functions which appear in menus on all Axis_Knobs.
        
        @param name: The name of the menu to get. Must be one of the values above.
        @return: The menu.
        @raise RuntimeError: if Nuke isn't in GUI mode.

    None

可以通过nuke.menu("Nuke")来获取菜单实例，再次查看实例对象的属性与方法。

.. code-block:: python

    mainMenu = nuke.menu("Nuke")
    print(dir(mainMenu))

    # Result: ['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'action', 'addAction', 'addCommand', 'addMenu', 'addSeparator', 'clearMenu', 'findItem', 'icon', 'invoke', 'items', 'menu', 'name', 'removeItem', 'script', 'setEnabled', 'setIcon', 'setScript', 'setShortcut', 'setVisible', 'shortcut', 'updateMenuItems']

其中addMenu方法可以在此菜单对象上添加一个菜单，返回此菜单的实例对象，addCommand可以添加一个执行命令的菜单。

.. code-block:: python

    toolMenu = mainMenu.addMenu("DO-VFX")
    toolMenu.addCommand("Choose Task", "print(100)", shortcut="t")

nuke.menu("Nuke")是主菜单的实例对象，如果想创建左侧工具栏工具，可以通过nuke.menu("Nodes")或者nuke.toolbar("Nodes")来获取实例对象。

.. code-block:: python

    import nuke

    toolbar = nuke.toolbar("Nodes")
    doToolbar = toolbar.addMenu("DO-VFX", "设置图标路径")
    doToolbar.addCommand("Choose Task", "print(100)")
