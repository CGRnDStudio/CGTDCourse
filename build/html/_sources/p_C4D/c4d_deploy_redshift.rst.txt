=========================================
C4D部署Redshift
=========================================

C4D中部署Redshift非常简单，在安装Redshift的时候如果没有安装C4D或者自动配置环境的选项没有勾选，则C4D不会自动加载Redshift插件。后期部署Redshift也非常简单。这里假设你已经安装好了Redshift以及C4D R19，以管理员身份打开命令行窗口（切记以管理员身份运行）。

.. code-block:: python

    C:\Users\huweiguo>cd C:\ProgramData\Redshift\Plugins\C4D
    C:\ProgramData\Redshift\Plugins\C4D>install_c4d.bat R19 "C:\Program Files\MAXON\Cinema 4D R19\plugins"
