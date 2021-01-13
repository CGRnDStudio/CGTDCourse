=============================
Python装饰器
=============================

Python装饰器的理论依据：Python中一切皆对象，函数也是对象。使用到Python闭包函数以及高阶函数的知识。


.. code-block:: python

    def fac(num):
        print("This is fac function!")
        return range(num)


    result = fac(6)
    print(result)

.. code-block:: python

    def fac(num):
        print("before")
        print("This is fac function!")
        print("after")
        return range(num)


    result = fac(6)
    print(result)


.. code-block:: python

    def fac():
        print("This is fac function!")
        return range(5)

    def mesause(func):
        def inner():
            func()
        return inner

    fac = mesause(fac)

    result = fac()
    print(result)


.. code-block:: python

    def fac():
        print("This is fac function!")
        return range(5)

    def mesause(func):
        def inner():
            res = func()
            return res
        return inner

    fac = mesause(fac)

    result = fac()
    print(result)

.. code-block:: python


    def mesause(func):
        def inner():
            print("before")
            res = func()
            return res
            print("after")
        return inner

    @mesause
    def fac():
        print("This is fac function!")
        return range(5)

    result = fac()
    print(result)


.. code-block:: python


    def mesause(func):
        def inner(*args, **kwargs):
            print("before")
            res = func(*args, **kwargs)
            return res
            print("after")
        return inner

    @mesause
    def fac():
        print("This is fac function!")
        return range(5)

    result = fac()
    print(result)

Python会自动执行mesause(fac)，执行完之后会将结果给到fac

相当于fac = mesause(fac)

Python高阶函数

Python闭包函数

Python装饰器函数传参

Python装饰器传参

类中的语法糖


.. code-block:: python

    import time


    def measure_time(func):

        def wrapped(*args, **kwargs):
            start = time.time()

            try:
                return func(*args, **kwargs)
            finally:
                runtime = time.time() - start
                print("Execution time: %.6f seconds" % runtime)

        return wrapped


    @measure_time
    def f():
        l = []
        for i in range(1000000):
            l.append(i)

    if __name__ == "__main__":
        f()




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