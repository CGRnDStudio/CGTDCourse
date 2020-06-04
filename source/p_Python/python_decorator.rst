=============================
Python装饰器
=============================

.. code-block:: python

    import logging


    def wrap_func_log(level="info"):
        LOG_LEVELS = {
            "debug": logging.debug,
            "info": logging.info,
            "warning": logging.warning,
            "error": logging.error
        }
        log_command = LOG_LEVELS.get(level) or logging.info

        def dec_wrapper(func):
            def wrapper(*args, **kwargs):
                log_command(func.__name__ + " is running...")
                return func(*args, **kwargs)
            return wrapper
        return dec_wrapper


    @wrap_func_log(level="error")
    def add1(n):
        print(n + 1)

    add1(10)