=========================================
Katana自定义工具架工具
=========================================

工具架工具有几个地方可以定义Shelf Actions，主菜单上的齿轮菜单、Scene Graph中的齿轮菜单、节点参数面板中的齿轮菜单。

点击齿轮菜单>Add>New Shelf>New Item，工具架工具会存储在下面路径。

C:\Users\<USERNAME>\.katana\Shelves

工具架的几个参数定义

.. code-block:: python

    """
    NAME: Set abcAsset Path
    ICON: icon.png
    KEYBOARD_SHORTCUT: 
    SCOPE:
    Enter Description Here

    """

每个工具架工具代码中开头都有这么一段配置脚本。

NAME即工具的名称，ICON设置工具图标，KEYBOARD_SHORTCUT设置工具的快捷方式。

图标文件在这里C:\Program Files\Katana3.5v2\bin\python\UI4\Resources\Icons

即$KATANA_HOME\bin\python\UI4\Resources\Icons

SCOPE限制特定节点类型，写描述。

我们可以在.katana/Shelves创建文件夹Custom_Shelves，然后创建一个firstShelfTool.py文件，写入如下内容。

.. code-block:: python

    """
    NAME: Float Selected
    ICON: Icons\Scenegraph\camera128.png
    KEYBOARD_SHORTCUT: T
    SCOPE: none
    Float Selected Nodes via Keyboard Shortcut
    """

    # Get list of selected nodes
    nodeList = NodegraphAPI.GetAllSelectedNodes()

    # Find Nodegraph tab and float nodes
    nodegraphTab = UI4.App.Tabs.FindTopTab("Node Graph")

    if nodegraphTab:
        nodegraphTab.floatNodes(nodeList)


- https://support.foundry.com/hc/en-us/articles/360001163884-Q100401-Creating-a-Shelf-Item-in-Katana
- https://support.foundry.com/hc/en-us/articles/360001235064
- https://learn.foundry.com/katana/content/tg/shelf_item_scripts/shelf_item_scripts.html?TocPath=Technical%20Information%7C_____5#User-def
