改变RGB灯珠的颜色
======================

RGB像素灯珠串是非常有趣的一种输出，不仅可以用于照明和产生彩光，还能输出动态的流光溢彩的光效。

IoTs2上仅有1颗RGB彩色灯珠，虽然不能产生彩色灯珠串那种流光溢彩的光效，但仍可以利用这个灯珠产生有趣的光效。

如果你已经使用IoTs2一段时间了，相信你一定注意过IoTs2的RGB彩色灯珠，在IoTs2每次启动时该灯珠的颜色都会切换几次，
这些颜色代表不同的IoTs2状态，譬如显示紫色时此时按下Boot按钮将迫使IoTs2进入二级BootLoader状态(可更新Python固件)，
当显示黄色时按下Boot按钮将迫使IoTs2进入Python的安全模式(不执行我们的code.py程序)。
本节我们将掌握如何通过编程控制这个灯珠编程产生特殊的颜色。

第一个示例的代码如下：

.. code-block::  python
  :linenos:

  import time
  from hiibot_iots2 import IoTs2
  iots2 = IoTs2()
  iots2.pixels.auto_write = True
  iots2.pixels.brightness = 0.1
  colorsList = [(255,0,0),(192,63,0),(127,127,0),(0,255,0),
              (0,127,127), (0,0,255),(127,0,127)]
  index = 0
  while True:
      iots2.pixels[0] = colorsList[index%len(colorsList)]
      time.sleep(0.5)
      index += 1

打开MU编辑器，点击“新建”按钮，并将本示例代码复制-粘贴的MU编辑器中，然后点击“保存”按钮，并在弹出的窗口中输入文件名为“code.py”，
保存文件的磁盘为“CIRCUITPY”，路径为该磁盘的根目录。一旦将code.py文件保存到IoTs2的CIRCUITPY磁盘上，IoTs2立即开始执行这个脚本程序。
运行这个示例程序时，如果你的环境光较暗，可以调低RGB像素灯珠的亮度，即减小第5行代码的等号右边的值，避免眼睛盯着非常明亮的光源。

  示例代码分析：

    - 第1行，导入一个Python内建的模块“time”
    - 第2行，从“/CIRCUITPY/lib/hiibot_iots2.py”模块中导入一个名叫“IoTs2”的类
    - 第3行，将导入的“IoTs2”类实例化为一个实体对象，名叫“iots2”
    - 第4行，设置iots2对象的pixels的auto_write属性(即RGB像素彩灯的自动刷新)为True
    - 第5行，设置iots2对象的pixels的brightness属性(即RGB像素彩灯的整体亮度)为0.1，合理取值范围：0.05(亮度最小)~1.0(亮度最大)
    - 第6~7行，定一个名叫“colorsList”颜色列表，列表中包含7种颜色(即彩虹的颜色)的RGB值
    - 第8行，定义一个变量index，并设置其初始值为0
    - 第9行，开始一个无穷循环的程序块
    - 第10行(无穷循环程序块的第1行)，设置iots2对象的pixels[0]像素灯珠的颜色为colorsList[index%len(colorsList)]，即颜色列表colorsList[]种的某一项
    - 第11行(无穷循环程序块的第2行)，执行time的sleep方法，参数为0.5秒，即系统空操作0.5秒
    - 第12行(无穷循环程序块的第3行)，将变量index增加1

对照每一行代码的作用，你能根据观察到的本示例程序的执行效果与示例代码逐行地对照上吗？

-----------------------

.. admonition:: 
  总结：

    - RGB像素灯珠
    - RGB三基色
    - 子类
    - 变量赋值
    - 变量自增/自减
    - 逻辑判断和逻辑程序块
    - 本节中，你总计完成了12行代码的编写工作

------------------------------------


.. Important::
  **IoTs2类的pixel属性和接口**

    - pixels (子类), BlueFi的NeoPixel子类
    - pixels.n (属性, 只读, 有效值：1或更多), IoTs2的RGB像素灯珠的个数(默认为1)
    - pixels.brightness (属性, 可读可写, 有效值：0.0～1.0), IoTs2的RGB像素灯珠的亮度
    - pixels.auto_write (属性, 可读可写, 有效值：0/False 或 1/True), 自动更新IoTs2 RGB像素灯珠的状态
    - pixels[0] (属性, 可读可写, 有效值：tuple型(R,G,B)三基色信息), IoTs2的RGB像素灯珠颜色
    - pixles.fill( (R,G,B) ) (函数, 输入参数：三基色分量的元组, 无返回值), 填充IoTs2的所有RGB像素灯珠为指定的颜色
    - pixels.show() (函数, 无输入参数, 无返回值), 更新IoTs2的RGB像素灯珠的状态(当pixles.auto_write为False时，改变pixels的任何属性值后必须调用此方法更新像素的状态)
