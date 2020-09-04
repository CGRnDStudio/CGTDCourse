==============================
Maya拍屏工具
==============================

.. code-block:: python

    import uuid
    import datetime
    import maya.cmds as cmds

    def playblast(path, cam, start, end, view=False):
        """
        """
        imagePath = os.path.expanduser("~/playblast")

        if not os.path.isdir(imagePath):
            os.makedirs(imagePath)

        imagePrefix = os.path.join(imagePath, "20200903_ABCDEF")
        print(imagePrefix)
        cmds.playblast(filename=imagePrefix,
                        format="image",
                        compression="tga",
                        width=1280,
                        height=720,
                        startTime=start,
                        endTime=end,
                        clearCache=1,
                        viewer=1,
                        showOrnaments=1,
                        fp=4,
                        percent=100,
                        quality=100)

    if __name__ == "__main__":
        playblast("", "persp", 1, 10)
