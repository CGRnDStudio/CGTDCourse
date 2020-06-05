=========================================
Clarisse Python开发环境
=========================================

在Clarisse测试Python代码需要打开Script Editor和Log两个面板，Log面板中将会获取一些反馈结果。

或者选择菜单Layout>Presets>Scripting Workshop即可。

.. code-block:: python

    print(type(ix))
    # <type 'module'>
    print(dir(ix))
    # ['ApplicationSelection', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '_get_of_object', 'add_attribute', 'api', 'application', 'begin_command_batch', 'check_need_save', 'cmds', 'create_context', 'create_generic_object', 'create_object', 'delete_item', 'disable_command_history', 'disable_echo_command', 'enable_command_history', 'enable_echo_command', 'end_command_batch', 'export_context_as_project', 'export_geometries', 'export_geometry', 'export_render_archive', 'get_current_context', 'get_current_frame', 'get_item', 'import_geometries', 'import_geometry', 'import_image', 'import_images', 'import_map_file', 'import_map_files', 'import_project', 'import_scene', 'import_volume', 'import_volumes', 'inspect', 'is_context_exists', 'is_gui_application', 'is_interactive_application', 'is_process_application', 'item_exists', 'ix', 'load_project', 'log_error', 'log_info', 'log_warning', 'make_absolute_of_path', 'os', 'reference_export_context', 'reference_file', 'reference_make_local', 'render_image', 'save_bmp', 'save_exr16', 'save_exr32', 'save_image', 'save_jpg', 'save_png16', 'save_png8', 'save_project', 'save_tga', 'save_tif16', 'save_tif32', 'save_tif8', 'selection', 'set_current_context', 'set_current_frame']
    print(dir(ix.selection))
    # ['__doc__', '__getitem__', '__module__', 'add', 'deselect_all', 'get', 'get_contexts', 'get_count', 'get_objects', 'is_empty', 'select', 'select_all']
    print(ix.selection.get_count())
    # 获取当前选择物体的个数
    for i in range(ix.selection.get_count()):
        print(ix.selection[i])

Clarisse API文档在help>Contents>Reference>Scripting/API中，因为是从C++ API封装而来，大部分还是要看C++文档来写对应的Python代码。

.. code-block:: python

    for i in range(ix.selection.get_count()):
        sel = ix.selection[i]
        
        if sel.is_kindof("GeometryBox"):
            sel.attrs.scale[0] = 10
            sel.attrs.scale[1] = 10
            sel.attrs.scale[2] = 10
        else:
            print(ix.selection[i])

.. code-block:: python

    ix.cmds.CreateObject("box", "GeometryBox", "Global", "project://scene")
