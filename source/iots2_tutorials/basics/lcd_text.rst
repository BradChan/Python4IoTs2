使用LCD显示器显示文本
======================

BlueFi正面有一个1.3寸的彩色LCD屏幕，分辨率为240x240点阵，点间距和像素点都很小，这个屏幕几何达到视网膜级别(据说iPhone和iPad
都采用视网膜级别的显示器)，显示文字或图案时非常细腻。在准备阶段我们已经介绍过BlieFi的LCD屏幕的用途，他是我们的控制台，无论任何
时候只要脚本程序遇到错误停止执行时，详细的错误提示信息都会显示在这个屏幕上，方便我们快速排查问题所在，这一功能在执行Python等脚本
程序的计算机相同中尤为重要。

控制台只接受“print()”方法输出的信息和相同的提示信息等，如果用户编程需要使用LCD屏幕显示自己订制的信息，那就需要进一步了解BlueFi
的LCD屏幕的用法。本节仅介绍如何显示简单的文本，虽然只是文本显示，但是颜色、字体大小和位置等都是可编程的。

-----------------------

把文字放大显示
-----------------------

用本节的第一个示例程序来回复“BlueFi的显示文字太小”，当我们把LCD屏当作控制台使用使用时，其显示的相同提示等信息尽可能多，
采用越大的字体意味着整屏能显示的信息就更少，当你嫌控制台信息的字体过小时，那就不用“print()”来show自己的程序输出，参考
本示例的方法，相信可以满足你的“显示大文字”需求。示例程序如下：

.. code-block::  python
  :linenos:

    import time
    from hiibot_bluefi.basedio import Button
    from hiibot_bluefi.soundio import SoundIn
    from hiibot_bluefi.screen import Screen
    button = Button()
    mic = SoundIn()
    screen = Screen()
    show_data = screen.simple_text_display(title="BlueFi LCD", title_scale=2, text_scale=2)
    while True:
        show_data[2].text = "A:{}".format(button.A)
        show_data[3].text = "B:{}".format(button.B)
        show_data[5].text = "SoundIn:{:.1f}".format(mic.sound_level)
        show_data.show()
        time.sleep(0.1)

将本示例程序保存到BlueFi到/CIRCUITPY/code.py文件，执行程序的显示效果与控制台的显示效果做一个对比：

.. image:: /../../_static/images/bluefi_basics/lcd_font_zoom.jpg
  :scale: 40%
  :align: center

本示例程序中，我们将显示的文字在放大2倍后才显示。下面来分析本示例程序。

示例代码分析：

    - 第1行，导入一个Python内建的模块“time”
    - 第2行，从“/CIRCUITPY/lib/hiibot_bluefi/basedio.py”模块中导入一个名叫“Button”的类
    - 第3行，从“/CIRCUITPY/lib/hiibot_bluefi/soundio.py”模块中导入一个名叫“SoundIn”的类
    - 第4行，从“/CIRCUITPY/lib/hiibot_bluefi/screen.py”模块中导入一个名叫“Screen”的类
    - 第5行，将导入的“Button”类实例化为一个实体对象，名叫“button”
    - 第6行，将导入的“SoundIn”类实例化为一个实体对象，名叫“mic”
    - 第7行，将导入的“Screen”类实例化为一个实体对象，名叫“screen”
    - 第8行，定义一个名叫“show_data”的Screen类的多行文本显示子类，设置文本显示的标题为“BlueFi LCD”，标题字体放大2倍，文本字体放大2倍
    - 第9行，一个无穷循环的程序块
    - 第10行(无穷循环程序块的第1行)，设置多行文本显示子类的第2行的文本内容为A按钮状态
    - 第11行(无穷循环程序块的第2行)，设置多行文本显示子类的第3行的文本内容为B按钮状态
    - 第12行(无穷循环程序块的第3行)，设置多行文本显示子类的第5行的文本内容为麦克风感知到的声音变化强弱
    - 第13行(无穷循环程序块的第4行)，更新多行文本显示
    - 第14行(无穷循环程序块的第5行)，执行time的sleep方法，参数为0.1秒

第8行是本示例程序的重点，我们使用Screen类的一个名叫simple_text_display子类，即实现多行简单文本显示的一组方法，使用这个子类允许你
定义多行简单文本显示的所用的字体、标题、标题字的缩放倍数(默认为标准字体的2倍)、标题颜色，以及多行文本的字体缩放倍数(默认为标准字体)、颜色等。
定义simple_text_display子类的接口原型：

.. code-block::  python
  :linenos:

    def simple_text_display(  
        title=None,                   # title
        title_color=(255, 255, 255),  # title_color
        title_scale=1,                # title_scale
        text_scale=1,                 # text_scale
        font=None,                    # used font
        colors=None,                  # list of text_color
    ):

在本示例程序的“while True:”程序块内，前三行程序分别是指定三行文本的显示内容(我们把拟显示的变量格式为字符串用来显示)，show_data[i].text
表示第i行文本的内容。调用show_data.show()函数只是更新多行文本显示到屏幕上。


调整屏幕亮度和屏保
-----------------------

如果你想了解Screen类的接口都有那些，直接滑到本页最底部，我们已经把所有接口都列举在那里，供参考。细心的你或许早就发现，在入门级教程中，每一节
教程的最底部都包含有所用类的接口列表。当然，你也可以让BlueFi进入REPL模式，通过导入模块或类，使用“help(className)”、“dir(className)”、
“className.”并按Tab键来了解className类的接口。

BlueFi的Screen类中包含有几个很重要的属性：width(BlueFi屏幕宽度)、height(BlueFi屏幕高度)、rotation(BlueFi屏幕旋转)和brightness
(BlueFi屏幕亮度)。前两个属性是固定值，由BlueFi所用屏幕的物理参数确定，旋转屏幕是根据自己的需要来决定，如果你想直到当前的旋转角度，只需要
将screen.rotation值打印出来就知道了。屏幕亮度属性——brightness非常重要，如果你的BlueFi已经运行了很长时间，期间未关闭过屏幕显示，你可以
用手指去触摸显示屏能明显感觉到温度。LCD显示屏的是一种被动显示器，屏幕本身不会发光，必须借助于外接光源才能看到屏幕上的字。因此，绝大多数LCD
屏幕都会带着一个背光板，一种面积跟LCD屏幕完全相同的平面光源，光源被置于LCD屏幕后面。LCD屏背光板是功耗较大的电子元件，而且寿命也比较短，尤其
是随着使用时间的增加，背光板的亮度将逐渐降低。为了节能，大部分时间我们不需要看LCD显示屏的内容时，我们应该关闭LCD屏幕后面的背光板。

.. code-block::  python
  :linenos:

    import time
    from hiibot_bluefi.basedio import Button, NeoPixel
    from hiibot_bluefi.soundio import SoundIn
    from hiibot_bluefi.screen import Screen
    button = Button()
    mic = SoundIn()
    screen = Screen()
    delayCnt=500

    def screenSave():
        global delayCnt
        time.sleep(0.01)
        if delayCnt<=0:
            screen.brightness = 0 # close backlight
        else:
            delayCnt -= 1
            if delayCnt<50:
                screen.brightness = 0.2
            elif delayCnt<100:
                screen.brightness = 0.5    

    pixels = NeoPixel()
    pixels.clearPixels()
    show_data = screen.simple_text_display(title="BlueFi Text Lines", title_scale=1, text_scale=2)
    while True:
        screenSave()
        show_data[2].text = "A:{}".format(button.A)
        show_data[3].text = "B:{}".format(button.B)
        sl = mic.sound_level
        show_data[5].text = "SoundIn:{:.1f}".format(sl)
        show_data.show()
        if button.A or button.B or sl>500:
            delayCnt = 500
            screen.brightness = 1.0

我们首先来描述以下上面示例程序的执行效果，你也可以跳过这段文字，直接把这个程序保存到/CIRCUITPY/code.py文件中执行，观察执行效果。
运行本示例程序期间如果你的周围环境无噪音(相对比较安静)，也不触碰A和B按钮，大约6秒之后，BlueFi的LCD屏幕自动关闭，实际上是背光板
的光源被关闭，我们就看不到LCD屏幕上的文字。如果你吹一下口哨或拍拍巴掌等制造较大的声音，你会发现LCD屏自动亮起，按下A或B按钮也会看到
相同的情况。

这个程序看起来很长(34行代码!)，不过很好理解，我们只是在前一个示例的基础上增加一个自动进入/退出屏保的功能。主要修改是增加一个名叫
“screenSave”的无参数无返回值的函数，在无穷循环程序块内调用该函数实现自动进入屏保的业务。并在程序的最后增加3行语句实现，按下
按钮A或B、或麦克风感知到很大的声音时，自动退出屏保打开显示屏。第31行程序语句中采用三个条件的或逻辑，满足任何一个条件时，重置变量
delayCnt为500，并设置屏幕背光板亮度为最大(1.0)。在screenSave函数中不断地将变量delayCnt自减1，降到100以下时让屏幕亮度保持为
50%；降至50以下时亮度保持20%；降至0时亮度也设为0，即进入屏保。保持BlueFi处于屏保状态一段时间，你再用手指触摸LCD屏幕，感知他的
温度，判断屏保的节能效果。


.. admonition:: 
  总结：

    - LCD显示器
    - LCD显示器背光板的亮度和屏保
    - 多行文本显示的数据结构
    - 文本字体的缩放
    - 函数及其定义和调用
    - 全局变量和局部变量
    - 本节中，你总计完成了34行代码的编写工作

------------------------------------


.. Important::
  **Screen类的接口**

    - display (子类), BlueFi的Screen子类
    - width (属性, 只读, 有效值：240), BlueFi的Screen类属性，屏幕宽度(x-)方向的像素个数
    - height (属性, 只读, 有效值：240), BlueFi的Screen类属性，屏幕高度(y-)方向的像素个数
    - rotation (属性, 可读可写, 有效值: 0/90/180/270), 旋转BlueFi的LCD屏幕的方向控制
    - brightness (属性, 可读可写, 有效值: 0.0~1.0), BlueFi的LCD屏幕的亮度控制
    - show (函数, 输入参数: 指定显示内容, 无返回值), 将某些指定的内容显示在BlueFi的LCD屏上
    - simple_text_display (子类), 用于控制BlueFi的LCD屏幕显示多行文本

      - show (多行文本显示子类的函数, 无参数, 无返回值), 更新多行文本显示的内容到屏幕上
      - show_terminal (多行文本显示子类的函数, 无参数, 无返回值), 关闭多行文本显示并返回控制台状态 