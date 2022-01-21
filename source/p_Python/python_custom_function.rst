=============================
Python自定义函数
=============================

函数是Python内建的一种封装，我们把大段代码拆成函数，通过一层一层的函数调用，就可以把复杂的任务分解成简单的任务，这种分解称为面向过程的程序设计。函数就是面向过程的程序设计的基本单元。Python提供了很多内置函数，比如print()，你也可以自己创建函数，这被叫做自定义函数。

函数的几个概念

- 基本语法

.. code-block:: python

    def 函数名(形式参数):
        函数体
        return 返回值

形式参数和返回值不是必须的，但函数都是有返回值的，如果没有使用关键字return关键字，则函数默认返回None。

- 形式参数(形参)

- 实际参数(实参)

- 返回值

形参的几种形式

- 缺省参数，又叫默认参数

- 可变参数 ``*args`` 

``*args`` 表示可变参数，就是传入的参数个数是可变的，可以是1个，2个到任意个或者0个。其实就是将传入的一堆参数打包成元组使用。

- 关键字参数 ``**kwargs``

``**kwargs`` 将传入的0个或者多个含参数名的参数打包成字典使用。

- 不同形式参数之间组合

作用域

在函数外部，locals()和globals()作用完全相同。而当在函数内部调用时，locals()则是获取当前函数堆栈中的名字空间，其中存储的是函数参数、局部变量等信息。

.. code-block:: python

    >>> locals()
    {'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
    >>> globals()
    {'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
    >>> locals() is globals()
    True
    >>> def func(a):
    ...     b = a % 2
    ...     print(locals())
    ...     print(locals() is globals())
    ...
    >>> func(5)
    {'a': 5, 'b': 1}
    False
    >>> locals() is globals()
    True

.. code-block:: python

    def f(arg1, arg2, arg3):
        print(arg1, arg2, arg3)
        
    def f(*args):
        print(type(args))
        print(args)
        
    f(3, 2, 1)

    def f(**kwargs):
        print(type(kwargs))
        print(kwargs)
        
    f(name="Andy", lang="Chinese")

    def f(*args, **kwargs):
        print(args)
        print(kwargs.items())

    f(1, 2, name="Andy", lang="Chinese")

    def setParms(**kwargs):

        for k,v in kwargs.items():
            print("Setting parameter {0} to {1}".format(k,v))
            
    setParms(streng=13, resistance=0.7, weigh=100)

    return

    def double_parm(**kwargs):
        return kwargs["weigh"] * 2

    print(double_parm(streng=13, resistance=0.7, weigh=100))

函数赋值

.. code-block:: python

    def double_parm(**kwargs):
        return kwargs["weigh"] * 2, kwargs["streng"]

    new_func = double_parm

    print(new_func(streng=13, resistance=0.7, weigh=100))

函数中套函数

.. code-block:: python

    def double_parm(**kwargs):
        
        def check(weight):
            if weight < 100:
                return False
            else:
                return True

        if check(kwargs["weigh"]):
            return kwargs["weigh"] * 2, kwargs["streng"] * 2
        else:
            return kwargs["weigh"] * 2, kwargs["streng"] * 4

    new_func = double_parm

    print(new_func(streng=13, resistance=0.7, weigh=60))

    import os
    from sys import version

    PATH = "/tmp/folder/name"


    # def localFunc():
    #     global version
    #     version = 13.3
    #     print("Local version", version)

    # localFunc()
    # print(version)


    # def getTempContent():
    #     tempdir = os.listdir("C:/")

    # getTempContent()
    # print(tempdir)


    def func1():
        print(mvar)
        print(PATH)


    def funcBase():
        mvar = 15
        func1()

    funcBase()

默认值（缺省值）对函数重载的作用

len多态函数

len("andy")
len(range(10))

运算符重载多态性
100 + 200
"hello " + "python"

Python函数没有重载的概念主要是因为动态语言特性以及缺省值

.. code-block:: python

    def function(args):
        code
        return

    def foo():
        print("this is function")

    foo()

    # 形式参数
    def sayHello(name):
        print("hello, ", name)

    sayHello("andy")

    # 缺省参数

    def sayHello(name="andy"):
        print("hello, ", name)

    sayHello()

    # 形式参数>缺省参数>*args>**kwargs
    # 可变参数
    def sayHello(*names):
        print(names)

    sayHello("andy", "tommy")

    # 顺序传参，关键字传参
    def foo(a, b, c):
        print("a is ", a)
        print("b is ", b)
        print("c is ", c)

    foo(1, 2, 3)
    foo(a=1, b=2, c=3)
    foo(b=2, c=3, a=1)
    foo(1, c=3, b=2)

    def sayHello(**names):
        print(names, type(names))

    sayHello(name="andy", age=30)

    def foo(a, b=1, *args, **kwargs):
        pass

    # 返回值
    def foo():
        return 5

    a = foo()
    print(a)

    def foo(a):
        if a < 0:
            return
        return 100 + a

    foo(9)
    foo(-9)
