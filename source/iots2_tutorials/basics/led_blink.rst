正在工作中..
====================

LED指示灯是最简单的一种输出设备，常用于指示计算机系统的内部状态。在IoTs2上有一个可编程控制的蓝色LED指示灯。
所谓可编程控制的LED，就是我们可以用程序控制其亮度，以及亮或灭。

首先看一个示例：

.. code-block::  python
  :linenos:
  
  import time
  from hiibot_iots2 import IoTs2
  iots2 = IoTs2()
  while True:
      iots2.blueLED_bright = 1.0
      time.sleep(0.5)
      iots2.blueLED_bright = 0.0
      time.sleep(0.5)

打开MU编辑器，点击“新建”按钮，并将本示例代码复制-粘贴的MU编辑器中，然后点击“保存”按钮，并在弹出的窗口中输入文件名为“code.py”，
保存文件的磁盘为“CIRCUITPY”，路径为该磁盘的根目录。一旦将code.py文件保存到IoTs2的CIRCUITPY磁盘上，IoTs2立即开始执行这个脚本程序。

这个示例程序的执行效果是：IoTs2的蓝色LED指示灯不停地闪烁。闪烁的LED指示灯常用于指示计算机系统正在工作中，如果程序一旦停止，指示灯也停止闪烁。
如果你打开MU编辑器的串口控制台，按下“Ctrl+C”键让IoTs2终止执行code.py程序，进入REPL模式，你会发现蓝色LED指示灯不再闪烁。

下面我们逐行来分析每行脚本程序的效果，就像REPL一样地执行程序。

  示例代码分析：

    - 第1行，导入一个Python内建的模块“time”
    - 第2行，从“/CIRCUITPY/lib/hiibot_iots2.py”模块中导入一个名叫“IoTs2”的类
    - 第3行，将导入的“IoTs2”类实例化为一个实体对象，名叫“iots2”
    - 第4行，一个无穷循环的程序块
    - 第5行(无穷循环程序块的第1行)，iots2实体对象的blueLED_bright属性(蓝色LED指示灯的亮度)设置为1.0
    - 第6行(无穷循环程序块的第2行)，执行time的sleep方法，参数为0.5秒
    - 第7行(无穷循环程序块的第3行)，iots2实体对象的blueLED_bright属性(蓝色LED指示灯的亮度)设置为0.0
    - 第8行(无穷循环程序块的第4行)，执行time的sleep方法，参数为0.5秒

其中第1行和第2行都是导入Python的模块，为什么有两种不同的写法呢？第1行的导入方法，目的是将整个time模块导入到code.py中；
第2行的导入方法仅仅从hiibot_iots2.py模块中导入IoTs2类，或许hiibot_iots2.py模块中还有其他类。事实上，
Python的导入(import)模块的方法远不止这两种，如果需要深入了解import的其他方法，可以使用网络引擎搜索“python import”查阅更多的介绍。

第3行是本示例的重点，执行这个语句的目的是将IoTs2类实例化。Python是一种面向对象编程(OOP)的机制，IoTs2类包含有多种接口或方法，
通过类的实例化对象即可访问该类的接口或方法。

第5行和第7行也是本示例的重点，从两个语句中等号右边的值我们可以想象得出，一个语句是让蓝色LED亮度为最大，另一个语句是让蓝色LED亮度为0(即LED灭)。
我们可以借助于REPL模式分别单步执行其中一个语句，并观察蓝色LED指示灯的状态。在MU编辑器的串口控制台窗口，按下“Ctrl+C”键，
让IoTs2进入REPL模式，然后在“>>”提示符后依次输入以下语句并按“Enter”键执行每一个语句：

.. code-block::  python
  :linenos:
  
  >> from hiibot_iots2 import IoTs2
  >> iots2 = IoTs2()
  >> iots2.blueLED_bright = 1.0
  >>  

然后，观察执行“iots2.blueLED_bright = 1.0”之后蓝色LED的状态；然后再输入下面语句并按“Enter”键，观察蓝色LED的状态：


.. code-block::  python
  :linenos:
  
  >> iots2.blueLED_bright = 0.0
  >>  

我们在“IoTs2简介”的内容中已经遇到过下面的示例代码：

.. code-block::  python
  :linenos:

  import time
  from hiibot_iots2 import IoTs2
  iots2 = IoTs2()
  iots2.blueLED_bright = 1.0
  while True:
      iots2.blueLED_toggle()
      time.sleep(0.5)

现在可以仔细来理解每一个语句的作用和执行效果。打开MU编辑器，点击“新建”按钮，并将本示例代码复制-粘贴的MU编辑器中，然后点击“保存”按钮，
并在弹出的窗口中输入文件名为“code.py”，保存文件的磁盘为“CIRCUITPY”，路径为该磁盘的根目录。一旦将code.py文件保存到IoTs2的CIRCUITPY磁盘上，
IoTs2立即开始执行这个脚本程序。

这个示例程序的执行效果：IoTs2的蓝色LED指示灯不停地闪烁。程序执行效果与上面的示例相同！但代码看起来有很多区别，这是为什么？
显然，同一种任务可以采用不同的程序软件来实现！


下面我们逐行来分析每行脚本程序的效果。

  示例代码分析：

    - 第1行，导入一个Python内建的模块“time”
    - 第2行，从“/CIRCUITPY/lib/hiibot_iots2.py”模块中导入一个名叫“IoTs2”的类
    - 第3行，将导入的“IoTs2”类实例化为一个实体对象，名叫“iots2”
    - 第4行，将iots2实体对象的blueLED_bright属性(蓝色LED指示灯的亮度)设置为1.0
    - 第5行，一个无穷循环的程序块
    - 第6行(无穷循环程序块的第1行)，调用iots2实体对象的接口函数blueLED_toggle()
    - 第7行(无穷循环程序块的第2行)，执行time的sleep方法，参数为0.5秒

从代码分析看，实现IoTs2上蓝色LED闪烁的关键语句是第6行，即调用iots2实体对象的接口函数blueLED_toggle()，
这个接口函数可以实现蓝色LED的亮/灭状态切换。现在我们尝试将第4行代码中“iots2实体对象的blueLED_bright属性值”修改为0.1，
再观察蓝色LED的闪烁效果。或者修改为其他值，再观察效果。注意，blueLED_bright属性值的有效范围：0.0~1.0。

通过反复修改示例中第4行的blueLED_bright属性值，我们将会发现闪烁时蓝色LED的亮度不同。

-------------------------------------

.. admonition:: 
  总结：

    - Python的程序块使用相同的行缩进空格数来界定
    - Python的import有很多种用法，本节我们使用过两种方法
    - Python中的导入的类，使用前必须先实例化, iots2=IoTs2()
    - 实体对象的属性赋值

      - iots2.blueLED_bright=1.0   # 蓝色LED亮度的属性值

      
    - 实体对象的函数调用
      
      - iots2.blueLED_toggle()   # 切换蓝色色LED的状态

    - 本节中，你总计完成了8行代码的编写工作

.. Important::
  **IoTs2类的blueLED属性和接口**

    - blueLED_bright (属性, 可读可写, 有效值：0.0~1.0), IoTs2蓝色LED的亮度
    - blueLED_toggle (函数，无参数), 切换IoTs2蓝色LED的状态

