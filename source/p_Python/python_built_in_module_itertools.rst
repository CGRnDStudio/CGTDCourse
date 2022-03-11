=============================
Python内置模块：itertools
=============================

.. code-block:: python

    >>> import itertools
    >>> 
    >>> list(itertools.dropwhile(lambda i: i < 4, range(10)))
    [4, 5, 6, 7, 8, 9]
    >>> list(itertools.takewhile(lambda i: i < 4, range(10)))
    [0, 1, 2, 3]
    >>> list(itertools.ifilter(lambda x: x % 2, range(10)))
    [1, 3, 5, 7, 9]
    >>> list(itertools.ifilterfalse(lambda x: x % 2, range(10)))
    [0, 2, 4, 6, 8]
    >>> list(itertools.imap(lambda x, y: x + y, (2, 3, 10), (5, 2, 3)))
    [7, 5, 13]
    >>> list(itertools.starmap(lambda x, y: x + y, [(1, 2), (10, 20)]))
    [3, 30]

