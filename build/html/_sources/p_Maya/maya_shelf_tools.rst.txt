==============================
Maya自定义工具架工具
==============================



load shelf

自定义工具架
自定义工具架工具

1.鼠标中键拖拽代码
2.Ctrl+Shift+鼠标左键点击菜单

Shelf Editor

Shelves
Command
Double Click Command
Popup Menu Items


loadNewShelf

import pymel.core as pm

if not pm.shelfLayout(shelfName, q=True, ex=True)
