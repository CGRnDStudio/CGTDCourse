================================
Maya Redshift批量转贴图rstexbin
================================

在Redshift安装路径 ``C:\ProgramData\Redshift\bin`` 下找到redshiftTextureProcessor.exe，比如 ``D:\Texture`` 路径下有一批.jpg贴图需要转rstexbin，可以打开命令行窗口，写入下面的指令批量转换，有时候能解决贴图渲染卡住的问题。

.. code-block:: bash

    C:\ProgramData\Redshift\bin\redshiftTextureProcessor.exe D:\Texture\*.jpg
