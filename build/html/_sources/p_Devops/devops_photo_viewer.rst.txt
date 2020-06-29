=========================================
Win10调出照片查看器
=========================================

写一个注册表文件.reg，将下面的文本拷贝到其中保存之后运行合并即可。

.. code-block:: python

    Windows Registry Editor Version 5.00
    
     ; Change Extension's File Type
    
     [HKEY_CURRENT_USER\Software\Classes\.jpg]
    
     @="PhotoViewer.FileAssoc.Tiff"
    
     ; Change Extension's File Type
    
     [HKEY_CURRENT_USER\Software\Classes\.jpeg]
    
     @="PhotoViewer.FileAssoc.Tiff"
    
     ; Change Extension's File Type
    
     [HKEY_CURRENT_USER\Software\Classes\.gif]
    
     @="PhotoViewer.FileAssoc.Tiff"
    
     ; Change Extension's File Type
    
     [HKEY_CURRENT_USER\Software\Classes\.png]
    
     @="PhotoViewer.FileAssoc.Tiff"
    
     ; Change Extension's File Type
    
     [HKEY_CURRENT_USER\Software\Classes\.bmp]
    
     @="PhotoViewer.FileAssoc.Tiff"
    
     ; Change Extension's File Type
    
     [HKEY_CURRENT_USER\Software\Classes\.tiff]
    
     @="PhotoViewer.FileAssoc.Tiff"
    
     ; Change Extension's File Type
    
     [HKEY_CURRENT_USER\Software\Classes\.ico]
    
     @="PhotoViewer.FileAssoc.Tiff"