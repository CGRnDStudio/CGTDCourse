=============================
Python自定义类
=============================

私有属性获取与修改可以通过方法，这样可以在修改属性之前做些check。

.. code-block:: python

    class Student(object):
        def __init__(self, name, score):
            self.__name = name
            self.__score = score

        def getName(self):
            return self.__name

        def getScore(self):
            return self.__score

        def setName(self, name):
            self.__name = name

        def setScore(self, score):
            if score >= 0 and score <= 100: 
                self.__score = score
            else:
                print("value wrong")

.. code-block:: python

    class Student(object):
        def __init__(self, name, score):
            self.__name = name
            self.__score = score

        @property
        def score(self):
            return self.__score

        @score.setter
        def score(self, value):
            if value >= 0 and value <= 100:
                self.__score = value
            else:
                print("value wrong")


    s1 = Student("Andy", 90)

    print(s1.score)

    s1.score = 80

    print(s1.score)



自定义类也称自定义数据类型，下面是自定义类的一些标识。

- class
- 类命名首字母大写
- self
- __init__

自定义类的语法

.. code-block:: python

    class CustomClass(object):
        pass

理解类的一些概念

- 类封装
- 类继承
- 类多态

- 实例属性和实例方法
- 类属性和类方法
- 静态方法

.. code-block:: python

    class MyClass(object):
        
        def __init__(self, var1, var2):
            self.a = var1
            self.b = var2
            
        def sum(self):
            return self.a + self.b
        
    a = MyClass(200, 300)
    print(a)
    print(a.sum())

理解特殊方法__repr__，特殊方法也称魔法方法或者双下方法。

.. code-block:: python

    class Car(object):
        def __init__(self, name, eng, year):
            self.name = name
            self.eng = eng
            self.year = year
        
        def __repr__(self):
            return "My car name is %s" % self.name
        
    car = Car("Jili", 120, 2019)
    print(car)

类继承

.. code-block:: python

    class Car(object):
        def __init__(self, name, eng, year):
            self.name = name
            self.eng = eng
            self.year = year
        
        def __repr__(self):
            return "My car name is %s" % self.name
        
        def orderParts(self, *args):
            print("Connecting to server...")
            print("Ordering parts %s: for car %s" % (args, self.name))
            print("Checking status")
        
    class Truck(Car):
        def __init__(self, name, eng, year):
            Car.__init__(self, name, eng, year)
            
    truck = Truck("Benz", 800, 2008)
    truck.orderParts("Wheels", "Silencer")

类继承分单继承和多继承，注意__init__的用法。

- 如果子类没有定义初始化函数，父类的初始化函数默认被调用。
- 如果子类定义了自己的初始化函数，但没有显示调用父类的初始化函数，则父类属性不会被初始化。
- 如果子类定义了自己的初始化函数，在子类中显示调用父类，子类和父类的属性都会被初始化。

初始化方案

.. code-block:: python

    # python 2.x
    def __init__(self, args):
        super(ClassName, self).__init__(args)

    # python 3.x
    def __init__(self, args):
        super().__init__(args)

    def __init__(self, args):
        ClassName.__init__(args)

    # PyQt中
    # python 2.x
    def __init__(self, parent=None):
        super(ClassName, self).__init__(parent)

    # python 3.x
    def __init__(self, parent=None):
        super().__init__(parent)

自定义向量类型

.. code-block:: python

    class Vector(object):
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z
        
        def __repr__(self):
            return "Vector(%f, %f, %f)" % (self.x, self.y, self.z)
        
        def __add__(self, other):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        
    v1 = Vector(2, 1.5, 3.2)
    v2 = Vector(3, 4, 5)
    print(v1)
    print(v1 + v2)

.. code-block:: python

    import math
    from __future__ import division

    class Vector(object):
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z
        
        def __repr__(self):
            return "Vector(%f, %f, %f)" % (self.x, self.y, self.z)
        
        def __add__(self, other):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        
        def __sub__(self, other):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        
        def __mul__(self, other):
            return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
        
        def __div__(self, other):
            return Vector(self.x / other.x, self.y / other.y, self.z / other.z)
        
        def __getitem__(self, item):
            if item == 0:
                return self.x
            elif item == 1:
                return self.y
            elif item == 2:
                return self.z
            else:
                raise IndexError("There is no vector index: %d" % item)
                
        def __setitem__(self, key, value):
            if key == 0:
                self.x = value
            elif key == 1:
                self.y = value
            elif key == 2:
                self.z = value
            else:
                raise IndexError("There is no vector index: %d" % key)
        
        def dot(self, other):
            return self.x * other.x + self.y * other.y + self.z * other.z
        
        def cross(self, other):
            return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
        
        def length(self):
            return math.sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))
        
    v1 = Vector(2, 1.5, 3.2)
    v2 = Vector(3, 4, 5)
    print(v1)
    print(v1 + v2)
    print(v1.dot(v2))
    print(v1.length())
    print(v1[2])
    v1[2] = 10
    print(v1)

实例方法、类方法和静态方法

.. code-block:: python

    import string

    def getAllChars():
        all_letters = string.ascii_lowercase
        result=[]
        for letter in all_letters:
            result.append([letter, all_letters.find(letter)])
        return result

    def generateChars():
        all_letters = string.ascii_lowercase
        for letter in all_letters:
            yield letter, all_letters.find(letter)
            
    for i in generateChars():
        print("Letter: {0} - Index: {1}".format(*i))

语法糖与装饰器

- @property
- @classmethod
- @staticmethod

.. code-block:: python

    def check_args(func):
        def wrap(*args):
            args = filter(bool, args)
            func(*args)

        return wrap


    @check_args
    def test(*args):
        print(args)


    print(test)
    test(1, 0, 2, "", [], 3)

装饰器不一定非得是个函数返回包装对象，也可以是个类，通过__call__完成目标调用

.. code-block:: python

    class CheckArgs(object):
        def __init__(self, func):
            self._func = func

        def __call__(self, *args):
            args = filter(bool, args)
            self._func(*args)


    @CheckArgs
    def test(*args):
        print(args)


    print(test)
    test(1, 0, 2, "", [], 3)

为class提供装饰器

.. code-block:: python

    def singleton(cls):
        def wrap(*args, **kwargs):
            o = getattr(cls, "__instance__", None)

            if not o:
                o = cls(*args, **kwargs)
                cls.__instance__ = o

            return o

        return wrap


    @singleton
    class A(object):
        def __init__(self, x):
            self.x = x

    print(A)
    a, b = A(1), A(2)
    print(a is b)

类专属的装饰器

.. code-block:: python

    class Artist(object):
        _hits = ["John"]

        def __init__(self, name):
            self._name = name

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, name):

            if name not in CUSTOM_ARTIST:
                raise ValueError("%s is not a custom artist" % name)

            self._name = name

        @staticmethod
        def random_artist():
            return Artist(random.choice(CUSTOM_ARTIST))

        @classmethod
        def hits(cls):
            return cls._hits


    # rr = Artist("Andy Hu")
    # print(rr.name)
    # print(type(rr.name))
    # rr.name = "Andy"
    # print(rr.name)
    # rr2 = Artist.random_artist()
    # print(rr2.name)
    # print(Artist.hits())
    # print(Artist._hits)
    rr = Artist("Andy")
    print(rr.random_artist())
    # print(rr.hits())

私有属性与私有方法

在定义方法前面加__method即声明私有方法，理论上私有方法是不能被继承的，只能在当下定义的类中被调用，但Python的私有方法只是约定上的私有，实际是可以通过类名来访问。

- 类属性和类方法可以被实例对象来调用，也可以通过类名直接调用，一般是通过类名调用
- 静态方法可以被实例对象来调用
- 实例属性和实例方法只能通过实例对象来调用，不能通过类名直接调用
- 静态方法和类方法的区别是类方法可能需要访问类属性，和类还有那么点关系，静态方法是访问不了任何类属性或者实例属性的
