==============================
Maya开发环境
==============================
坐井观天：本节知识点
.mod
bat & vbs
模块导入流程
自定义菜单导入
自定义工具架导入


管中窥豹：延伸阅读

https://www.youtube.com/watch?v=18bMHq43K3U&t=2489s

如何制定一个module

环境变量管理

.mod文件
扩展工具层级结构

我的文档/modules
我的文档/scripts
我的文档/plug-ins

DO-VFX.mod

+ DO-VFX any \\server\manager\centralizeTools\maya\env\2018

icons
modules
plug-ins
scripts
shelves
Maya.env

.bat批处理

from pprint import pprint
import pymel.core as pm

pprint(dir(pm))
pprint(pm.language.Env.envVars.items())

坐井观天：本节知识点

分析资产
XGen
Reference
Texture
Fur
Proxy
Cache
Alembic
Assembly
Yeti
Qualoth
...
分析插件
Arnold
Redshift
分析渲染层
分析渲染设置

用户界面
正则表达式
上下文管理器
文件操作
字符编码
读写配置文件
XMLGenerator
json

如何来调试局部代码？

管中窥豹：延伸阅读


# optionVar设置首选项变量
import maya.cmds as cmds
cmds.optionVar(intValue=("defaultTriangles", 100))
cmds.optionVar(query="defaultTriangles")

# file文件操作
cmds.file(query=True, sceneName=True, shortName=True)

# getAttr & setAttr 属性读写操作
cmds.getAttr("defaultRenderGlobals.modifyExtension")

# listConnections & listRelatives 节点关联操作
cmds.listConnections("renderLayerManager.renderLayerId")

# 渲染层分析
def nzList(buf):
    if buf == None:
        return []
    return buf

def nzAnalyzeMayaGetAttr(layer, attr):
    attr = nzGetOverrideAttr(layer, attr)
    print(attr)
    return cmds.getAttr(attr, expandEnvironmentVariables = True)

def nzGetOverrideAttr(layer, attr):
    if layer == cmds.editRenderLayerGlobals(query = True, currentRenderLayer = True):
        return attr
    layers = cmds.listConnections('renderLayerManager.renderLayerId[0]')
    layers.insert(0, layer)
    buf = cmds.listConnections(attr, source = False, plugs = True, connections = True)
    for layer in layers:
        print(layer)
        print(buf)
        for i in range(1, len(nzList(buf)), 2):
            if re.search('^' + layer + r'\.adjustments\[\d+]\.plug$', buf[i]) != None:
                # print ('w:' + str(buf[i]) + re.sub(r'\.plug$', '.value', buf[i]))
                return re.sub(r'\.plug$', '.value', buf[i])
    return attr
    
renderLayers = cmds.listConnections('renderLayerManager.renderLayerId')

print(renderLayers)

for layer in renderLayers:
    renderer = nzAnalyzeMayaGetAttr(layer, 'defaultRenderGlobals.currentRenderer')
    print(renderer)


# error日志提醒
mom.MGlobal.displayError("File not existed!")
cmds.error("File not existed!")




# codecs
import codecs
def readFileContent(filePath):
    with codecs.open(filePath, "r", "utf-8") as f:
        lines = [line.strip() for line in f if line]
    return lines

