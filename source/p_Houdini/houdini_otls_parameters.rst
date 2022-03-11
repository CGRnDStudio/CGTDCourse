========================================
Houdini otls：自定义参数
========================================

otls上参数创建有三种方案：

* By Type
* From Nodes
* 拖拽参数

Name
Label
Type
Callback Script
Invisible
File Pattern
Horizontally Join to Next Parameter

Houdini创建otl的时候，想要将节点的参数面板做些布局，学会使用参数Folder的用法是比较有意思的。

Folder参数有以下几种类型模式：

- Collapsible # 加减号收缩与伸展
- Simple # 简单的框框
- Tabs # 选项卡式
- Radio Buttons # 和Tabs类似，多了一个Radio按钮显示
- Import Block 
- Multiparm Block (list) # 可以加减控件数量以列表的形式
- Multiparm Block (scrolling) # 可以加减控件数量以下拉滑条的形式
- Multiparm Block (tabs) # 可以加减控件数量以选项卡的形式

Ordered Menu>Menu Script

.. code-block:: python

    labels = ["Box", "Sphere", "Grid"]
    result = []

    for i, v in enumerate(labels):
        result.extend([i, v])

    return result

String>Menu

- Replace (Field + Single Selection Menu)
- Toggle (Field + Multiple Selection Menu)

Action Button

参考文档

https://www.sidefx.com/docs/houdini/assets/index.html
