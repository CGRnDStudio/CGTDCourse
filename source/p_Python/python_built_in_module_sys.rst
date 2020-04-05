=============================
Python内置模块：sys
=============================

内置模块sys是用来描述与Python解释器密切相关的一些功能，而非操作系统的功能，操作系统相关功能都在内置模块os中，这也是两个模块主要区别。

.. code-block:: python

    >>> import sys
    >>>
    >>> type(sys)
    <type 'module'>
    >>> dir(sys)
    ['__displayhook__', '__doc__', '__excepthook__', '__name__', '__package__', '__stderr__', '__stdin__', '__stdout__', '_clear_type_cache', '_current_frames', '_getframe', '_git', 'api_version', 'argv', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_clear', 'exc_info', 'exc_type', 'excepthook', 'exec_prefix', 'executable', 'exit', 'exitfunc', 'flags', 'float_info', 'float_repr_style', 'getcheckinterval', 'getdefaultencoding', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'gettrace', 'getwindowsversion', 'hexversion', 'last_traceback', 'last_type', 'last_value', 'long_info', 'maxint', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'py3kwarning', 'setcheckinterval', 'setprofile', 'setrecursionlimit', 'settrace', 'stderr', 'stdin', 'stdout', 'subversion', 'version', 'version_info', 'warnoptions', 'winver']
    >>> 
    >>> sys.api_version
    1013
    >>> sys.executable
    'C:\\Python27\\python.exe'
    >>> sys.platform
    'win32'
    >>> sys.version
    '2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)]'
    >>> sys.version_info
    sys.version_info(major=2, minor=7, micro=14, releaselevel='final', serial=0)

* sys.argv
* sys.path
* sys.modules
* reload
