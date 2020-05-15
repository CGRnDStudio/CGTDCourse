==============================
Maya如何获取拍屏面板参数？
==============================

optionVar命令可以获取一些Maya选项设置的参数

.. code-block:: python

    import maya.cmds as cmds

    for elem in cmds.optionVar(l=True):

        if "playblast" in elem.lower():
            print(elem)
            print(cmds.optionVar(q=elem))

通过上面的代码可以将与拍屏相关的参数筛选出来。

.. code-block:: python

    PlayblastCmdAvi

    PlayblastCmdFormatAvi

    PlayblastCmdFormatQuicktime

    PlayblastCmdQuicktime

    optionBoxDimensionsPlayblast
    [546L, 350L]
    playblastClearCache
    1
    playblastCompression
    H.264
    playblastDisplaySizeSource
    1
    playblastEndTime
    10.0
    playblastFile
    playblast
    playblastFormat
    qt
    playblastHeight
    256
    playblastMultiCamera
    0
    playblastOffscreen
    0
    playblastPadding
    4
    playblastQuality
    70
    playblastSaveToFile
    0
    playblastScale
    0.5
    playblastShowOrnaments
    1
    playblastStartTime
    1.0
    playblastUseSequenceTime
    0
    playblastUseStartEnd
    0
    playblastViewerOn
    1
    playblastWidth
    256

参数与具体option的对照表

========================  ===================================================
View:                      playblastViewerOn
Show ornaments:            playblastShowOrnaments
Render offscreen:          playblastOffscreen
Multi-Camera Output:       playblastMultiCamera
Format:                    playblastFormat
Encoding:                  playblastCompression
Quality:                   playblastQuality
Display size:              playblastWidth playblastHeight
Scale:                     playblastScale
Frame padding:             playblastPadding
Remove temporary files:    playblastClearCache
Save to file:              playblastSaveToFile
Movie file:                playblastFile
========================  ===================================================
