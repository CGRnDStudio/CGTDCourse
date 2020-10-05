=============================
Python内置模块：subprocess
=============================

.. code-block:: python

    >>> import subprocess
    >>> type(subprocess)
    <type 'module'>
    >>> dir(subprocess)
    ['CREATE_NEW_CONSOLE', 'CREATE_NEW_PROCESS_GROUP', 'CalledProcessError', 'MAXFD', 'PIPE', 'Popen', 'STARTF_USESHOWWINDOW', 'STARTF_USESTDHANDLES', 'STARTUPINFO', 'STDOUT', 'STD_ERROR_HANDLE', 'STD_INPUT_HANDLE', 'STD_OUTPUT_HANDLE', 'SW_HIDE', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '_active', '_args_from_interpreter_flags', '_cleanup', '_demo_posix', '_demo_windows', '_eintr_retry_call', '_subprocess', 'call', 'check_call', 'check_output', 'errno', 'gc', 'list2cmdline', 'msvcrt', 'mswindows', 'os', 'pywintypes', 'signal', 'sys', 'threading', 'traceback', 'types']
    >>>

.. code-block:: python

    import subprocess

    exePath = "C:/Python27/python.exe"

    pyFile = "D:/andy/tests_subprocess.py"

    commands = '"{0}" "{1}"'.format(exePath, pyFile)

    subprocess.check_call(commands)

.. code-block:: python

    import subprocess

    exePath = "C:/Program Files/Nuke10.5v1/Nuke10.5.exe"

    commands = '"{0}" --nukex'.format(exePath)

    subprocess.check_call(commands)

subprocess.check_call->会卡主程序

subprocess.check_output->会卡主程序，会返回一些结果

subprocess.Popen->独立程序，不会卡主程序
