=======================================
Python特殊属性：__file__ & __path__
=======================================

__file__是模块对象的特殊属性，它会返回模块文件的完整路径，如果模块是包的话，则返回包的__init__.py的完整路径。这在工作中非常实用，比如我自定义了一个命名污染的模块platform.py，在使用的时候一直报错，就可以通过代码查找此模块的路径，就会发现系统已经存在这个模块，是因为导入的不是我写的这个模块导致的错误，很多时候很方便检查代码在什么地方。

.. code-block:: python

    >>> import platform
    >>> platform.__file__
    'C:\\Python27\\lib\\platform.pyc'

__path__是模块包的特殊属性，它会返回模块包的文件夹完整路径。

.. code-block:: python

    >>> import PySide
    >>> PySide.__file__
    'C:\\Python27\\lib\\site-packages\\PySide\\__init__.pyc'
    >>> PySide.__path__
    ['C:\\Python27\\lib\\site-packages\\PySide']



__file__
__name__


import random

class Point(object):
    def __init__(self, dist_from_origin, weight):
        self.dist = dist_from_origin
        self.weight = weight
        
    def __repr__(self):
        return "Point dist: %f; weight: %f" % (self.dist, self.weight)
    
def getPointList(numPoints, maxDist):
    l = []
    n = 0
    while n <= numPoints:
        dist = random.random()
        random.seed()
        weight = random.uniform(0.01, 0.1)
        if dist <= maxDist:
            l.append(Point(dist, weight))
            n += 1
    return l

print(getPointList(100, 0.17))


import random

class Point(object):
    def __init__(self, dist_from_origin, weight):
        self.dist = dist_from_origin
        self.weight = weight
        
    def __repr__(self):
        return "Point dist: %f; weight: %f" % (self.dist, self.weight)
    
@measure_time
def getPointList(numPoints, maxDist):
    l = []
    n = 0
    while n <= numPoints:
        dist = random.random()
        random.seed()
        weight = random.uniform(0.01, 0.1)
        if dist <= maxDist:
            l.append(Point(dist, weight))
            n += 1
    return l

@measure_time
def pointGenerator(numPoints, maxDist):
    n = 0
    while n <= numPoints:
        dist = random.random()
        random.seed()
        weight = random.uniform(0.01, 0.1)
        if dist <= maxDist:
            n += 1
            yield Point(dist, weight)

print("List: ", getPointList(1000, 0.17))
print("Generator: ", pointGenerator(1000, 0.17))
