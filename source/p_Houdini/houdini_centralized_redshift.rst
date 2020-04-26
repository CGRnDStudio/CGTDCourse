=================================
Houdini中心化部署：Redshift插件
=================================

中心化部署也称集中式部署环境，集中式部署对于多台电脑的局域网环境是非常有利的，只要将Redshift渲染器部署到共享位置，通过环境变量来控制插件加载路径即可。

这意味着你可以将Redshift渲染器部署到任何位置，比如D盘。

Redshift渲染器默认安装路径 ``C:\ProgramData\Redshift`` ，安装完可以将Redshift文件夹拷贝到D盘或者共享位置，如果不想改，默认用C盘安装路径也无不可。

在我的文档中找到需要安装Redshift渲染器的Houdini文件夹，比如houdini18.0，打开houdini.env文件，写入如下三句环境变量配置脚本即可。

.. code-block:: bash

    # Redshift env
    RS_PATH = C:/ProgramData/Redshift
    PATH = $PATH;$RS_PATH/bin

    HOUDINI_PATH = $RS_PATH/Plugins/Houdini/18.0.348;&

如果你想用共享位置的Redshift，假如现在有个M盘，我将Redshfit文件夹拷贝到M:\thirdParty\Redshift位置，就可以这样配置houdini.env。

.. code-block:: bash

    # Redshift env
    RS_PATH = M:/thirdParty/Redshift
    PATH = $PATH;$RS_PATH/bin

    HOUDINI_PATH = $RS_PATH/Plugins/Houdini/18.0.348;&

如果houdini.env中配置了别的环境变量，注意将环境变量合并处理。
