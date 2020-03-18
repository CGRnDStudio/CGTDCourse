=================================
Houdini中心化部署：Arnold渲染器
=================================

中心化部署也称集中式部署环境，集中式部署对于多台电脑的局域网环境是非常有利的，只要将Arnold渲染器部署到共享位置，通过环境变量来控制插件加载路径即可。

这意味着你可以将Arnold渲染器部署到任何位置，比如D盘。

在安装Arnold是时候可以自定义选择安装路径，尽量不要去拷贝文件夹到别的位置，如果不想改，默认用C盘安装路径也无不可。

在我的文档中找到需要安装Arnold渲染器的Houdini文件夹，比如houdini18.0，打开houdini.env文件，写入如下四句环境变量配置脚本即可。

.. code-block:: bash

    # htoa env
    HTOA = M:/thirdParty/htoa/htoa-5.1.0_r9289183_houdini-18.0.348/htoa-5.1.0_r9289183_houdini-18.0.348
    PATH = $PATH;$HTOA/scripts/bin
    solidangle_LICENSE = 5053@localhost

    # HOUDINI_PATH
    HOUDINI_PATH = $HTOA;&

如果houdini.env中配置了别的环境变量，注意将环境变量合并处理。
