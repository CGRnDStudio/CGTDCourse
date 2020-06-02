=============================
Python内置模块：logging
=============================

.. code-block:: python

    >>> import logging
    >>> type(logging)
    <class 'module'>
    >>> logging.__file__
    'C:\\Python38\\lib\\logging\\__init__.py'
    >>> dir(logging)
    ['BASIC_FORMAT', 'BufferingFormatter', 'CRITICAL', 'DEBUG', 'ERROR', 'FATAL', 'FileHandler', 'Filter', 'Filterer', 'Formatter', 'Handler', 'INFO', 'LogRecord', 'Logger', 'LoggerAdapter', 'Manager', 'NOTSET', 'NullHandler', 'PercentStyle', 'PlaceHolder', 'RootLogger', 'StrFormatStyle', 'StreamHandler', 'StringTemplateStyle', 'Template', 'WARN', 'WARNING', '_STYLES', '_StderrHandler', '__all__', '__author__', '__builtins__', '__cached__', '__date__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__status__', '__version__', '_acquireLock', '_addHandlerRef', '_checkLevel', '_defaultFormatter', '_defaultLastResort', '_handlerList', '_handlers', '_levelToName', '_lock', '_logRecordFactory', '_loggerClass', '_nameToLevel', '_register_at_fork_reinit_lock', '_releaseLock', '_removeHandlerRef', '_showwarning', '_srcfile', '_startTime', '_str_formatter', '_warnings_showwarning', 'addLevelName', 'atexit', 'basicConfig', 'captureWarnings', 'collections', 'critical', 'currentframe', 'debug', 'disable', 'error', 'exception', 'fatal', 'getLevelName', 'getLogRecordFactory', 'getLogger', 'getLoggerClass', 'info', 'io', 'lastResort', 'log', 'logMultiprocessing', 'logProcesses', 'logThreads', 'makeLogRecord', 'os', 'raiseExceptions', 're', 'root', 'setLogRecordFactory', 'setLoggerClass', 'shutdown', 'sys', 'threading', 'time', 'traceback', 'warn', 'warning', 'warnings', 'weakref']
    >>>

.. code-block:: python

    import logging

    def main():
        logging.basicConfig(
            filename="app.log",
            level=logging.ERROR
        )
        hostname = "www.python.org"
        item = "spam"
        filename = "data.csv"
        mode = "r"

        logging.critical("Host %s unknown", hostname)
        logging.error("Couldn't find %r", item)
        logging.warning("Feature is deprecated")
        logging.info("Opening file %r, mode=%r", filename, mode)
        logging.debug("Got here")

    if __name__ == "__main__":
        main()

level是一个过滤器，critical error warning info debug代表不同的严重级别

.. code-block:: python

    logging.basicConfig(
        filename="app.log",
        level=logging.WARNING,
        format="%(levelname)s:%(asctime)s:%(message)s"
    )