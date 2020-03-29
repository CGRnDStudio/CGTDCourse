=============================
Python推导
=============================

Python四种内建容器刚好对应有四种推导方式。

--------------
列表推导
--------------

.. code-block:: python

    myList = []

    for i in range(10):
        myList.append(i * 2)

.. code-block:: python

    myList = [i * 2 for i in range(10)]

--------------
生成器表达式
--------------

--------------
集合推导
--------------

--------------
字典推导
--------------

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