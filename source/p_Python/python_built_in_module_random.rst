=============================
Python内置模块：random
=============================

.. code-block:: python

    >>> import random
    >>> type(random)
    <class 'module'>
    >>> random.__file__
    'C:\\Python38\\lib\\random.py'
    >>> dir(random)
    ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_inst', '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
    >>>

=================== ===========================================================
random.choice()      # 从序列中随机挑选一个元素
random.randint()     # 给定范围随机整数
random.random()      # 随机0~1之间小数
=================== ===========================================================
