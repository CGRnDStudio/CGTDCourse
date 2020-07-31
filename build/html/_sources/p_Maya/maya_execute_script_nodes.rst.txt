=====================================
Maya配置Execute script nodes
=====================================

在菜单File>Open打开文件的选项设置中有一项Execute script nodes，默认是勾选状态，它的意思是打开文件的时候执行文件中ScriptNode节点中的脚本，这也是普天同庆恶意脚本传播的原理，所以在清理完C盘相关文件之后，只要简单配置关闭这个选项就可以防止这个恶意脚本的传播。

我们找到文件C:\Users\huweiguo\Documents\maya\2018\prefs\userPrefs.mel，搜索fileExecuteSN，将1改为0保存即可。

.. code-block:: python

    -iv "fileExecuteSN" 0
