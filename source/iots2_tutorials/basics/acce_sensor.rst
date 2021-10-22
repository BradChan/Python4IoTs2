加速度传感器
======================

加速度传感器是惯性导航装置中最重要的一个组件，这是一种利于地球重力场的物理特性的传感器，并组合敏感元件、特殊设计的机械结构。
加速度计、地磁计、海拔计和陀螺仪都是惯性导航的关键元件，本节内容中仅涉及加速度计。由于加速度传感器是基于地球重力场的物理特性，
无法用于地外太空领域。

IoTs2的陶瓷型WiFi天线的附近就是加速度计元件，这是一种3-DoF/3轴角速度传感器，其体积非常小是因为近些年才发展起来的MEMS(微机电系统)技术，
以及今天的半导体技术使得这些惯性元件的体积非常小，但在原理上几乎与数十年前使用的体积庞大的加速度传感器相同。

-----------------------

重力加速度和姿态感知
-----------------------

今天的惯性测量装置几乎是所有飞行器的关键元件，没有这些元件我们的飞机无法准确地抵达目的地，无人机无法稳定停留在空中帮你拍照。
加速度计使用近地空间不变的重力场方向和重力常数(g)，借助于压电效应、容变、热变等敏感元件、特定机械结构和测量电路，
根据牛顿第三定律当物体姿态发生改变时的加速度变化对传感器内部的质量块/热气腔产生反作用力，敏感元件和测量电路能够精确地测量力的大小，
从而得到加速度的变化。

根据加速度计的设计，加速度计分为动态型和动静态型两类。采用压电效应的加速度传感器只能感知加速度的“动态”变化，
无法感知确定静态时的物体姿态，此类传感器必须借助于姿态估算算法和动态加速度变化信息来确定物体的当前姿态；采用容变和热变的加速度传感器，
特殊的机械结构、敏感元件和测量电路设计使得他们不仅能感知加速度的动态变化，还能测量静态的姿态。基于中学的物理知识(力的分量和合成)，
结合下图我们就能想象得出加速度计的基本原理：

.. image:: /../../_static/images/iots2_tutorials/acce_principle.jpeg
  :scale: 100%
  :align: center

此图仅展示一个方向的加速度变化和重力分量。事实上，我们在描述物体的加速度时总会先构建一个三维坐标系，加速度计会输出三个方向的加速度分量。
当然也有少部分加速度传感器只能给出x-、y-两个方向的加速度分量。所以加速度传感器又分为1D-、2D、3D的。

IoTs2采用3D的动静态型加速度计，即使在静止状态，IoTs2的加速度传感器也能给出自己的准确姿势。
下面我们使用一个简单示例来观察IoTs2给出的加速度变化信息。示例代码如下：

.. code-block::  python
  :linenos:

  import time
  import terminalio
  import displayio
  from adafruit_display_text.label import Label
  from hiibot_iots2 import IoTs2
  iots2 = IoTs2()
  iots2.screen.rotation = 180
  # create a text label
  textlabel_group = displayio.Group(scale=2)
  textLabel_title = Label(terminalio.FONT, x=10, y=10, text="Acce", max_glyphs=10, scale=2, color=(255,0,0))
  textLabel_x = Label(terminalio.FONT, x=10, y=32, text="", max_glyphs=24, color=(255,0,0))
  textLabel_y = Label(terminalio.FONT, x=10, y=48, text="", max_glyphs=24, color=(0,255,0))
  textLabel_z = Label(terminalio.FONT, x=10, y=64, text="", max_glyphs=24, color=(0,0,255))
  textlabel_group.append(textLabel_title)
  textlabel_group.append(textLabel_x)
  textlabel_group.append(textLabel_y)
  textlabel_group.append(textLabel_z)
  # show those content on the IoTs2 screen
  iots2.screen.show(textlabel_group)
  while True:
      x, y, z = iots2.Accele_ms2 # Accele_Gs
      textLabel_x.text = "X: {:.2f}".format(x)
      textLabel_y.text = "Y: {:.2f}".format(y)
      textLabel_z.text = "Z: {:.2f}".format(z)
      time.sleep(0.1)

将本示例代码保存到IoTs2的/CIRCUITPY/code.py文件中，IoTs2在执行示例程序时，你可以尝试让IoTs2平躺、竖立、倒立、侧立等姿势，
并观察三个加速度分量与姿态之间关系，并找出加速度每一个分量的最小值和最大值(加速度每一个分量的范围)。

示例代码分析：

    - 第1行，导入一个Python内建的模块“time”
    - 第2行，导入一个Python内建的模块“terminalio”
    - 第3行，导入一个Python内建的模块“displayio”
    - 第4行，从“/CIRCUITPY/lib/adafruit_display_text/label.py”模块中导入一个名叫“Label”的类，即文本标签类
    - 第5行，从“/CIRCUITPY/lib/hiibot_iots2.py”模块中导入一个名叫“IoTs2”的类，即IoTs2模块类
    - 第6行，将导入的“IoTs2”类实例化为一个实体对象，名叫“iots2”
    - 第7行，将IoTs2的LCD屏幕旋转为180度，即USB座朝上
    - 第8行，注释
    - 第9～17行，定义一个文本标签组textlabel_group，然后定义4个文本标签并添加到textlabel_group中，这些文本标签分别为textLabel_title、textLabel_x、textLabel_y、textLabel_z
    - 第18行，注释
    - 第19行，将textlabel_group对象当作参数传递给“iots2.screen.show()”函数，即让上述文本标签的内容显示在IoTs2的LCD显示器上
    - 第20行，一个无穷循环的程序块
    - 第21行(无穷循环程序块的第1行)，用"iots2.Accele_ms2"更新变量x, y, z (iots2.Accele_ms2是采用m/s^2为量纲的加速度值)
    - 第22~24行(无穷循环程序块的第2~4行)，设置多行文本显示子类的第2行的文本内容为acce[0]的值
    - 第25行(无穷循环程序块的第5行)，执行time的sleep方法，参数为0.1秒

建议你设计数据记录表，将本示例给出的加速度三分量的值与姿态之间关系记录下来，然后根据这一关系确定姿态和加速度数据之间变化规律。
如果你想要以“相对加速度”(相对于地球重力场的加速度)的单位的结果，修改上述代码的第21行，即用“iots2.Accele_Gs”属性值更新x, y, 
z并观察结果。

我们还可以使用“iots2.angle_RollPitch”属性值获得IoTs2当前的姿态角：Roll(翻滚角)和Pitch(俯仰角)。修改上述示例代码，
增加2个文本标签，然后将“iots2.angle_RollPitch”属性值(2个元素组成的元组)当作2个标签的text属性显示在屏幕上。
修改后的代码如下：

.. code-block::  python
  :linenos:

  import time
  import terminalio
  import displayio
  from adafruit_display_text.label import Label
  from hiibot_iots2 import IoTs2
  iots2 = IoTs2()
  iots2.screen.rotation = 180
  # create a text label
  textlabel_group = displayio.Group(scale=2)
  textLabel_title = Label(terminalio.FONT, x=9, y=10, text="Acce", max_glyphs=10, scale=2, color=(255,0,0))
  textLabel_x = Label(terminalio.FONT, x=1, y=32, text="", max_glyphs=24, color=(255,0,0))
  textLabel_y = Label(terminalio.FONT, x=1, y=48, text="", max_glyphs=24, color=(0,255,0))
  textLabel_z = Label(terminalio.FONT, x=1, y=64, text="", max_glyphs=24, color=(0,0,255))
  textLabel_roll  = Label(terminalio.FONT, x=1, y=80, text="", max_glyphs=24, color=(255,0,255))
  textLabel_pitch = Label(terminalio.FONT, x=1, y=96, text="", max_glyphs=24, color=(0,255,255))
  textlabel_group.append(textLabel_title)
  textlabel_group.append(textLabel_x)
  textlabel_group.append(textLabel_y)
  textlabel_group.append(textLabel_z)
  textlabel_group.append(textLabel_roll)
  textlabel_group.append(textLabel_pitch)
  # show those content on the IoTs2 screen angle_RollPitch
  iots2.screen.show(textlabel_group)
  while True:
      x, y, z = iots2.Accele_ms2 # Accele_Gs
      roll, pitch = iots2.angle_RollPitch # angle of roll and pitch
      textLabel_x.text = "x: {:.2f}".format(x)
      textLabel_y.text = "y: {:.2f}".format(y)
      textLabel_z.text = "z: {:.2f}".format(z)
      textLabel_roll.text = "roll: {}".format(roll)
      textLabel_pitch.text = "pitch: {}".format(pitch)
      time.sleep(0.1)

修改前后的两种示例代码的执行效果如下图所示：

.. image:: /../../_static/images/iots2_tutorials/acce_angle_roll_pitch.jpg
  :scale: 25%
  :align: center

或许你会问“为什么只有翻滚角和俯仰角？” 除了翻滚角和俯仰角，3D空间物体的姿态角还有航向角(Yaw angle)，即绕着垂直于地面方向的直线的旋转角。
事实上，仅依赖IoTs2的3轴角速度传感器无法获取航向角信息。


用RGB像素颜色来表示加速度变化
-----------------------------

IoTs2的RGB像素彩灯是一种特殊的显示元件，响应速度快能呈现动感效果。在前一个示例中我们把加速度的三个分量的数值显示在LCD屏幕上，
当你旋转IoTs2改变其姿态时，观察屏幕的数值并不方便。那我们就想到其他的显示方式，譬如我们用IoTs2的RGB像素灯珠发出的光颜色来指示加速度的三个分量。
巧合的是，IoTs2加速度传感器能给出三个分量值，而RGB像素灯珠的颜色也正好是三个分量RGB。下面的示例程序中，
我们将IoTs2的加速度传感器三个分量分别映射为像素灯珠的RGB三基色的三个分量。示例代码如下：

.. code-block::  python
  :linenos:

  import time
  from hiibot_iots2 import IoTs2
  iots2 = IoTs2()
  # map acceleration values (-10.24~10.24) into 0~255
  def map(v):
      return  abs( int((v/10.24)*255.0) )

  while True:
      x, y, z = iots2.Accele_ms2 # unit with ms^2 
      iots2.pixels[0] = ( map(x), map(y), map(z) )
      time.sleep(0.1)

很酷！这么短一点代码就能实现如此酷的效果。这个示例的程序结构已经被我们在前几节中反复使用过，我们定义来一个函数来处理数据映射：
把加速度的某个分量值(范围-10.24～+10.24)映射成RGB三基色某个分量(范围0~255)。下面是该示例程序的代码分析：

示例代码分析：

    - 第1行，导入一个Python内建的模块“time”
    - 第2行，从“/CIRCUITPY/lib/hiibot_iots2.py”模块中导入一个名叫“IoTs2”的类
    - 第3行，将导入的“IoTs2”类实例化为一个实体对象，名叫“iots2”
    - 第4行，注释
    - 第5行，定义一个名叫“map”的函数，输入参数是变量v
    - 第6行，函数map的程序块，直接返回“abs( int((v/10.24)*255.0) )”
    - 第8行，开始一个无穷循环
    - 第9行(无穷循环程序块的第1行)，将元组型sensor.acceleration加速度传感器的三分量分别赋给变量x,y,z
    - 第10行(无穷循环程序块的第2行)，分别将x,y,z映射为RGB三基色分量，并用这个三基色设置IoTs2的RGB彩灯颜色
    - 第11行(无穷循环程序块的第3行)，执行time的sleep方法，参数为0.1秒

将本示例代码保存到IoTs2的/CIRCUITPY/code.py文件中，当IoTs2运行示例代码期间，试着改变IoTs2的姿态，
你发现IoTs2的RGB像素的颜色与IoTs2姿态之间什么关系？

正面朝上时，为什么是蓝色？根据本示例代码，以及加速度传感器三分量、姿态之间关系，请你说明这个原因。

-----------------------------

.. admonition:: 
  总结：

    - 地球重力场和方向
    - 地球重力常数
    - 加速度计
    - 姿态感知和加速度
    - 姿态估算和加速度动态变化
    - 多行文本显示的数据结构
    - 文本字体的缩放
    - 本节中，你总计完成了56行代码的编写工作

------------------------------------

.. Important::
  **IoTs2类的加速度传感器属性和接口**

    - Accele_Range (属性值，可读可写的，有效值为{0, 1, 2, 3}分别代表2G、4G、8G和16G的加速度范围(G——地球重力加速度))
    - Accele_DataRate (属性值，可读可写的，有效值为0~9的整数，分别代表掉电、1Hz、10Hz、25Hz、50HZ、100Hz、200Hz、400Hz、1.6KHz、1.334KHz的加速度数据采样率
    - Accele_ms2 (属性, 元组类型, 只读, 每个分量的有效值: -10.24~+10.24), IoTs2的Accele_ms2属性采用m/s^2为加速度量纲, 加速度传感器的三个分量值

      - Accele_ms2[0]: x方向分量
      - Accele_ms2[1]: y方向分量
      - Accele_ms2[2]: z方向分量

    - Accele_Gs (属性, 元组类型, 只读, 每个分量的有效值: -1.0~+1.0), IoTs2的Accele_Gs属性是相对加速度值，相对于地球标准重力场的加速度值, 加速度传感器的三个分量值

      - Accele_Gs[0]: x方向分量
      - Accele_Gs[1]: y方向分量
      - Accele_Gs[2]: z方向分量

    - angle_RollPitch (属性, 元组类型, 只读, 每个分量的有效值: -180~+180), IoTs2的angle_RollPitch属性是翻滚角和俯仰角，angle_RollPitch的两个分量值

      - angle_RollPitch[0]: 翻滚角(roll)
      - angle_RollPitch[1]: 俯仰角(pitch)

    - Shake (函数, 输入参数: 阈值, 采样次数, 延迟时间, 返回值: 0/False或1/True), IoTs2的加速度传感器的晃动检测, 返回1/True:有晃动，0/False:无晃动

