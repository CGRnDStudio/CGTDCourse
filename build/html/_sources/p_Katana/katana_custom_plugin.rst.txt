=========================================
Katana自定义插件层级结构
=========================================

参考示例C:\Program Files\Katana3.5v2\plugins\Resources\Examples或者$KATANA_ROOT/plugins/Resources/Examples

- Args
- AssetPlugins
- Gaffer*
- GenericAssign
- Importmatic*
- Libs
- Macros
- Ops
- Plugins
- Python: 配置PYTHONPATH或通过Startup添加sys.path或直接在插件中添加sys.path。
- RenderBin
- Resolutions
- Shaders
- Shelves: 自定义主菜单工具架工具
- ShelvesNodeSpecific: 自定义节点参数面板工具架工具
- ShelvesScenegraph: 自定义Scene Graph面板工具架工具
- Startup: init.py自启动执行脚本
- SuperTools*
- Tabs*
- UIPlugins
- ViewerManipulators

- https://learn.foundry.com/katana/Content/ug/installation_licensing/katana_resources.html