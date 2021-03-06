呼吸灯
====================

前一节中我们已经掌握从hiibot_iots.py模块中导入IoTs2类，并实例化为iots2，然后对blueLED_bright属性赋不同的值以设置IoTs2蓝色LED亮度，
或者调用函数：blueLED_toggle()控制IoTs2蓝色LED的状态切换，也能达到指示灯闪烁的目的。

这一节我们将通过编程改变LED亮度实现呼吸效果。首先看下面的示例：

.. code-block::  python
  :linenos:

  import time
  from hiibot_iots2 import IoTs2
  iots2 = IoTs2()
  b=1.0
  while True:
      iots2.blueLED_bright = b
      b -= 0.05
      if b<0.0:
          b = 1.0
      time.sleep(0.1)

打开MU编辑器，点击“新建”按钮，并将本示例代码复制-粘贴的MU编辑器中，然后点击“保存”按钮，并在弹出的窗口中输入文件名为“code.py”，
保存文件的磁盘为“CIRCUITPY”，路径为该磁盘的根目录。一旦将code.py文件保存到IoTs2的CIRCUITPY磁盘上，IoTs2立即开始执行这个脚本程序。

仔细观察本示例程序的执行效果，感觉到IoTs2在打盹儿吗？蓝色LED灯的亮度逐渐减弱(像人的眼睛慢慢闭上)，然后立即变为最亮(像突然睁开眼睛)，
再逐渐变暗，如此往复。为什么有这种效果？下面我们逐行来分析每行脚本程序的效果。

  示例代码分析：

    - 第1行，导入一个Python内建的模块“time”
    - 第2行，从“/CIRCUITPY/lib/hiibot_iots2.py”模块中导入“IoTs2”类
    - 第3行，将导入的“IoTs2”类实例化为一个实体对象，名叫“iots2”
    - 第4行，声明一个变量“b”，并赋值1.0
    - 第5行，开始一个无穷循环的程序块
    - 第6行(无穷循环程序块的第1行)，将iots2对象的blueLED_bright属性值设置为变量b的值
    - 第7行(无穷循环程序块的第2行)，将变量b的值减小0.05
    - 第8行(无穷循环程序块的第3行)，判断变量b的值是否小于0.0
    - 第9行(无穷循环程序块的第4行)，如果b<0.0，则b=1.0
    - 第10行(无穷循环程序块的第5行)，执行time的sleep方法，参数为0.1秒(即100ms)

这个示例中，我们在无穷循环的程序块中不停地将变量b减小0.05，一直减到到b<0.0之后再把b重新赋值为1.0，如此重复，
而且每重复一次都会把b的值赋给iots2对象的blueLED_bright属性。

变量，允许在程序中改变的量！在本示例中，变量b的值顺序地取{1.0, 0.95, 0.90, .., 0.0}数据集中的一个值，
并把这个数值当作蓝色LED的亮度赋值给“iots2.blueLED_bright”属性。蓝色LED亮度的变化规律正好与数据集中的数值变化规律一致。

下面的示例程序执行结果具有特殊的医学效果：催眠。运行本示例程序时，切勿直视IoTs2的蓝色LED，直视蓝色LED太久，我们可能会被催眠！

.. code-block::  python
  :linenos:

  import time
  from hiibot_iots2 import IoTs2
  iots2 = IoTs2()
  b = 1.0
  dir = 0
  while True:
      iots2.blueLED_bright = b
      b += 0.05 if dir==1 else -0.05
      if b>1.0:
          b = 1.0
          dir = 0
      if b<0.0:
          b = 0.0
          dir = 1
      time.sleep(0.05)

你被催眠了吗？这个示例程序的执行效果俗称“呼吸灯”。蓝色LED的亮度从灭逐渐变为最亮，然后又逐渐灭掉，如此重复。
这样的周期如果正好与你的呼气-吸气的周期一致，据说很容易把人催眠。

这段程序能够让蓝色LED亮度随着我们呼吸节奏改变亮度，其中的关键之处是变量b的变化规律。第8～14行程序都是在增加或减少b变量的值。
你能列举出变量b取值的完全数据集？{}

你能用一句既贴切又合适的话来概括变量b的变化规律？

----------------------------------

.. admonition:: 
  总结：

    - 实体对象的属性赋值
    - 变量
    - 变量赋值
    - 变量自增/自减
    - 本节中，你总计完成了15行代码的编写工作


.. Important::
  **IoTs2类的blueLED属性和接口**

    - blueLED_bright (属性, 可读可写, 有效值：0.0~1.0), IoTs2蓝色LED的亮度
    - blueLED_toggle (函数，无参数), 切换IoTs2蓝色LED的状态

