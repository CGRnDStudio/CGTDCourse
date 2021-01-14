=============================
Python装饰器
=============================

装饰器在Python中也称为语法糖，使用到的知识点是高阶函数与闭包函数，而高阶函数的依据是Python中一切皆对象，函数也是对象，所以装饰器也是以此为依据。

.. code-block:: python

    def myFunc():
        l = []

        for i in range(1000000):
            l.append(i)

        return l

    if __name__ == "__main__":
        myFunc()

.. code-block:: python

    import time


    def myFunc():
        l = []

        for i in range(1000000):
            l.append(i)

        return l

    if __name__ == "__main__":
        print("start...")
        start = time.time()
        myFunc()
        end = time.time()
        print("end...")
        print("execute time: %.6f" % (end - start))

.. code-block:: python

    import time


    def myFunc():
        print("start...")
        start = time.time()

        l = []

        for i in range(1000000):
            l.append(i)

        end = time.time()
        print("end...")
        print("execute time: %.6f" % (end - start))

        return l

    if __name__ == "__main__":
        myFunc()

.. code-block:: python

    import time


    def measureTime(fun):
        def wrapped():
            print("start...")
            start = time.time()

            result = fun()

            end = time.time()
            print("end...")
            print("execute time: %.6f" % (end - start))

            return result

        return wrapped


    def myFunc():
        l = []

        for i in range(1000000):
            l.append(i)

        return l

    if __name__ == "__main__":
        myFunc = measureTime(myFunc)
        myFunc()

.. code-block:: python

    import time


    def measureTime(fun):
        def wrapped():
            print("start...")
            start = time.time()

            result = fun()

            end = time.time()
            print("end...")
            print("execute time: %.6f" % (end - start))

            return result

        return wrapped


    @measureTime # Python会自动执行measureTime(myFunc)，执行完之后会将结果给到myFunc，相当于myFunc = measureTime(myFunc)
    def myFunc():
        l = []

        for i in range(1000000):
            l.append(i)

        return l

    if __name__ == "__main__":
        yFunc()


.. code-block:: python

    import time


    def measureTime(fun):
        def wrapped(*args, **kwargs):
            print("start...")
            start = time.time()

            result = fun(*args, **kwargs)

            end = time.time()
            print("end...")
            print("execute time: %.6f" % (end - start))

            return result

        return wrapped


    @measureTime
    def myFunc(num):
        l = []

        for i in range(num):
            l.append(i)

        return l

    if __name__ == "__main__":
        yFunc(1000000)


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
