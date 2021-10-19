=========================
使用IoTs2的LCD显示器
=========================

IoTs2配置有一个240x135点阵的1.14英寸彩色LCD显示器，这个小显示屏的点阵密度几乎接近视网膜屏，即使采用很小的字体的情况下仍保持字符和图案的清晰度。
IoTs2处于Bootloader模式时，显示屏自动关闭。进入Python模式时，执行code.py或main.py程序时，IoTs2的LCD显示器由用户程序掌控，
停止Python代码执行或进入REPL模式，这个显示屏与串口控制台几乎完全同步。

IoTs2的LCD显示器主要有以下几种用法：

----------------------------------

1. 作为用户程序的一种输出设备
----------------------------------

这个模式下，只要code.py或main.py程序启动时，屏幕会显示一行提示：“code.py output:”(或 “main.py output:”)，
提醒我们屏幕的内容都是由code.py或main.py执行结果。譬如，我们编写一个最简单的程序：

.. code-block::  python
   :linenos:

    print("hello world")
    print("i'am IoTs2")

将这个输出两行文本到控制台的脚本程序保存到/CIRCUITPY/code.py文件，如果IoTs2已经与宿主计算机上MU编辑器链接好，点击“串口”按钮，
你在串口控制台的窗口中将会看到以下提示信息：

    Auto-reload is on. Simply save files over USB to run them or enter REPL to disable.

    code.py output:

    hello world

    I'm IoTs2将会想控制台输出内建的

    Press any key to enter the REPL. Use CTRL-D to reload.


“Auto-reload is on. Simply save files over USB to run them or enter REPL to disable.”这一行信息提示我们，
IoTs2开始自动加载用户程序(code.py)，禁用REPL；
“code.py output:”这一行信息表示，开始执行code.py程序，启动code.py程序时，IoTs2的Python解释器自动给出的提示信息；
“hello world”和“I'm IoTs2”是我们编写的code.py程序中的两个语句所输出的结果；
“Press any key to enter the REPL. Use CTRL-D to reload.”这一行信息表示，code.py程序已经执行完毕，按任意键进入REPL模式，
按“Ctrl+D”键重新执行code.py程序。

你在IoTs2的LCD屏幕上也能看到这些信息，而且完全相同。通过这个示例我们看到，IoTs2的LCD显示器相当于一个小型控制台，
用户程序“print("xxx")”的输出都被作为一整行显示出来，如果文本内容超过一行，并自动换行继续显示。当开始启动用户程序或执行完毕后，
系统的提示信息也被显示在LCD上。

我们再来看另外一个示例，Python脚本程序如下：

.. code-block::  python
   :linenos:

    # 从adafruit_turtle中导入turtle画笔模块和颜色模块
    from adafruit_turtle import Color, turtle
    # 从hiibot_iots2模块或hiibot_iots2v2模块中导入IoTs2类，该类的"screen"接口即为显示屏
    #from hiibot_iots2 import IoTs2
    from hiibot_iots2v2 import IoTs2  # IoTs2v2 be used
    # 实例化Screen模块类为screen
    iots2 = IoTs2()
    screen = iots2.screen
    colors = [Color.ORANGE, Color.PURPLE]
    # 实例化turtle画笔为turtle, 并使用screen作为显示器
    turtle = turtle(screen)
    # 落笔
    turtle.pendown()
    # 循环200次
    for x in range(200):
        turtle.pencolor(colors[x % 2])
        turtle.forward(x)
        turtle.left(91)

    while True:
        pass

看起来这个示例程序蛮长，其实并不复杂，尤其你如果使用过Scratch的画笔模块、Python的turtle模块，这里所用的turtle模块用法几乎与他们完全相同。
当然这个时候我们并不关心程序的具体细节。将程序代码复制到MU编辑器中，并保存到/CIRCUITPY/code.py文件中，等待几秒看IoTs2的LCD屏幕输出就可以。

在这个示例中，我们看不到系统的提示信息，只是看到code.py程序的执行结果：在LCD屏幕上绘制了一个彩色图案。这是因为本示例的第6行程序将IoTs2的
LCD显示器当作turtle画笔的输出设备使用，画笔程序绘制的几何图案被显示在LCD屏幕上，但系统提示等文本信息就不会显示在这里。

如果你将程序的最后两行(第18行和第19行)删除了，包保存到/CIRCUITPY/code.py文件，再观察执行结果的屏幕显示是什么内容？你认为这是什么原因？


----------------------------------

2. 输出脚本程序的错误信息
----------------------------------

脚本程序的执行过程是“逐行执行并输出结果”的串行模式。如果我们编写的一个10行的脚本程序，前5行程序没有任何错误，第6行程序有一个拼写错误。执行
这个脚本程序的效果是，执行到第6行包含拼写错误的语句时，脚本解释器无法执行，于是直接终止程序执行，并输出错误信息的提示，无论第7～10行程序是否
正确都不会被执行。

以下面程序为例，复制下面代码到MU编辑器中，并保存到/CIRCUITPY/code.py文件：

.. code-block::  python
   :linenos:

    from adafruit_turtle import Color, turtle
    #from hiibot_iots2 import IoTs2
    from hiibot_iots2v2 import IoTs2  # IoTs2v2 be used
    iots2 = IoTs2()
    screen = iots2.screen
    colors = [Color.ORANGE, Color.PURPLE]
    turtle = turtle(screen)
    turtle.pen()
    for x in range(200):
        turtle.pencolor(colors[x % 2])
        turtle.forward(x)
        turtle.left(91)

第6行程序的正确拼写为“turtle.pendown()”，但是上面程序中被我们错误拼写为“turtle.pen()”。IoTs2在执行这个包含错误拼写的程序时，会出现以下提示：

    Auto-reload is on. Simply save files over USB to run them or enter REPL to disable.

    code.py output:

    Traceback (most recent call last):

      File "code.py", line 6, in <module>

      AttributeError: 'turtle' object has no attribute 'pen'

    Press any key to enter the REPL. Use CTRL-D to reload.

显然，第4和第5行提示信息中已经明确地告诉我们错误的语句是第几行，错误的原因是turtle对象没有pen这个属性。

IoTs2的LCD显示器虽然很小，但是作用很大！尤其执行Python脚本程序的过程中，动态地加载和执行一些存在错误的模块，终止脚本程序的执行，并提示
发声错误的位置和错误原因，很容易帮助我们排查错误。如果没有这样的显示和提示机制，程序被终止后编程者就很难定位问题。任何时候，只要用代码编写
程序，各种各样的错误是难免的，如果能快速地定位问题，编写代码、调试程序的效率将大大地提升。







