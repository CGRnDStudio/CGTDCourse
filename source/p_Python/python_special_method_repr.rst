==========================================
Python特殊方法：__repr__
==========================================

.. code-block:: python

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

.. code-block:: python

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
