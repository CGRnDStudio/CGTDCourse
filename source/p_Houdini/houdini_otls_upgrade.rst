=============================
Houdini otls：升级的两种方案
=============================

Houdini中otl的版本切换可以通过主菜单 Asset>Asset Manager>Configuration 设置 Asset Bar 为 Display Menu of All Definitions ，在每个otl参数面板即可看到 Asset Name and Path 的切换信息。

Houdini中想升级otl，在已经创建好的otl节点上右键选择 Show in Asset Manager... 菜单打开 Asset Manager 。

Asset Manager 对话框中在当前选择的节点上右键选择 Duplicate... 菜单，可以打开 Copy Asset 对话框。

这里升级otl有两种方案，推荐使用第一种。

第一种方案是在 Operator Name 上添加版本号， Operator Label 以及 Save to Library 保持不变。

比如：

.. code-block:: python

    do::pack_cache::1.0
    do::pack_cache::2.0

使用这种方案的好处是otl文件只有一个，两个版本都存储在此文件中，可以通过otl参数面板上的 Asset Name 来切换版本，默认优先使用的都是最新版本。

第二种方案是在 Save to Library 的时候将版本号添加到otl文件名上，保持 Operator Name 和 Operator Label 不变。这样做会另外存一个otl文件出来，相当于重新做了一个otl的方案。因为 Operator Name 是相同的，所以节点也只有一个，可以通过otl参数面板上的 Asset Path 来切换版本，默认优先使用的都是最新版本。


参考文档

https://www.sidefx.com/docs/houdini/assets/index.html
