用按钮给计算机发指令
======================

按钮(Button)是计算机系统最简单的一种输入设备，计算机键盘上有100个左右的按键(不同键盘的按键个数不同)，每一个按键就是一个按钮，
每一个按钮赋予惟一的编号，如A按键的编号为0x41，B按键的编号为0x42，当我们按下按键的按钮时，键盘将对应按键的惟一编号发送给电脑主机，
实现人-机交互的输入。

绝大多数嵌入式系统的按键输入比较少，如电梯召唤按钮、轿箱内楼层按钮等都仅有几个或几十个按钮，这些按钮用于人向计算机系统发出指令，
按下电梯某楼层的召唤按钮告知电梯控制的计算机系统我需要乘坐电梯，电梯系统收到召唤后即让召唤按钮背后指示灯亮起，表示收到召唤，启动响应。

IoTs2具有两个按钮，分别是可编程按钮和复位按钮，分别位于USB座的左右两侧，我们可以使用这两个按钮向IoTs2发指令，譬如开启蓝色LED、
关闭蓝色LED、复位系统等。当然，复位按钮的优先级最高，任何时候按下复位按钮都可以终止CPU执行程序并重新启动。本节重点了解可编程按钮。

--------------------------

可编程按钮的输入状态
--------------------------

按钮仅有两个状态：被按下和未被按下。如果被按下时的状态记为“1”，未被按下的状态记为“0”。也可以使用逻辑变量值来表示，
按下时的状态记为“True”，未被按下时的状态记为“False”。

我们使用以下程序，将IoTs2上按钮的状态显示在屏幕(和控制台)上：

.. code-block::  python
  :linenos:

  import time
  from hiibot_iots2 import IoTs2
  iots2 = IoTs2()
  while True:
      print("button:{:d} ".format(iots2.button_state))
      time.sleep(0.5)

打开MU编辑器，点击“新建”按钮，并将本示例代码复制-粘贴的MU编辑器中，然后点击“保存”按钮，并在弹出的窗口中输入文件名为“code.py”，
保存文件的磁盘为“CIRCUITPY”，路径为该磁盘的根目录。一旦将code.py文件保存到IoTs2的CIRCUITPY磁盘上，IoTs2立即开始执行这个脚本程序。
你将会看到LCD屏幕(和控制台)上看到下面的显示效果：

.. code-block::  python
  :linenos:

  button:0 
  button:0 
  button:1  
  button:1 
  button:0 

当我们按下IoTs2的可编程按钮时，屏幕上显示“button:1”信息；当IoTs2的可编程按钮被释放时，屏幕上显示“button:0”信息。

  示例代码分析：

    - 第1行，导入一个Python内建的模块“time”
    - 第2行，从“/CIRCUITPY/lib/hiibot_iots2.py”模块中导入IoTs2类
    - 第3行，将导入的“IoTs2”类实例化为一个实体对象，名叫“iots2”
    - 第4行，一个无穷循环的程序块
    - 第5行(无穷循环程序块的第1行)，将IoTs2可编程的按钮的状态值格式化显示到LCD屏幕(控制台)上
    - 第6行(无穷循环程序块的第2行)，执行time的sleep方法，参数为0.5秒

第5行程序是重点，将变量值val格式化为一个字符串："{:d}".format(val)。其中，“{}”内的“:d”表示将val值显示十进制形式。
print("hello")是将字符串“hello”显示在LCD屏幕(控制台)上。如果将本示例程序稍作修改，你将会看到另外一种显示效果：

.. code-block::  python
  :linenos:

  import time
  from hiibot_iots2 import IoTs2
  iots2 = IoTs2()
  while True:
      print("button:{}".format(iots2.button_state))
      time.sleep(0.5)

修改后的程序只是去掉“{}”内的“:d”，即使用默认的格式化(系统根据变量val的类型自动决定格式化的输出形式)。
执行这个示例程序时屏幕上将显示“button:True”(当按钮被按下时)、“button:False”(当按钮未被按下时)。即，

.. code-block::  python
  :linenos:

  button:False 
  button:True  
  button:True
  button:False


用按钮开关蓝色LED
--------------------------

下面这个示例，我们使用IoTs2的可编程按钮来切换蓝色LED的亮和灭：

.. code-block::  python
  :linenos:

  import time
  from hiibot_iots2 import IoTs2
  iots2 = IoTs2()
  while True:
      iots2.button_update()
      if iots2.button_wasPressed:
          iots2.blueLED_toggle()

打开MU编辑器，点击“新建”按钮，并将本示例代码复制-粘贴的MU编辑器中，然后点击“保存”按钮，并在弹出的窗口中输入文件名为“code.py”，
保存文件的磁盘为“CIRCUITPY”，路径为该磁盘的根目录。一旦将code.py文件保存到IoTs2的CIRCUITPY磁盘上，IoTs2立即开始执行这个脚本程序。
运行本示例程序时，你会发现程序的效果：每按下可编程按钮一次，蓝色LED状态就被切换一次。这个效果像是一个被轻触开关控制的照明灯。

  示例代码分析：

    - 第1行，导入一个Python内建的模块“time”
    - 第2行，从“/CIRCUITPY/lib/hiibot_iots2.py”模块中导入IoTs2类
    - 第3行，将导入的“IoTs2”类实例化为一个实体对象，名叫“iots2”
    - 第4行，一个无穷循环的程序块
    - 第5行(无穷循环程序块的第1行)，更新IoTs2上的按钮状态
    - 第6行(无穷循环程序块的第2行，判断条件为True时的程序块)，判断IoTs2的可编程按钮是否已被按下
    - 第7行(无穷循环程序块的第3行，条件为True时的程序块的第1行)，如果按钮已被按下，切换IoTs2蓝色LED的状态

第6行和第6行是一个简单的逻辑判断和逻辑程序块，当“iots2.button_wasPressed”为True时，执行“iots2.blueLED_toggle()”。


用按钮调节蓝色LED的亮度
--------------------------

我们将上面的程序稍作修改，即可实现“使用可编程按钮调节蓝色LED的亮度”，程序代码如下：

.. code-block::  python
  :linenos:

    import time
    from hiibot_iots2 import IoTs2
    iots2 = IoTs2()
    b=0.2
    dir=1
    while True:
        iots2.blueLED_bright=b
        iots2.button_update()
        if iots2.button_wasPressed:
            b += 0.2 if dir==1 else -0.2
            if b>1.0:
                b=1.0
                dir=0
            if b<0.0:
                b=0.0
                dir=1

将上面的示例程序保存到IoTs2的CIRCUITPY磁盘的code.y文件，当IoTs2执行该程序时，试一试按下IoTs2的可编程按钮，
你将观察到蓝色LED的亮度变化。

  示例代码分析：

    - 第1行，导入一个Python内建的模块“time”
    - 第2行，从“/CIRCUITPY/lib/hiibot_iots2.py”模块中导入IoTs2类
    - 第3行，将导入的“IoTs2”类实例化为一个实体对象，名叫“iots2”
    - 第4行，声明一个变量b，并赋初始值为0.5
    - 第5行，声明一个变量dir，并赋初始值为1
    - 第6行，一个无穷循环的程序块
    - 第7行(无穷循环程序块的第1行)，用变量b的值更新实体对象iots2的blueLED_bright属性(即蓝色LED的亮度属性)
    - 第8行(无穷循环程序块的第2行)，更新IoTs2的可编程按钮的状态
    - 第9行(无穷循环程序块的第3行，判断条件为True时的程序块)，判断IoTs2的可编程按钮是否已被按下
    - 第10行(无穷循环程序块的第4行，条件为True时的程序块的第1行)，如果按钮已被按下，变量b的值增加0.2(如果变量dir等于1)或-0.2(如果变量dir等于0)
    - 第11行(无穷循环程序块的第5行，判断条件为True时的程序块)，判断变量b的值是否大于1.0
    - 第12行(无穷循环程序块的第6行，条件为True时的程序块的第1行)，如果变量b大于1.0，变量b设为1.0
    - 第13行(无穷循环程序块的第7行，条件为True时的程序块的第2行)，如果变量b大于1.0，变量dir设为0
    - 第14行(无穷循环程序块的第8行，判断条件为True时的程序块)，判断变量b的值是否小于0.0
    - 第15行(无穷循环程序块的第9行，条件为True时的程序块的第1行)，如果变量b的值小于0.0，变量b设为0.0
    - 第16行(无穷循环程序块的第10行，条件为True时的程序块的第2行)，如果变量b的值小于0.0，变量dir设为1

你能确定变量b的有效数据集吗？根据每个循环中变量b的取值列出来即可。上面示例程序的关键每次侦测到按钮被按下后都会调整一次IoTs2蓝色LED的亮度。
如果我们使用Python的列表(list)将蓝色LED亮度值列举出来，也能实现同样的执行效果，但是程序代码更短。代码如下：

.. code-block::  python
  :linenos:

  import time
  from hiibot_iots2 import IoTs2
  iots2 = IoTs2()
  cnt=1
  bl = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 0.8, 0.6, 0.4, 0.2]
  while True:
      iots2.blueLED_bright=bl[cnt%10]
      iots2.button_update()
      if iots2.button_wasPressed:
          cnt += 1

将上面的示例程序保存到IoTs2的CIRCUITPY磁盘的code.y文件，当IoTs2执行该程序时，试一试按下IoTs2的可编程按钮，
你将观察到蓝色LED的亮度变化与前一个示例代码的执行效果有何区别。


按钮的短按和长按
--------------------------

当你一直按着桌面计算机的某个按键时，相当于快速输入很多个相同的字母或数字，IoTs2的按钮也有相同的效果吗？

为了验证这一设想，我们可以修改前一个示例程序，如果发现长按IoTs2的可编程按钮时则直接让变量b的值变为1.0(最大亮度)或0.0(最小亮度/灭)根据当前亮度的增加方向，
如果短按该按钮时仍以0.2的步长增减变量b的值。修改后的程序如下：

.. code-block::  python
  :linenos:

  import time
  from hiibot_iots2 import IoTs2
  iots2 = IoTs2()
  b = 1.0
  dir = 0
  while True:
      iots2.blueLED_bright = b
      iots2.button_update()
      if iots2.button_wasPressed:       # 是否已被短按
          b += 0.2 if dir==1 else -0.2
          if b>1.0:
              b=1.0
              dir=0
          if b<0.0:
              b=0.0
              dir=1
      if iots2.button_pressedFor(2.0):  # 是否已被长按并超过2.0s
          b = 1.0 if dir==1 else 0.0
          dir = 0 if dir==1 else 1

修改后的程序仅仅增加最后的3行，即第17～19行。第17行是条件判断，条件是IoTs2的可编程按钮是否已按下超过2s？如果条件成立则执行第18行和第19行，
第18行将变量b设为1.0(如果dir等于1)或0.0(如果dir不等于1)，第19行将变量dir设为0(如果dir等于1)或1(如果dir不等于1)。
其他程序语句与前一示例程序完全相同，此处不再赘述。

请在IoTs2上测试本示例，检验程序的执行效果是否达到设想：短按IoTs2的可编程按钮时蓝色LED的亮度将分别减小或增加，长按按钮时蓝色LED亮度直接变为0.0或1.0。
然后试一试修改第17的长按时间参数，观察执行效果，并思考为什么是这样的效果。

---------------------------------

.. admonition:: 
  总结：

    - 按钮输入
    - 实体对象的属性的状态
    - 变量
    - 变量赋值
    - 变量自增/自减
    - 逻辑判断和逻辑程序块
    - 本节中，你总计完成了19行代码的编写工作


.. Important::
  **IoTs2类的button属性和接口**

    - button_state (属性, 只读, 有效值：0/False 或 1/True), IoTs2的可编程按钮的状态
    - button_wasPressed (属性, 只读, 有效值：0/False 或 1/True), IoTs2的可编程按钮是否已被按下
    - button_wasReleased (属性, 只读, 有效值：0/False 或 1/True), IoTs2的可编程按钮是否已被释放
    - button_pressedFor (函数, 输入参数: 时长, 返回值:0/False 或 1/True), IoTs2的可编程按钮是否被长按超过指定的时长
    - button_update (函数, 无参数, 无返回值), 更新IoTs2的按钮状态, 必须放在循环体内调用