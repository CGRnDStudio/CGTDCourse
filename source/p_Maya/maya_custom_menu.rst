==============================
Maya自定义菜单
==============================


maya mod环境变量管理
MAYA_MODULE_PATH  扩展开发层级结构
Python模块加载的机制
PYTHONPATH在mod中的配置



DO-VFX.mod
+ DO-VFX any \\server\manager\centralizeTools\maya\env\2018

扩展开发层级结构
.\scripts 存放代码的地方，mel文件（userSetup.mel），py文件以包的形式管理

比如下面创建userSetup.mel文件来加载自定义菜单

.. code-block:: bash

    if (`menu -exists "menuDO"`){
        deleteUI -menu "menuDO";
    }

    menu -label "DO-VFX" -parent $gMainWindow -tearOff true "menuDO";
    menuItem -divider true -dividerLabel "General";
    menuItem -label "Choose Shot" -parent "menuDO" -command "print(1);";
    menuItem -label "Upload RV" -parent "menuDO" -command "print(1);";
    menuItem -label "Submit To Deadline" -parent "menuDO" -command "python(\"from submitJob import submitter;reload(submitter);submitter.main()\")";

    menuItem -divider true -dividerLabel "Step";
    menuItem -label "LAY" -parent "menuDO" -subMenu true -tearOff true "menuLay";
    menuItem -label "Bake Camera" -parent "menuLay" -command "BakeCamera;";

    menuItem -label "MOD" -parent "menuDO" -subMenu true -tearOff true "menuMod";
    menuItem -label "Batch Transfer UV" -parent "menuMod" -command "BatchTransferUV;";
    menuItem -label "Remove Duplicate Object Names" -parent "menuMod" -command "RemoveDuplicateObjectNames;";
    menuItem -label "Find Triangle Face" -parent "menuMod" -command "FindTriangleFace;";
    menuItem -label "Remove All Namespaces" -parent "menuMod" -command "RemoveAllNamespaces;";
    menuItem -label "Rock Generator" -parent "menuMod" -command "RockGenerator;";

    menuItem -label "ANM" -parent "menuDO" -subMenu true -tearOff true "menuAnm";
    menuItem -label "Anim Playblast Tool" -parent "menuAnm" -command "AnimPlayblastTool;";
    menuItem -label "Camera Shaker" -parent "menuAnm" -command "cameraShaker;";
    menuItem -label "Anim Smooth Keys" -parent "menuAnm" -command "oaSmoothKeys;";

    menuItem -label "LGT" -parent "menuDO" -subMenu true -tearOff true "menuLgt";
    menuItem -label "Reference LookDev" -parent "menuLgt" -command "python(\"from lookDev import referenceFile;reload(referenceFile);referenceFile.referenceLookdevFile()\")";
    menuItem -label "Create Rivet Locator" -parent "menuLgt" -command "rivetEX;";
    menuItem -label "Check Scene" -parent "menuLgt" -command "python(\"from checkScene import ZCheck_JBY;reload(ZCheck_JBY);ZCheck_JBY.CheckTheScene_UI();ZCheck_JBY.show()\")";
    menuItem -label "File Texture Manager" -parent "menuLgt" -command "FileTextureManager;";
    menuItem -label "Arnold AOV Creator" -parent "menuLgt" -command "tjh_Arnold_AOV_creator;";
    menuItem -label "Lost Textures Finder" -parent "menuLgt" -command "tjh_lost_textures_finder_Main;";
    menuItem -label "Vray Attributes Assigner" -parent "menuLgt" -command "tjh_vray_attributes_assigner_Main;";
    menuItem -label "Plant On Surface with Follicles" -parent "menuLgt" -command "tjh_plantOnSurface_withFollicles_Main;";
    menuItem -label "AOVs Arnold Masker" -parent "menuLgt" -command "AOVsArnoldMasker;";
    menuItem -label "Arnold ID" -parent "menuLgt" -command "ArnoldID;";
    menuItem -label "Arnold Masks" -parent "menuLgt" -command "ArnoldMasks;";
    menuItem -label "ASS Proxy Switch" -parent "menuLgt" -command "ASSProxySwitch;";
    menuItem -label "Batch View Render" -parent "menuLgt" -command "python(\"from batchViewRender import mainWin;reload(mainWin);mainWin.mayaRenderWindowRender();mainWin.checkSettings()\")";
    menuItem -label "Arnold Render Check" -parent "menuLgt" -command "python(\"from renderCheck import linearWorkflowCheck;reload(linearWorkflowCheck);linearWorkflowCheck.maya_ui()\")";


认识PYTHONPATH环境变量的作用

添加PYTHONPATH的几种方案
1、添加到系统环境变量或者用户环境变量
2、配置Maya.env文件
3、配置mod文件
4、配置启动文件去加载环境变量
5、抑或在使用的时候用sys.path添加

认识sys.path的作用
sys.path.append()
sys.path.insert()

py文件以包的形式存放在scripts文件夹中



