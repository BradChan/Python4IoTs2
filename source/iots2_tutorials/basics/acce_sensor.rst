加速度传感器
======================

加速度传感器是惯性导航装置中最重要的一个组件，这是一种利于地球重力场的物理特性的传感器，并组合敏感元件、特殊设计的机械结构。
加速度计、地磁计、海拔计和陀螺仪都是惯性导航的关键元件，本节内容中仅涉及加速度计。由于加速度传感器是基于地球重力场的物理特性，
无法用于地外太空领域。

BlueFi的背面画有x-y坐标系图案的旁边就是加速度计和陀螺仪的组合元件，体积非常小，这是因为他们采用近些年才发展起来的MEMS(微机
电系统)技术进行设计和制造，使得这些惯性元件的体积急剧缩小，今天的半导体技术使得他们的成本也很低，但在原理上几乎与数十年前使用
的体积庞大的加速度传感器和陀螺仪相同。

-----------------------

重力加速度和姿态感知
-----------------------

今天的惯性测量装置几乎是所有飞行器的关键元件，没有这些元件我们的飞机无法准确地抵达目的地，无人机无法稳定停留在空中帮你拍照。
加速度计使用近地空间不变的重力场方向和重力常数(g)，借助于压电效应、容变、热变等敏感元件、特定机械结构和测量电路，根据牛顿第三定律当物体
姿态发生改变时的加速度变化对传感器内部的质量块/热气腔产生反作用力，敏感元件和测量电路能够精确地测量力的大小，从而得到加速度的变化。

根据加速度计的设计，加速度计分为动态型和动静态型两类。采用压电效应的加速度传感器只能感知加速度的“动态”变化，无法感知确定
静态时的物体姿态，此类传感器必须借助于姿态估算算法和动态加速度变化信息来确定物体的当前姿态；采用容变和热变的加速度传感器，
特殊的机械结构、敏感元件和测量电路设计使得他们不仅能感知加速度的动态变化，还能测量静态的姿态。基于中学的物理知识(力的分量和合成)，
结合下图我们就能想象得出加速度计的基本原理：

.. image:: /../../_static/images/bluefi_basics/acce_principle.jpeg
  :scale: 100%
  :align: center

此图仅展示一个方向的加速度变化和重力分量。事实上，我们在描述物体的加速度时总会先构建一个三维坐标系，加速度计会输出三个方向的加速度分量。
当然也有少部分加速度传感器只能给出x-、y-两个方向的加速度分量。所以加速度传感器又分为1D-、2D、3D的。

BlueFi采用3D的动静态型加速度计，即使在静止状态，BlueFi的加速度传感器也能给出自己的准确姿势。下面我们使用一个简单示例来观察BlueFi给出的
加速度变化信息。示例代码如下：

.. code-block::  python
  :linenos:

    import time
    from hiibot_bluefi.sensors import Sensors
    from hiibot_bluefi.screen import Screen
    screen = Screen()
    sensors = Sensors()
    acce = sensors.acceleration
    show_data = screen.simple_text_display(title="BlueFi Accelerations", title_scale=1, text_scale=2)
    while True:
        acce = sensors.acceleration
        show_data[2].text = "X: {:.2f}".format(acce[0])
        show_data[2].color = screen.RED
        show_data[3].text = "Y: {:.2f}".format(acce[1])
        show_data[3].color = screen.GREEN
        show_data[4].text = "Z: {:.2f}".format(acce[2])
        show_data[4].color = screen.BLUE
        show_data.show()
        time.sleep(0.1)

将本示例代码保存到BlueFi的/CIRCUITPY/code.py文件中，BlueFi在执行示例程序时，你可以尝试让BlueFi平躺、竖立、倒立、侧立等姿势
并观察三个加速度分量与姿态之间关系，并找出加速度每一个分量的最小值和最大值(加速度每一个分量的范围)。

示例代码分析：

    - 第1行，导入一个Python内建的模块“time”
    - 第2行，从“/CIRCUITPY/lib/hiibot_bluefi/sensors.py”模块中导入一个名叫“Sensors”的类
    - 第3行，从“/CIRCUITPY/lib/hiibot_bluefi/screen.py”模块中导入一个名叫“Screen”的类
    - 第4行，将导入的“Screen”类实例化为一个实体对象，名叫“screen”
    - 第5行，将导入的“Sensors”类实例化为一个实体对象，名叫“ensors”
    - 第6行，定义一个名叫“acce”的Sensors类acceleration型变量，并赋初值为sensors.acceleration
    - 第7行，定义一个名叫“show_data”的Screen类的多行文本显示子类，设置文本显示的标题为“BlueFi Accelerations”，标题字体放大1倍，文本字体放大2倍
    - 第8行，一个无穷循环的程序块
    - 第9行(无穷循环程序块的第1行)，用sensors.acceleration更新变量acce
    - 第10行(无穷循环程序块的第2行)，设置多行文本显示子类的第2行的文本内容为acce[0]的值
    - 第11行(无穷循环程序块的第3行)，设置多行文本显示子类的第2行的文本颜色为红色
    - 第12行(无穷循环程序块的第4行)，设置多行文本显示子类的第3行的文本内容为acce[1]的值
    - 第13行(无穷循环程序块的第5行)，设置多行文本显示子类的第3行的文本颜色为绿色
    - 第14行(无穷循环程序块的第6行)，设置多行文本显示子类的第4行的文本内容为acce[2]的值
    - 第15行(无穷循环程序块的第7行)，设置多行文本显示子类的第4行的文本颜色为蓝色
    - 第16行(无穷循环程序块的第8行)，更新多行文本显示
    - 第17行(无穷循环程序块的第9行)，执行time的sleep方法，参数为0.1秒

建议你设计数据记录表，将本示例给出的加速度三分量的值与姿态之间关系记录下来，然后根据这一关系确定姿态和加速度数据之间变化规律。


用RGB像素颜色来表示加速度变化
-----------------------------

BlueFi的5颗RGB像素彩灯是一种特殊的显示元件，响应速度快能呈现动感效果。在前一个示例中我们把加速度的三个分量的数值显示在LCD屏幕上，
当你旋转BlueFi改变其姿态时，观察屏幕的数值并不方便。那我们就想到其他的显示方式，譬如我们用5颗RGB像素灯珠发出的光颜色来指示加速度
的三个分量。巧合的是，BlueFi加速度传感器能给出三个分量值，而RGB像素灯珠的颜色也正好是三个分量。下面的示例程序中，我们将BlueFi的
加速度传感器三个分量分别映射为像素灯珠的RGB三基色的三个分量。示例代码如下：

.. code-block::  python
  :linenos:

    import time
    from hiibot_bluefi.sensors import Sensors
    from hiibot_bluefi.basedio import NeoPixel
    sensor = Sensors()
    pixels = NeoPixel()

    def map(v):
        return  abs( int((v/10.24)*255.0) )

    while True:
        x, y, z = sensor.acceleration
        pixels.fillPixels( ( map(x), map(y), map(z) ) )
        time.sleep(0.1)

很酷！这么短一点代码就能实现如此酷的效果。这个示例的程序结构已经被我们在前几节中反复使用过，我们定义来一个函数来处理
数据映射：把加速度的某个分量值(范围-10.24～+10.24)映射成RGB三基色某个分量(范围0~255)。下面是该示例程序的代码分析：

示例代码分析：

    - 第1行，导入一个Python内建的模块“time”
    - 第2行，从“/CIRCUITPY/lib/hiibot_bluefi/sensors.py”模块中导入一个名叫“Sensors”的类
    - 第3行，从“/CIRCUITPY/lib/hiibot_bluefi/basedio.py”模块中导入一个名叫“NeoPixel”的类
    - 第4行，将导入的“Sensors”类实例化为一个实体对象，名叫“ensor”
    - 第5行，将导入的“NeoPixel”类实例化为一个实体对象，名叫“pixels”
    - 第7行，定义一个名叫“map”的函数，输入参数是变量v
    - 第8行，函数map的程序块，直接返回“abs( int((v/10.24)*255.0) )”
    - 第10行，开始一个无穷循环
    - 第11行(无穷循环程序块的第1行)，将元组型sensor.acceleration加速度传感器的三分量分别赋给变量x,y,z
    - 第12行(无穷循环程序块的第2行)，分别将x,y,z映射为RGB三基色分量，并用这个三基色填充BlueFi的5颗RGB彩灯颜色
    - 第13行(无穷循环程序块的第3行)，执行time的sleep方法，参数为0.1秒

将本示例代码保存到BlueFi的/CIRCUITPY/code.py文件中，当BlueFi运行示例代码期间，试着改变BlueFi的姿态，你发现
5颗RGB像素的颜色与BlueFi姿态之间什么关系？

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
    - 本节中，你总计完成了37行代码的编写工作

------------------------------------

.. Important::
  **Sensors类的加速度传感器接口**

    - acceleration (属性, 元组类型, 只读, 每个分量的有效值: -10.24~+10.24), BlueFi的Sensors类acceleration属性, 加速度传感器的三个分量值

      - acceleration[0]: x方向分量
      - acceleration[1]: y方向分量
      - acceleration[2]: z方向分量

    - PedometerValue (属性, 只读, 有效值: 0~65535), BlueFi的Sensors类减速度传感器的计步器值属性
    - AcceRange (属性, 可读可写, 有效值: 0~3), BlueFi的Sensors类加速度传感器量程属性, 0:2g, 1:4g, 2:8g, 3:16g
    - AcceRate (属性, 可读可写, 有效值: 0~11), BlueFi的Sensors类加速度传感器数据更新率属性, 0:SD, 1:1.6Hz, 2:12.5Hz, 3:26Hz, .., 10:3.33Khz, 11:6.66KHz
    - enablePedometer (函数, 输入参数: 使能或禁止, 无返回值), BlueFi的Sensor类加速度传感器的计步器单元使能/禁用控制
    - shake (函数, 输入参数: 阈值, 采样次数, 延迟时间, 返回值: 0或1), BlueFi的Sensor类加速度传感器的振动检测, 返回1:有振动，0:无振动

