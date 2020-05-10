==============================
Nuke自定义节点参数
==============================

Nuke官方给了一些节点参数控件，可以通过简单添加来自定义节点参数。

- Floating Point Slider
- 2d Position Knob
- 3d Position Knob
- Width/Height Knob
- Bounding Box Knob
- Size Knob
- UV Coordinate Knob
- Integer Knob
- RGB Color Knob
- RGBA Color Knob
- Check Box
- TCL Script Button
- Python Script Button
- Python Custom
- Pulldown Choice
- Cascading Pulldown Choice
- Command Menu
- Text input Knob
- Filename
- Tab
- Group
- Text
- Divider Line
- Obsolete Knob

这些参数控件都非常简单，使用起来也很简单，只要创建过一次应该都可以上手掌握，但有几个细节值得注意:

- 我们往往会先创建一个Tab，将自定义创建的参数归类放在一起，默认直接创建knob会在User选项中，也可以后期修改User的命名。
- Hide可以隐藏参数控件。
- Python Custom会在显示节点参数的时候初始化代码，用于事件触发。
- Start new line可以让控件在不换行，比如并行两个Button。
- 参数关联。

创建一个NoOp， 右键参数菜单Manage User Knobs...>Add>Python Script Button...

Python Script Button中添加可执行代码。

