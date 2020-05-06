==============================
Houdini VEX：内置函数
==============================

VEX内置函数有七八百之多，掌握如何查询与使用的通用心法非常重要，剩下的就是靠项目经验的积累来灵活运用。

我们来查看帮助文档具体分析VEX内置函数使用上的需要掌握的知识点。

.. code-block:: python

    int  addpoint(int geohandle, int point_number)

        Creates a new point with all the attributes and group memberships of the point with the given point number.

    int  addpoint(int geohandle, vector pos)

        Creates a new point with the given position.

写过函数的我们都知道函数最关键的就是传参以及返回值，我们分析一下addpoint()这个函数的形式参数和返回值。

首先addpoint,这个函数有两种写法，这是一种函数重载的写法，意味着你传入不同的实参的时候VEX会自我选择对应函数执行，如果实参类型和所有函数的形参类型都对不上，则会报错。函数重载是VEX内置函数的一种常见形态。

- int geohandle也是VEX内置函数常见的一个形参，这个和Python类中的self很像，指的是当前几何体自身，一般传入0或者geoself()。

- int point_number表示添加几个点。

- vector pos表示添加一个点的空间坐标，是个向量类型。

.. code-block:: python

    vector position = {0, 0, 0};
    addpoint(0, position);

代码创建一个三角形。

.. code-block:: python

    int p1 = addpoint(geoself(), {0, 1, 0});
    int p2 = addpoint(geoself(), {1, 1, 0});
    int p3 = addpoint(geoself(), {1, 1, 1});

    int prim = addprim(geoself(), "poly");
    addvertex(geoself(), prim, p1);
    addvertex(geoself(), prim, p2);
    addvertex(geoself(), prim, p3);

代码创建一个圆环。

.. code-block:: python

    float angle = 0;
    int num = chi("num");
    float segmentAngle = 2 * PI / num;
    int prim = addprim(geoself(), "poly");

    for (int n = 0; n < num; n++) {
        int p = addpoint(geoself(), set(cos(angle), 0, sin(angle)));
        addvertex(geoself(), prim, p);
        angle += segmentAngle;
    }

代码实现正弦波。

.. code-block:: python

    @P.y = sin(@P.x + @Time);

代码实现噪波。

.. code-block:: python

    // size = 5
    // offset = 0
    // threshold = 0.5
    @Cd = {0, 0, 0};
    float noseValues = noise(@P*chf("size") + chf("offset"));

    if(noseValues > chf("threshold")) {
        @Cd.r = 1;
    }


VEX代码可视化，创建一个line节点，将点数增加到1000。

.. code-block:: python

    @P.y = @P.x;
    @P.y = pow(@P.x, 2);
    @P.y = sin(@P.x);
    @P.y = floor(@P.x);
    @P.y = frac(@P.x);
    @P.y = abs(@P.x);
    @P.y = abs(sin(@P.x));
    @P.y = floor(sin(@P.x));
    @P.y = clamp(sin(@P.x));
    @P.y = pow(frac(@P.x), 2);
    @P.y = noise(frac(@P.x));


内置函数set()可以用来做类型的强制转换，这非常有用，很多时候定义向量，四元素的时候以花括号初始化固定值，不能是动态的值，我们可以依赖set()函数来处理。

.. code-block:: python

    vector2  set(float v1, float v2)

    vector  set(float v1, float v2, float v3)

    vector4  set(float v1, float v2, float v3, float v4)

    matrix2  set(float v1, float v2, float v3, float v4)

    matrix3  set(float v1, float v2, float v4, float v4, float v5, float v6, float v7, float v8, float v9)

    matrix  set(float v1, float v2, float v3, float v4, float v5, float v6, float v7, float v8, float v9, float v10, float v11, float v12, float v13, float v14, float v15, float v16)

然而set()有其更复杂的类型转换机制，可以参考文档 http://www.sidefx.com/docs/houdini/vex/functions/set

VEX内置函数的分类:

=========================== ========== ===============================================
ARRAYS                      数组       append, argsort, array, insert, isvalidindex,

                                       len, pop, push, removeindex, removevalue,

                                       reorder, resize, reverse, slice, sort
ATTRIBUTES AND INTRINSICS   属性       addattrib, adddetailattrib, addpointattrib,

                                       addprimattrib, addvertexattrib, attrib,

                                       detail, point, prim, primintrinsic, primuv,

                                       setpointattrib, setprimattrib, setprimintrinsic,

                                       setvertexattrib, vertex
BSDFS
CHOP                        通道
COLOR                       颜色
CONVERSION                  转换       atof, atoi, degrees, radians
CROWDS                      群组
DISPLACE                    置换
FILE I/O                    IO
FUZZY LOGIC
GEOMETRY                    几何体     addpoint, addprim, addvertex, geoself,

                                       intersect, intersect_all, nearpoint,

                                       nearpoints, npoints, nprimitives, nvertices,
                                       
                                       pointprims, pointvertex, pointvertices, 
                                       
                                       primpoint, primpoints, primvertex, primvertexcount,
                                       
                                       removepoint, removeprim, removevertex
GROUPS                      组         expandpointgroup, expandprimgroup, expandvertexgroup,

                                       inpointgroup, inprimgroup, invertexgroup,
                                       
                                       npointsgroup, nprimitivesgroup, setpointgroup,

                                       setprimgroup, setvertexgroup
HALF-EDGES
IMAGE PROCESSING
INTERPOLATION               插值         clamp, fit, fit01, fit10, fit11, lerp
LIGHT                                      
MATH                        数学        abs, acos, asin, atan, atan2, ceil, cos,

                                        cross, dot, floor, frac, length, length2,
                                        
                                        log, log10, max, min, normalize, pow, sin,

                                        sqrt, sum, tan

                                        pow, sin, squrt, sum
MEASURE                     测量        distance, getbbox, getbbox_size, relbbox
METABALL                    
NODES                       节点         ch, ch2, ch3, ch4, chf, chi, chramp, chs,

                                         chu, chv, opfullpath
NOISE AND RANDOMNESS        噪波         anoise, noise, rand, random, snoise, xnoise
NORMALS                     法线
OPEN COLOR IO               色彩空间
PARTICLES                   粒子
POINT CLOUDS AND 3D IMAGES  点云          pcfilter, pcfind, pcimport, pcopen
SAMPLING                    采样
SENSOR INPUT                传感器
SHADING AND RENDERING       材质渲染
STRINGS                     字符串        endswith, find, isalpha, isdigit, itoa,

                                          join, lstrip, match, re_find, re_findall,

                                          re_match, re_replace, re_split, split,

                                          sprintf, toupper
SUBDIVISION SURFACES        
TETRAHEDRONS                
TEXTURING                   贴图
TRANSFORMS AND SPACE        
USD                         USD
UTILITY                     实用        getcomp, printf, set, setcomp
VOLUME                      体积       
=========================== ========== ===============================================

.. code-block:: bash

    vector npos = point(1, "P", @ptnum);

    int np = addpoint(0, npos);

    addprim(0, "polyline", @ptnum, np);

---------------
参考文档
---------------

- http://www.sidefx.com/docs/houdini/vex/functions/index.html

