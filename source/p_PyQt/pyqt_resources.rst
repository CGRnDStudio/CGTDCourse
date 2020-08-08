=============================
PyQt设置图标的相对路径
=============================

- 编译qrc相对路径

创建resource.qrc
"C:\Python27\Scripts\pyside-uic.exe" -o deploy.py deploy.ui
"C:\Python27\Lib\site-packages\PySide\pyside-rcc.exe" -o resource_rc.py resource.qrc
