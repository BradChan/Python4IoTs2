改变RGB灯珠的颜色
======================

RGB像素灯珠串是非常有趣的一种输出，不仅可以用于照明和产生彩光，还能输出动态的流光溢彩的光效。

IoTs2上仅有1颗RGB彩色灯珠，虽然不能产生彩色灯珠串那种流光溢彩的光效，但仍可以利用这个灯珠产生有趣的光效。

如果你已经使用IoTs2一段时间了，相信你一定注意过IoTs2的RGB彩色灯珠，在IoTs2每次启动时该灯珠的颜色都会切换几次，
这些颜色代表不同的IoTs2状态，譬如显示紫色时此时按下Boot按钮将迫使IoTs2进入二级BootLoader状态(可更新Python固件)，
当显示黄色时按下Boot按钮将迫使IoTs2进入Python的安全模式(不执行我们的code.py程序)。
本节我们将掌握如何通过编程控制这个灯珠编程产生特殊的颜色。

------------------------------------

显示预制的彩光图案
------------------------------------

BlueFi单板机上只有5颗RGB像素灯珠，能够产生多种静态或动态的彩光效果，我们已经预制了4种动态的彩光效果，你只需要给定他们的的显示时间，
即可产生动态彩光效果。在BlueFi上运行下面示例程序，你将看到4种光效：

.. code-block::  python
  :linenos:

    import time
    from hiibot_bluefi.basedio import NeoPixel
    pixels = NeoPixel()
    pixels.brightness = 0.3
    while True:
        print("show rainbow")
        pixels.showAnimation_rainbow(4)
        pixels.clearPixels()
        time.sleep(1)
        print("show stars")
        pixels.showAnimation_star(4)
        print("show comet")
        pixels.showAnimation_comet(4)
        pixels.clearPixels()
        time.sleep(1)
        print("show wipe")
        pixels.showAnimation_wipe(4)
        pixels.clearPixels()
        time.sleep(1)

运行这个示例程序时，如果你的环境光较暗，可以调低RGB像素灯珠的亮度，即减小程序的第4行等号右边的值，避免眼睛盯着非常明亮的光源。

  示例代码分析：

    - 第1行，导入一个Python内建的模块“time”
    - 第2行，从“/CIRCUITPY/lib/hiibot_bluefi/basedio.py”模块中导入一个名叫“NeoPixel”的类
    - 第3行，将导入的“NeoPixel”类实例化为一个实体对象，名叫“pixels”
    - 第4行，设置pixels的brightness属性(即RGB像素彩灯的整体亮度)为0.3，合理取值范围：0.05(亮度最小)~1.0(亮度最大)
    - 第5行，开始一个无穷循环的程序块
    - 第6行(无穷循环程序块的第1行)，在LCD屏幕(控制台)上显示字符串“show rainbow”
    - 第7行(无穷循环程序块的第2行)，调用pixels的函数showAnimation_rainbow显示动态彩虹光效，并持续时间参数设为4秒
    - 第8行(无穷循环程序块的第3行)，调用pixels的函数clearPixels，清除所有像素的颜色(即关闭彩灯)
    - 第9行(无穷循环程序块的第4行)，执行time的sleep方法，参数为1秒，即系统空操作1秒
    - 第10行(无穷循环程序块的第5行)，在LCD屏幕(控制台)上显示字符串“show star”
    - 第11行(无穷循环程序块的第6行)，调用pixels的函数showAnimation_star显示星星眨眼光效，持续时间参数设为4秒
    - 第12行(无穷循环程序块的第7行)，在LCD屏幕(控制台)上显示字符串“show comet”
    - 第13行(无穷循环程序块的第8行)，调用pixels的函数showAnimation_comet显示彗星掠过光效，持续时间参数设为4秒
    - 第14行(无穷循环程序块的第9行)，调用pixels的函数clearPixels，清除所有像素的颜色(即关闭彩灯)
    - 第15行(无穷循环程序块的第10行)，执行time的sleep方法，参数为1秒，即系统空操作1秒
    - 第16行(无穷循环程序块的第11行)，在LCD屏幕(控制台)上显示字符串“show wipe”
    - 第17行(无穷循环程序块的第12行)，调用pixels的函数showAnimation_wipe显示进度条光效，持续时间参数设为4秒
    - 第18行(无穷循环程序块的第13行)，调用pixels的函数clearPixels，清除所有像素的颜色(即关闭彩灯)
    - 第19行(无穷循环程序块的第14行)，执行time的sleep方法，参数为1秒，即系统空操作1秒

我们所谓预制的光效，实际上是我们对BlueFi的每一个RGB像素灯珠的颜色进行编程，并通过移位实现动态光效，每一种光效我们在
NeoPixel类中定义一个对应的接口(函数)，使用时只需调用对应的函数，并指定持续显示光效时间长度即可。你可以参考这个类中的
这些接口设计更多种光效程序模块，用import的方法导入自己的其他Python程序中使用。


自制的彩光图案
------------------------------------

下面我们使用Python语言的列表(list)型变量定义BlueFi的5个RGB像素灯珠的颜色列表，然后显示出来，并逐位移动他们，产生自定义的光效。
示例程序如下：

.. code-block::  python
  :linenos:

    import time
    from hiibot_bluefi.basedio import NeoPixel
    pixels = NeoPixel()
    pixels.brightness = 0.2
    colors = [ (255,0,0), (127,127,0), (0,255,0), (0,127,127), (0,0,255) ]
    pixels.drawPattern(colors)
    while True:
        pixels.shiftRight()
        time.sleep(0.2)

在BlueFi上执行本示例程序，你会看到流动的光带效果，如果你改变程序最后一个语句(time.sleep(0.2))中的时间参数，并重新保存到
/CIRCUITPY/code.py中，将会看到不同的色彩运动效果。

  示例代码分析：

    - 第1行，导入一个Python内建的模块“time”
    - 第2行，从“/CIRCUITPY/lib/hiibot_bluefi/basedio.py”模块中导入一个名叫“NeoPixel”的类
    - 第3行，将导入的“NeoPixel”类实例化为一个实体对象，名叫“pixels”
    - 第4行，设置pixels的brightness属性(即RGB像素彩灯的整体亮度)为0.2，合理取值范围：0.05(亮度最小)~1.0(亮度最大)
    - 第5行，定义一个颜色列表变量，变量名叫colors，含5个元组型变量分别指定每个像素的三基色
    - 第6行，调用pixels的函数drawPattern，并将颜色列表colors作为输入参数，在BlueFi显示出5种颜色
    - 第7行，开始一个无穷循环的程序块
    - 第8行(无穷循环程序块的第1行)，调用pixels的函数shiftRight，让5个RGB像素灯珠的颜色循环右移一次
    - 第9行(无穷循环程序块的第4行)，执行time的sleep方法，参数为0.2秒，即系统空操作0.2秒

在本示例程序的第5行，我们使用元组“(R value, G value, B value)”定义单个RGB像素灯珠的颜色，即通过指定三基色的3个分量。
并使用这样的5个元组分别指定5个灯珠的颜色，这样5个元组组成一个颜色列表。

这一句程序中，我们用到的“()”和“[]”必须是成对儿的，也就是封闭的。其中“()”和内部的变量或数值组成“元组”，元组型变量常用于表示
颜色、坐标、速度等物理量，这些物理量都至少包含2个分量，而且每个分量的数据类型是相同的，譬如本示例中用到三基色元组，每个基色分量
都是一个数值；“[]”和内部的变量组成“列表”，列表型变量能够包含更多种不同的信息，本示例使用了最简单的一种列表，列表中的每一项都是
相同的：颜色元组。

虽然使用颜色列表和三基色元组定义自制图案非常方便，只需要用colors单个变量就可以把整个彩色图案传给pixels的函数drawPattern，
当然这不是惟一的方法，信息的组织和结构定义始终是计算机科学领域的一项持续研究的、不断进步的工作，随着我们的信息量越来越大、信息
结构越来越复杂，我们就需要更高效的信息组织和结构方法。

你可以使用pixels的shiftLeft函数让彩色图案左移，试一试并观察左移和右移的效果。现在我们每次只是移动1位，你能自己编写程序实现
每次移动2位或更多位吗？


用RGB像素灯珠画柱状图
------------------------------------

BlueFi上的并排5个彩灯可以实现很多种光效，最酷的应该是动态柱状图指示变量的变化，不仅直观而且彩色光柱让人印象深刻。如下示例：

.. code-block::  python
  :linenos:

    import time
    from hiibot_bluefi.basedio import NeoPixel
    from hiibot_bluefi.soundio import SoundIn
    pixels = NeoPixel()
    pixels.brightness = 0.2
    mic = SoundIn()
    vmin = mic.sound_level
    vmax = vmin+500
    while True:
        pixels.drawPillar(mic.sound_level, vmin, vmax)
        time.sleep(0.01)

当你把本示例程序保存为/CIRCUITPY/code.py文件后，播放节奏明显的音乐、敲桌子等方式制造点很有节奏的动静，你会发现BlueFi灯珠上
彩色光柱几乎完全与节奏同步跳动，效果非常有趣。

  示例代码分析：

    - 第1行，导入一个Python内建的模块“time”
    - 第2行，从“/CIRCUITPY/lib/hiibot_bluefi/basedio.py”模块中导入一个名叫“NeoPixel”的类
    - 第3行，从“/CIRCUITPY/lib/hiibot_bluefi/soundio.py”模块中导入一个名叫“SoundIn”的类
    - 第3行，将导入的“NeoPixel”类实例化为一个实体对象，名叫“pixels”
    - 第4行，设置pixels的brightness属性(即RGB像素彩灯的整体亮度)为0.2，合理取值范围：0.05(亮度最小)~1.0(亮度最大)
    - 第3行，将导入的“SoundIn”类实例化为一个实体对象，名叫“mic”
    - 第5行，定义一个变量名叫vmin，并使用mic的属性值sound_level(麦克风感知到的声音高低)作为初始值
    - 第6行，定义一个变量名叫vmax，并使用“vmin+500”作为初始值
    - 第7行，开始一个无穷循环的程序块
    - 第8行(无穷循环程序块的第1行)，调用pixels的函数drawPillar，使用mic的属性值(麦克风感知到的声音高低)作为变量画柱状图，且最小值为vmain和最大值为vmax
    - 第9行(无穷循环程序块的第4行)，执行time的sleep方法，参数为0.01秒，即系统空操作10毫秒

关于BlueFi的SoundIn类和数字麦克风传感器的用法，后续将会详细说明，此处只是使用SoundIn类的属性值(麦克风感知到的声音高低).


需要更多个RGB像素灯珠
------------------------------------

有时你需要更多个RGB像素灯珠，BlueFi的5个灯珠完全不够你使用，怎么办？

BlueFi支持你自购兼容WS2812B的RGB像素灯珠串，并准备烙铁、焊锡丝、彩色电线、3.3V/5V直流电源等辅材，自己动手很容易将自购的彩灯串接入BlueFi，使用
上面相同示例程序控制更多彩灯串产生绚丽多彩的光效。自购RGB像素灯珠时，务必注意需要兼容WS2812B型灯珠，工作电压必须兼容5V和3.3V！
按照下图的示意连接更多个彩色灯珠串。

.. image:: /../../_static/images/bluefi_basics/pixels_more.jpg
  :scale: 40%
  :align: center

在BlueFi正面5个RGB像素灯珠的右侧预留有级连灯珠串的数据输出信号焊盘，如图所示位置。使用烙铁和电线等辅材将这个焊盘与自购的灯珠串的
Din信号焊盘可靠地连接起来，并将灯珠串的V+和3.3V或5V直流电源的V+连接，Gnd与电源Gnd连接。如果需要继续级连下另一串灯珠，只需要将
前一串灯珠的Dout与下一串灯珠的Din连接，电源仍保持一一对应的正确连接即可。

.. Attention::
  
  - 焊接或连接电路时，务必先切断所有电路单元的供电，确保连接正确后再通电
  - 如果你的灯珠串不大于20个，你可以使用BlueFi的40-Pin拓展接口上的3V和Gnd电源为你自购的灯珠串供电，但务必注意亮度不宜过高
  - BlueFi内部供电电路能持续地输出最大1.5A电流，除去给板上的电路单元供电外，可以为外部负载供电。负载电流超过电源最大输出电流时，很容易损坏供电系统

如果使用BlueFi的3V和Gnd输出的3.3V电源为自购灯珠供电，你还需要用到鳄鱼夹电线等辅材。当我们把电路单元连接妥当之后，我们使用下面
示例程序控制这些彩灯产生特定光效：

.. code-block::  python
  :linenos:
    
    import time
    from hiibot_bluefi.basedio import NeoPixel
    pixels = NeoPixel(numPixels=5+10)
    pixels.brightness = 0.3
    while True:
        print("show rainbow")
        pixels.showAnimation_rainbow(4)
        pixels.clearPixels()
        time.sleep(1)
        print("show stars")
        pixels.showAnimation_star(4)
        print("show comet")
        pixels.showAnimation_comet(4)
        pixels.clearPixels()
        time.sleep(1)
        print("show wipe")
        pixels.showAnimation_wipe(4)
        pixels.clearPixels()
        time.sleep(1)

哈哈！这不就是本节的第一个示例程序吗！不完全是，我们只是修改了第3行程序，即实例化NeoPixel类的方法略作修改。
原来的实例化方法是“pixels = NeoPixel()”，修改后的实例化方法是“pixels = NeoPixel(numPixels=5+10)”。修改实例化方法的目的是，
指定灯珠串上灯珠的个数为“5+10”，假设你额外级连了10个兼容WS2812B的RGB像素灯珠，加上BlueFi固有的5个，总计15个像素灯珠，把这个数值赋给
NeoPixel类的变量numPixels。

也就是说，实例化NeoPixel类的时候不指定类成员变量numPixels的值，默认为5，当我们额外级连了10个灯珠，就需要指定该变量为15。NeoPixel类
的其他变量、属性和接口函数的用法不变。

.. admonition:: 
  总结：

    - RGB像素灯珠
    - RGB三基色
    - 子类
    - 变量赋值
    - 变量自增/自减
    - 逻辑判断和逻辑程序块
    - 本节中，你总计完成了19行代码的编写工作

------------------------------------


.. Important::
  **NeoPixel类的接口**

    - pixels (子类), BlueFi的NeoPixel子类
    - num_pixels (属性, 只读, 有效值：5或更多), BlueFi的RGB像素灯珠的个数
    - brightness (属性, 可读可写, 有效值：0.0～1.0), BlueFi的RGB像素灯珠串的整体亮度
    - clearPixels (函数, 无输入参数, 无返回值), 关闭BlueFi的所有RGB像素灯珠
    - fillPixels (函数, 输入参数：三基色分量的元组, 无返回值), 让BlueFi的所有RGB像素灯珠显示指定的颜色
    - drawPattern (函数, 输入参数:5或更多颗灯珠的颜色列表, 无返回值), 让BlueFi的RGB像素灯珠显示给定的图案
    - shiftRight (函数, 无输入参数, 无返回值), 让BlueFi的RGB像素灯珠显示的图案循环右移一步
    - shiftLeft (函数, 无输入参数, 无返回值), 让BlueFi的RGB像素灯珠显示的图案循环左移一步
    - drawRainbow (函数, 输入参数: 彩虹颜色序号, 无返回值), 让BlueFi显示彩虹图案(第n步), 0 <= n <= 255
    - showAnimation_star (函数, 输入参数: 持续时间t, 无返回值), 让BlueFi显示星星眨眼效果的预制图案, 并持续t秒
    - showAnimation_rainbow (函数, 输入参数: 持续时间t, 无返回值), 让BlueFi显示移动彩虹效果的预制图案, 并持续t秒
    - showAnimation_comet (函数, 输入参数: 持续时间t, 无返回值), 让BlueFi显示彗星掠过效果的预制图案, 并持续t秒
    - showAnimation_wipe (函数, 输入参数: 持续时间t, 无返回值), 让BlueFi显示进度条效果的预制图案, 并持续t秒
    - drawPillar (函数，输入参数: 变量v, 变量最小值, 变量最大值, 峰值颜色元组), 用变量v的值画柱状图