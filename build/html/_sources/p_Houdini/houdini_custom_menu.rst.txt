==============================
Houdini自定义菜单
==============================

自定义菜单是一项必备的技能，而Houdini中扩展自定义菜单更是非常简单方便，Houdini中可以自定义菜单的地方有很多，文档举三个比较重要的案例，其它菜单扩展以此类推。

* MainMenuCommon.xml 自定义主菜单
* OPmenu.xml 自定义节点菜单
* PARMmenu.xml 自定义参数菜单

scriptArgs怎么用

自定义主菜单

.. code-block:: bash

    <MainMenu>
        <menuBar>
            <subMenu>
                <label></label>
                <scriptItem id=>
                    <label></label>
                    <scriptPath></scriptPath>
                    <scriptArgs></scriptArgs>
                </scriptItem>
                <scriptItem id=>
                    <label></label>
                    <scriptCode></scriptCode>
                    <scriptArgs></scriptArgs>
                </scriptItem>
            </subMenu>
        </menuBar>
    </MainMenu>

在Windows主菜单中添加子菜单

.. code-block:: bash

    <subMenu id="windows_menu">
        <subMenu id=>
            <label></label>
            <insertBefore/>
            <titleItem>
                <label></label>
            </titleItem>
            <>
        </subMenu>
    </subMenu>

可执行代码标签<scriptPath>或<scriptCode>

.. code-block:: bash

    <scriptCode><![CDATA[
    hou.ui.displayMessage("Hello World")
    ]]>
    </scriptCode>

.. code-block:: bash

    <scriptCode><![CDATA[
    def runLater():
        hou.ui.displayMessage("Hello World")

    import hdefereval
    hdefereval.executeDeferred(runLater)
    ]]>
    </scriptCode>

参考文档：

* https://www.sidefx.com/docs/houdini/basics/config_menus