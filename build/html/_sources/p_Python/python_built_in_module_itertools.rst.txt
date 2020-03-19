=============================
Python内置模块：itertools
=============================

.. code-block:: python

    >>> import itertools
    >>> list(itertools.dropwhile(lambda i: i < 4, range(10)))
    >>> list(itertools.takewhile(lambda i: i < 4, range(10)))
    >>> list(itertools.ifilter(lambda x: x % 2, range(10)))
    >>> list(itertools.ifilterfalse(lambda x: x % 2, range(10)))
    >>> list(itertools.imap(lambda x, y: x + y, (2, 3, 10), (5, 2, 3)))
    >>> list(itertools.starmap(lambda x, y: x + y, [(1, 2), (10, 20)]))
