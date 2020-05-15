==============================
Nuke偏好配置
==============================

- 自定义布局

调整好自己喜欢的窗口布局之后，点击菜单Workspace>Save Workspace...，给布局起个名字比如叫blablabla。

.. code-block:: python

    .nuke/Workspaces/Nuke/blablabla.xml

保存完成之后点击菜单Edit>Preferences>Behaviors>Startup>startup workspace>blablabla。

- 脚本编辑器

去勾选Edit>Preferences>Panels>clear input window on successful script execution选项，在执行完代码，代码就不会丢失。

- 临时文件

Edit>Preferences>Performance>Caching>temp directory修改临时文件路径

- 兼容路径

Edit>Preferences>General>Path Substitutions，支持OSX、Windows、Linux，这里配置了路径之后，节点上文件路径可以简写自动匹配。


