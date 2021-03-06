===============================
Deadline渲染农场池和组的概念
===============================

Groups很容易理解，渲染节点的硬件和软件配置不同可以设置不同的组以便适应不同任务渲染。比如现在有一批Houdini 18的文件需要渲染，你只能在已经安装过Houdini 18的机器上才能正确渲染，别的机器渲染肯定会报错，此时为了排除不正确的机器就可以将机器编组，提交任务的时候将任务丢到组中，这样就不会调度没有组的机器。

池可以说是有优先级顺序的组，相当于把农场几分天下，有时候有这样一些需求就是灯光任务优先级永远是最高的，或者分配一部分机器给某一个项目优先使用，此时就要用到池的概念，一个任务进农场调度机器首先会检查它属于哪个池，如果没有设置池的属性，渲染优先级都是最低的，设置了池，任务就会到这个池中然后按正常的优先级，提交日期和组去调度池中的机器。如果池中没有了任务，机器才会调度给没有设置池的任务，即使他们的优先级设置了100也没用，池中优先级是最优先的。
