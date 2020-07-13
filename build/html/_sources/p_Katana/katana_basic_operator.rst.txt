=========================================
Katana基础操作
=========================================

默认视窗分为五大块: 渲染窗口、大纲窗口、三维视窗、节点编辑窗口和属性面板。

三维视窗的操作和Maya相同，非常简单，结合Alt+左中右键可以调整视窗，按F居中显示场景物体。

选中相应的物体可以通过W\E\R键来移动、旋转、缩放。

可以自定义视窗布局，通过Layouts>Save Current Layout保存自定义视窗。

在Node Graph窗口可以通过Tab来创建节点（也可以通过New菜单来创建节点）。

节点的左侧方格是在Scene Graph中显示，节点右侧方格是显示节点的属性面板，对应快捷键V和E。

修改节点名称可以通过属性面板修改或者选中节点按N键修改。

快捷键G可以将选中节点打组Group，Alt+G可以将选中节点打组GroupStack，可以使用Ctrl+鼠标中键或者Ctrl+Enter可以进组修改。

Node Graph>Edit>Fit Backdrop Node to Selected Nodes给节点归类添加Backdrop。

Viewer(Hydra)>Viewer>Monitor Layer: 视窗渲染

Viewer(Hydra)>Viewer>Monitor Layer Options>Display While Manipulating: 视窗实时监视渲染

Viewer(Hydra)>Viewer>Monitor Layer Options>Ignore Alpha: 视窗透明渲染

Scene Graph>Live Render Updates: 勾选需要实时渲染的选项。

常用一些节点解释

====================== ========================================================
节点类型                 节点描述
PrimitiveCreate         模型节点
Merge                   合并节点
Dot                     点节点
HierarchyCopy           复制节点
Transform3D             移动节点
CameraCreate            相机节点
Material                材质节点
MaterialAssign          材质赋予节点
GafferThree             灯光组节点
RenderSettings          渲染设置节点
DISettings              采样设置节点
Render                  渲染节点
====================== ========================================================

XGen毛发进Katana步骤

- [ ] 如何导入显示？
- [ ] 默认渲染器如何渲染？
- [ ] Katana中心化部署流程？
- [ ] Arnold如何渲染，配置与渲染？

文字Katana部署Arnold
文字Katana导入XGen流程
文字Katana中心化部署

-----------------------------
参考文档
-----------------------------


- https://rmanwiki.pixar.com/display/RFK/XGen+in+Katana
- https://docs.arnoldrenderer.com/display/A5KTN/Installation