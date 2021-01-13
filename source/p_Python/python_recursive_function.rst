=============================
Python递归函数
=============================

所谓递归就是在函数内部调用自己的函数被称之为递归，一般递归函数都有终止条件，采用的是后入先出的压栈数据结构。

阶乘函数 ``n!``

.. code-block:: python

    def factorial(n):

        if n == 1:
            return 1
        
        return n * factorial(n - 1)

斐波那契数列 ``1, 1, 2, 3, 5, 8...``

.. code-block:: python

    def fibonacci(n):

        if n < 2:
            return n

        return fibonacci(n - 2) + fibonacci(n - 1)

从递归函数谈

.. code-block:: python

    os.walk()
    os.listdir()
    os.mkdir()
    os.makedirs()
    os.rmdir()
    os.removedirs()
    copy.copy()
    copy.deepcopy()

深浅拷贝

从递归函数谈reduce

os.listdir递归查找文件

children递归查找filecache

斐波拉契数列
1 1 2 3 5 8

.. code-block:: python

    def fibonacci(num):
        if isinstance(num, int):
            if num <= 0:
                return 0
            elif num == 1:
                return 1
            else:
                return fibonacci(num - 1) + fibonacci(num - 2)
        else:
            raise ValueError("The input number error!")

    def factorial(number):

        if not isinstance(number, int) or number <= 0:
            return

        result = 1

        for n in range(1, number + 1)
            result *= n

        return result

    factorial(100)

    def fact(number):
        if number == 1:
            return number
        return number * fact(number - 1)

.. code-block:: python

    # os.walk()
    import os
    from pprint import pprint

    def walkFolders(folderPath):
        subFileList = []
        for subFileName in os.listdir(folderPath):
            subPath = os.path.join(folderPath, subFileName)
            if os.path.isfile(subPath):
                subFile = {"type": "file", "name": subFileName}
                subFileList.append(subFile)
            else:
                subFolder = {"type": "folder", "name": subFileName, "subFiles": walkFolders(subPath)}
                subFileList.append(subFolder)
        return subFileList
