================================
Houdini otls：创建以及更新的流程
================================

otl是一种老的数字资产的扩展名，现在扩展名是hda（Houdini Digital Assets），因为习惯就沿用了otl的名称。

Subnet自定义HDA方法
HOUDINI_PATH & HOUDINI_OTLSCAN_PATH
Operator Name & Operator Label
自定义参数齿轮菜单

内嵌资产是指将otl保存到Embedded，这样otl只会和场景文件一起存储，不会生成otl文件，一般是用于在正式创建资产之前测试数字资产，便于迭代和共享资产。

正常流程
Match Current Definition

Allow Editing of Contents

案例

创建一个pack cache的otl

要求能打包当前文件中所有filecache节点缓存，并生成新的hip文件

知识点

* 获取所有filecache节点
* 获取所有filecache节点上缓存路径
* 拷贝文件操作
* 修改所有filecache节点上缓存路径
* 保存成新的hip文件

.. code-block:: python

    # 获取某节点下的所有filecache节点
    import toolutils

    rootNode = hou.node("/")

    nodes = toolutils.findAllChildNodesOfType(rootNode, "filecache", dorecurse=True)

    # 获取所有filecache节点上缓存路径
    node.parm("file").eval()
    node.parm("file").unexpandedString()

Subnet自定义HDA方法
HOUDINI_PATH & HOUDINI_OTLSCAN_PATH
Operator Name & Operator Label
自定义参数齿轮菜单

参考文档：

https://www.sidefx.com/docs/houdini/assets/index.html
