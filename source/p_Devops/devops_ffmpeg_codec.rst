=========================================
FFmpeg批量转码工具
=========================================

.. code-block:: bash

    echo off
    M:
    cd M:\thirdParty\tools\ffmpeg\bin

    set OUTPUT_PATH=%1\build

    if not exist %OUTPUT_PATH% (
        md %OUTPUT_PATH%
    )

    for %%i in (%1\*.mov) do ffmpeg -i %%i -vcodec h264 -pix_fmt yuv420p -y %%~dpibuild\%%~ni.mov
    for %%i in (%1\*.mov) do echo %%~dpibuild\%%~ni.mov
    echo "Convert H.264 Successed!"
    echo "Output Path--->" %OUTPUT_PATH%
    pause
