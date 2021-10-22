使用LCD显示器显示文本
========================

IoTs2有一个1.14寸的彩色LCD屏幕，分辨率为240x135点阵，点间距和像素点都很小，
这个屏幕几何达到视网膜级别(据说iPhone和iPad都采用视网膜级别的显示器)，
视网膜级显示器上显示文字或图案时非常细腻。在准备阶段我们已经介绍过IoTs2的LCD屏幕的用途，他是我们的控制台，
无论任何时候只要脚本程序遇到错误停止执行时，详细的错误提示信息都会显示在这个屏幕上，方便我们快速排查问题所在，
这一功能在执行Python等脚本程序的计算机相同中尤为重要。

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
  import displayio
  import terminalio
  from adafruit_display_text import label 
  from hiibot_iots2 import IoTs2
  iots2 = IoTs2()
  text_group = displayio.Group(scale=2)
  text0 = label.Label(terminalio.FONT, x=0, y=0,  text="", max_glyphs=24,  color=(255,0,0))
  text1 = label.Label(terminalio.FONT, x=0, y=9,  text="", max_glyphs=24, color=(192,63,0))
  text2 = label.Label(terminalio.FONT, x=0, y=18, text="", max_glyphs=24,  color=(127,127,0))
  text3 = label.Label(terminalio.FONT, x=0, y=27, text="", max_glyphs=24,  color=(0,255,0))
  text4 = label.Label(terminalio.FONT, x=0, y=36, text="", max_glyphs=24,  color=(0,127,127))
  text5 = label.Label(terminalio.FONT, x=0, y=45, text="", max_glyphs=24,  color=(0,0,255))
  text6 = label.Label(terminalio.FONT, x=0, y=54, text="", max_glyphs=24,  color=(127,0,127))
  text7 = label.Label(terminalio.FONT, x=0, y=63, text="", max_glyphs=24,  color=(255,0,0))
  labelList = [text0, text1, text2, text3, text4, text5, text6, text7]
  for i in range(8):
      text_group.append(labelList[i])
  iots2.screen.show(text_group)
  stateList = ['Released', 'Pressed']
  while True:
      stateBtn = iots2.button_state
      str = "button: {:d} / {}".format(stateBtn, stateList[stateBtn])
      for i in range(8):
          labelList[i].text = str
      time.sleep(0.02)

将本示例程序保存到IoTs2到/CIRCUITPY/code.py文件，执行程序的显示效果与控制台的显示效果相对比，你会发现文本字体明显变大，
这是因为本示例程序的第7行中“scale”参数为2，该参数的有效值是1或2的整数倍，如果我们将该参数修改为1，你会发现什么现象？

下面来分析本示例程序。示例代码分析：

    - 第1行，导入一个Python内建的模块“time”
    - 第2行，导入一个Python内建的模块“displayio”
    - 第3行，导入一个Python内建的模块“terminalio”
    - 第4行，从“adafruit_display_text”模块中导入“label”类
    - 第5行，从“/CIRCUITPY/lib/hiibot_iots2.py”模块中导入“IoTs2”类
    - 第6行，将导入的“IoTs2”类实例化为一个实体对象，名叫“iots2”
    - 第7行，创建一个“displayio”的“Group”类的实体对象，即一组显示内容，名叫“text_group”，该组最多有8个显示内容，且字体放大2倍
    - 第8～15行，分别定义一个文本标签(Label)，所有文本标签的字体都是“terminalio.FONT”类型、最多字符个数为24，每个标签的坐标(x,y)和颜色分别指定
    - 第16行，将定义好的8个文本标签组成一个列表便于后面使用遍历列表的方法来访问每个标签
    - 第17～18行，定义一个8次的循环，遍历标签列表将列表中的文本标签逐个添加到“text_group”中
    - 第19行，将“text_group”作为显示对象传递给“iots2.screen.show”接口，目的是将“text_group”显示在IoTs2的LCD屏幕上
    - 第20行，定义一个字符串列表用来存储按钮的两个状态对应的字符串
    - 第21行，一个无穷循环的程序块
    - 第22行(无穷循环程序块的第1行)，将IoTs2的可编程按钮的当前状态保存在变量“stateBtn”中
    - 第23行(无穷循环程序块的第2行)，将按钮状态和描述该状态的字符串格式化成一个字符串，并赋给变量“str”
    - 第24～25行(无穷循环程序块的第3～4行)，定义一个8次的循环，将“str”当作标签的文本内容赋给标签列表中的每一项
    - 第26行(无穷循环程序块的第5行)，执行time的sleep方法，参数为0.02秒

在本示例中，“displayio”模块是最重要的Python内建库，使用这个库方便设计屏幕上多种显示内容的布局，虽然本示例仅仅显示多行文本。
“displayio”库的基本思路是，将一屏内要显示的所有内容称作一个“group”，一个显示屏(如本示例中的iots2.screen)只能显示一个“group”内容，
因此我们需要把多种显示内容添加到一个“group”中(如本示例中将8个文本行逐个添加到“text_group”中[第17～18行])。
当然“displayio”库支持“group”中包含其他“group”(准确地说是“sub-group”)，这样我们就可以把文本、图案、图片等按“group”形式分别组织好，
然后再添加到一个大的“group”中，最后再交给一个显示器上show出来。关于“displayio”更多的用法，我们将在高级向导中专门介绍。

上面示例的8个文本行都是一样的层次，有时候我们需要显示文本标题，该如何处理呢？文本标题和普通文本的主要区别是字体、字体大小等。
我们对上面示例代码稍作修改，即可实现文本标题的显示效果，我们假设文本标签“text0”是标题，标题字体是其他文本的字体的2倍。
注意，前面示例中所有文本的字体大小都是标准字体的2倍，如果标题字体大小是其他文本行字体大小的2倍，那么标题字体是标准字体的4倍，
意味着标题行占用更多的屏幕空间。修改后的代码如下：

.. code-block::  python
  :linenos:

  import time
  import displayio
  import terminalio
  from adafruit_display_text import label
  from hiibot_iots2 import IoTs2
  iots2 = IoTs2()
  text_group = displayio.Group(scale=2)
  text0 = label.Label(terminalio.FONT, x=8, y=6,  text="Hi, IoTs2", scale=2, max_glyphs=24,  color=(255,0,0))
  text1 = label.Label(terminalio.FONT, x=0, y=20, text="", max_glyphs=24, color=(192,63,0))
  text2 = label.Label(terminalio.FONT, x=0, y=29, text="", max_glyphs=24,  color=(127,127,0))
  text3 = label.Label(terminalio.FONT, x=0, y=38, text="", max_glyphs=24,  color=(0,255,0))
  text4 = label.Label(terminalio.FONT, x=0, y=47, text="", max_glyphs=24,  color=(0,127,127))
  text5 = label.Label(terminalio.FONT, x=0, y=56, text="", max_glyphs=24,  color=(0,0,255))
  text6 = label.Label(terminalio.FONT, x=0, y=65, text="", max_glyphs=24,  color=(127,0,127))
  testList = [text0, text1, text2, text3, text4, text5, text6]
  for i in range(7):
      text_group.append(testList[i])
  iots2.screen.show(text_group)
  stateList = ['Released', 'Pressed']
  while True:
      stateBtn = iots2.button_state
      str = "button: {:d} / {}".format(stateBtn, stateList[stateBtn])
      for i in range(1,7):
          testList[i].text = str
      time.sleep(0.02)

修改的示例程序中，文本标签“text0”的（x,y)坐标、缺省的文本内容、字体放大倍数为2(再乘以整个“group”的放大倍数2，即为标准字体的4倍)等做了修改。
此外，由于“text0”占用更大的屏幕空间，我们去掉前示例中的“text7”(即第8行)文本标签。

修改前后的IoTs2显示效果如下图所示：

.. image:: /../../_static/images/iots2_tutorials/iots2_displayio_label_font_zoom.jpg
  :scale: 5%
  :align: center

对于“adafruit_display_text”模块的“label”类，其详细的属性和参数见“https://circuitpython.readthedocs.io/projects/display_text/en/latest/api.html?highlight=label”。
在这里需要稍作说明，便于理解前面的示例代码。“label”类的原型和默认参数为：

.. code-block::  python
  :linenos:

  class adafruit_display_text.label.Label(font, *, x=0, y=0, text='', max_glyphs=None, color=16777215, background_color=None, line_spacing=1.25, background_tight=False, padding_top=0, padding_bottom=0, padding_left=0, padding_right=0, anchor_point=None, anchored_position=None, scale=1, base_alignment=False, **kwargs)

参数说明如下：

  - **font**，字体参数。示例中使用Python内建的“terminalio.FONT”字体，即“print()”使用的控制台字体
  - **x**, **y**，分别为文本标签的x,y坐标。注意，x是文本显示的起始横坐标，y是文本中间的纵坐标(不是左上角，也不是左下角，而是两者的中间)
  - **text**，文本标签的文字内容，字符串类型。注意，文字内容的最大字符个数(字节数)不能超过“max_glyphs”指定的个数
  - **max_glyphs**，指定文本标签的文字内容允许的最大字符个数，即字符串“text”参数的最大长度。前面示例中设为24
  - **color**，指定文本标签的文字颜色，即前景的颜色，默认为白色。前面示例中每一个文本标签的颜色都是单独指定的
  - **background_color**，指定文本标签的背景颜色，默认为无色(与屏幕当前的背景色保持一致)。前面示例中使用默认值
  - **line_spacing**，文本标签的行间隔，默认为1.25倍。前面示例中使用默认值
  - **background_tight**，文本标签的背景框是否需要紧紧地围绕着文本，默认值为False。如果这个参数设置为True，后面的4个参数将被忽略。前面示例中使用默认值
  - **padding_top**，围绕着文本标签的背景框与文字内容的上边界之间需要额外的空白像素个数，默认值为0。前面示例中使用默认值
  - **padding_bottom**，围绕着文本标签的背景框与文字内容的下边界之间需要额外的空白像素个数，默认值为0。前面示例中使用默认值
  - **padding_left**，围绕着文本标签的背景框与文字内容的左边界之间需要额外的空白像素个数，默认值为0。前面示例中使用默认值
  - **padding_right**，围绕着文本标签的背景框与文字内容的右边界之间需要额外的空白像素个数，默认值为0。前面示例中使用默认值
  - **anchor_point**，指定文本标签的卯接点参数，卯接点参数是tuple型(x,y)分别指定横向和纵向的卯接位置，有效值范围：0.0~1.0。(0.0,0.0)是左上角，(1.0,1.0)是右下角。默认值为(0.0, 0.5)，前面示例中使用此默认值
  - **anchored_position**，指定问呗标签的卯接点在屏幕上的坐标，该参数是tuple型(x,y)分别指定横坐标和纵坐标。前面示例中未使用此参数
  - **scale**，指定文本标签的字体放大倍数，该参数必须是整数，默认值为1，即不放大。前面示例中仅标题“text0”文本标签使用该参数
  - **base_alignment**，指定文本标签的背景框是否与基线对齐，默认为False。前面示例中未使用该参数

此外，文本标签“label”类还具有另外几个重要的属性，包括：

  - **hidden**，指定文本标签隐藏或显示的属性，正常显示时该属性为False，如果设置该属性为True，文本标签将被隐藏(不显示出来)
  - **height**, **width**，只读属性，返回文本标签当前的高度和宽度(像素个数)
  - **bounding_box**，只读属性，返回文本标签当前的背景框的左上角顶点坐标、宽度和高度，返回值的4个参数是tueple型(x,y,width,height)

在前面的示例中，无穷循环程序块中仅改变某个文本标签的“text”参数即可刷新屏幕，这说明“displayio”库和“label”类能够自动刷新。那么，
我们改变文本标签的x,y坐标等其他参数时会发生什么变化呢？改变x,y坐标后，自动刷新屏幕后文本标签的位置将会发生改变，譬如下面示例代码：

.. code-block::  python
  :linenos:

  import time
  import random
  import displayio
  import terminalio
  from adafruit_display_text import label
  from hiibot_iots2 import IoTs2
  iots2 = IoTs2()
  text_group = displayio.Group(scale=2)
  textLabel = label.Label( 
                      terminalio.FONT,    # font of the text label
                      x=20, y=30,         # initial position
                      text="Hello IoTs2", # text content of the label
                      max_glyphs=24,      # the maximal length of the text content
                      color=(255,0,0)     # text color
                      )
  text_group.append(textLabel)
  iots2.screen.show(text_group)
  xb = textLabel.x
  yb = textLabel.y
  while True:
      xp=random.randint(0, 60)
      yp=random.randint(6, 60)
      steps = max( abs(xp-xb), abs(yp-yb) )
      xdelta = float(xp-xb)/steps
      ydelta = float(yp-yb)/steps
      for i in range(steps):
          textLabel.x = int(xb+(xdelta*i))
          textLabel.y = int(yb+(ydelta*i))
          time.sleep(0.2)
      xb = textLabel.x
      xb = textLabel.y

将上面的代码保存到IoTs2的/CIRCUITPY/code.py文件，IoTs2执行这个示例程序的效果与电脑“文字移动”的屏保效果很相似：
红色字符串“Hello IoTs2”将在IoTs2的LCD屏幕上随机地移动。虽然这个示例代码看起来比较多，初始化部分的代码与前面的示例是相同的，
只是这个示例仅使用一个文本标签“textLabel”；在无穷循环程序块中，我们首先产生2个随机整数作为本次循环后文本标签的新坐标位置，
然后计算每次移动一个像素时需要移动的步数，再用一个有限次循环逐步移动文本标签，移动的方法仅仅是改变文本标签的x和y坐标，
循环最后再用变量将当前坐标位置保存下来。


调整屏幕亮度和屏保
-----------------------

如果你想了解“label”类的接口都有那些，最快速的查找方法是使用IoTs2 Python解释器的REPL模式。
在MU编辑器上，点击“串口”按钮，再用鼠标在MU编辑器底部弹出的新窗口，按下“ctrl+c”键将终止code.py程序的执行，
立即进入Python解释器的通过导入模块或类，使用“help(className)”、“dir(className)”、
“className.”并按Tab键来了解className类的接口。

前面的示例中用到的“iots2”类的“screen”子类也包含多种属性和接口，现在我们以这个子类为例，用Python解释器的REPL来了解其属性和接口函数。
在MU编辑器的串口控制台窗口按下“ctrl+c”键后，IoTs2的Python解释器将立即终止code.py程序，并在控制台输出以下信息(第一个“>>>”之前)：

.. code-block::  python
  :linenos:

  Press any key to enter the REPL. Use CTRL-D to reload.

  Adafruit CircuitPython 6.2.0-beta.2-105-gb19e7c914-dirty on 2021-03-02; IoTs2 with ESP32S2
  >>> from hiibot_iots2 import IoTs2
  >>> iots2 = IoTs2()
  >>> help(iots2.screen)
  object <Display> is of type Display
    show -- <function>
    refresh -- <function>
    fill_row -- <function>
    auto_refresh -- <property>
    brightness -- <property>
    auto_brightness -- <property>
    width -- <property>
    height -- <property>
    rotation -- <property>
    bus -- <property>

在“>>>”提示符后输入一行Python脚本然后按回车键，Pythn解释器将立即执行这个语句并输出执行结果。
当我们输入“from hiibot_iots2 import IoTs2”并回车，再输入“iots2 = IoTs2()”再回车，此时REPL空间已经有一个名叫“iots2”的“IoTs2”类实体对象，
然后再输入“help(iots2.screen)”并回车，Python解释器将会把“iots2.screen”子类的接口函数(function)和属性(property)都列举出来，如上所示。
可以看出，“iots2.screen”子类有3个接口函数和7种属性。

“iots2.screen”子类接口函数和属性的说明如下：

  - **show()**，将一组(“group”)显示内容传递给该接口，此组的内容将会显示在屏幕上
  - **refresh()**，无参数函数，用于刷新显示器。注意，如果“auto_refresh”属性设为“True”，则无需使用此接口
  - **fill_row()**，将一个“buffer”型参数传递给该接口以填充屏幕的一行空间。“buffer”是字节数组(存储有图案信息)
  - **auto_refresh**，可读可写的属性，用于指定屏幕自动刷新操作，默认值是“True”，即自动刷新
  - **brightness**，可读可写的属性，用于指定屏幕的亮度，有效值范围：0.0~1.0，默认是1.0(最亮)
  - **auto_brightness**，可读可写的属性，用于配置自动根据环境光亮度调节屏幕亮度，默认是“False”
  - **width**，只读属性，返回屏幕的宽度(像素个数)。IoTs2横屏显示时，屏幕宽度像素数固定为240
  - **height**，只读属性，返回屏幕的高度(像素个数)。IoTs2横屏显示时，屏幕高度像素数固定为135
  - **rotation**，可读可写的属性，指定屏幕旋转角度，有效值的集为{0，90，180，270}。IotS2的默认值是90，即横屏显示
  - **bus**，只读属性，返回显示器使用的接口总线

了解这些属性和接口之后，我们再来看看下面的示例代码：

.. code-block::  python
  :linenos:

  import time
  import random
  import displayio
  import terminalio
  from adafruit_display_text import label
  from hiibot_bluebox5 import BlueBox5
  iots2 = BlueBox5()
  text_group = displayio.Group(scale=2)
  textLabel = label.Label( 
                      terminalio.FONT,    # font of the text label
                      x=20, y=30,         # initial position
                      text="Hello IoTs2", # text content of the label
                      max_glyphs=24,      # the maximal length of the text content
                      color=(255,0,0)     # text color
                      )
  text_group.append(textLabel)
  iots2.screen.show(text_group)
  xb = textLabel.x
  yb = textLabel.y
  cntDelay = 0
  while True:
      xp=random.randint(0, 60)
      yp=random.randint(6, 60)
      steps = max( abs(xp-xb), abs(yp-yb) )
      xdelta = float(xp-xb)/steps
      ydelta = float(yp-yb)/steps
      for i in range(steps):
          textLabel.x = int(xb+(xdelta*i))
          textLabel.y = int(yb+(ydelta*i))
          time.sleep(0.1)
          # quit Screen saver if button be pressed
          if iots2.button_state:
              cntDelay = 0
      xb = textLabel.x
      xb = textLabel.y
      # Screen saver 
      cntDelay += 1
      if cntDelay>12:
          iots2.screen.brightness = 0.0
      elif cntDelay>8:
          iots2.screen.brightness = 0.2
      elif cntDelay>6:
          iots2.screen.brightness = 0.5
      else :
          iots2.screen.brightness = 1.0

这个示例代码是在前一个示例的基础上稍作修改得到的，增加的代码主要包括注释语句“# Screen saver”下面的部分，
以及无穷循环程序块中的有限次循环代码。将本示例代码保存到IoTs2的/CIRCUITPY/code.py文件中，IoTs2执行该示例程序时，
你将会看到更接近电脑“移动文字”屏保的效果：屏幕亮度逐渐变暗直到屏幕被关闭，按下IoTs2的可编程按钮后屏幕再次开启显示。

LCD显示屏的是一种被动显示器，屏幕本身不会发光，必须借助于外接光源才能看到屏幕上的字。因此，
绝大多数LCD屏幕都会带着一个背光板，一种面积跟LCD屏幕完全相同的平面光源，光源被置于LCD屏幕后面。
LCD屏背光板是功耗较大的电子元件，而且寿命也比较短，尤其是随着使用时间的增加，背光板的亮度将逐渐降低。
为了节能，大部分时间我们不需要看LCD显示屏的内容时，我们应该关闭LCD屏幕后面的背光板。

本示例程序中，我们仅仅是通过调节“iots2.screen.brightness”属性值来实现屏保效果。

------------------------------------

.. admonition:: 
  总结：

    - LCD显示器
    - LCD显示器背光板的亮度和屏保
    - 多行文本显示的数据结构
    - 文本字体的缩放
    - 函数及其定义和调用
    - 全局变量和局部变量
    - 本节中，你总计完成了45行代码的编写工作

