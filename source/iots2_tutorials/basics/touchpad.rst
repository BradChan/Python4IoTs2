触摸输入(无声的按钮)
======================

触摸输入是一种特殊的输入接口，功能几乎与按钮一样，但是没有按钮操作的机械声音，所以触摸输入被称作无声的按钮。

IoTs2的2x14P扩展接口上具有8个人体触摸输入引脚，这些引脚是一种特殊的输入接口。这些触摸引脚不仅能感知你触摸他们，
还允许你使用鳄鱼夹电线将触摸引脚与某些导体或相当于导体的材料相连接，如锡箔纸、导电不干胶、水果、蔬菜、盛有水的杯子等，
用手触摸这些导体或材料时，等同于触摸到IoTs2的触摸引脚。

本节我们来了解这些触摸输入的用法。先看第一个示例：

.. code-block::  python
  :linenos:

  import time
  import board
  from touchio import TouchIn
  # list of the Touched Pins
  touchPins = [TouchIn(board.IO3),  TouchIn(board.IO4), 
               TouchIn(board.IO7),  TouchIn(board.IO7),
               TouchIn(board.IO9),  TouchIn(board.IO10),
               TouchIn(board.IO11), TouchIn(board.IO12)]
  # set their threshold (default threshold be equal to 300 + "initial raw_value")
  for i in range(8):
      threshold = touchPins[i].raw_value
      touchPins[i].threshold = threshold+300
  while True:
      for i in range(8):  # scan all touchPins
          if touchPins[i].value:
              print("touchPin-{} be touched".format(i))
              time.sleep(0.2)

将本示例的程序复制-粘贴到MU编辑器，并保存到IoTs2的/CIRCUITPY/code.py文件，IoTs2将立即执行该程序，你可以用手指去触摸IoTs2的IO3、
IO4、IO7、IO8、IO9、IO10、IO11或IO12引脚，观察LCD屏幕(控制台)上的显示信息。如果手指触摸时会影响到相邻触摸引脚，
我们可以手握水笔或铅笔并用笔尖触碰这些引脚时，将会观察到同样的效果，而且不影响相邻引脚的状态。控制台输出的信息如下：

.. code-block::  python
  :linenos:

  Auto-reload is on. Simply save files over USB to run them or enter REPL to disable.

  code.py output:
  touchPin-0 be touched
  touchPin-1 be touched
  touchPin-7 be touched
  touchPin-6 be touched
  touchPin-5 be touched
  touchPin-4 be touched
  touchPin-3 be touched
  touchPin-4 be touched

根据你所看到的程序运行和试验结果，思考本示例的程序语句与测试结果之间的关联关系。

  示例代码分析：

    - 第1行，导入一个Python内建的模块“time”
    - 第2行，导入一个Python内建的模块“board”
    - 第3行，从“touchio”模块中导入TouchIn类
    - 第4行，注释语句
    - 第5～8行，声明一个名叫touchPins的列表，列表中的各项分别是“TouchIn(board.Px)“，即IoTs2的可用触摸输入引脚的实例化对象
    - 第9行，注释语句
    - 第10～12行，使用一个8次的循环体分别读取触摸引脚当前状态的原始值，并加上300后作为该触摸引脚的阈值
    - 第13行，一个无穷循环的程序块
    - 第14行(无穷循环程序块的第1行)，定义一个8次的循环程序块
    - 第15行(无穷循环程序块的第2行，8次循环程序块的第1行)，检测第i个触摸引脚是否被触摸
    - 第16行(无穷循环程序块的第3行，条件判断为True时的程序块第1行)，检测第i个触摸引脚被触摸，则向LCD屏幕(控制台)输出“touchPin-i be touched”
    - 第17行(无穷循环程序块的第4行，条件判断为True时的程序块第2行)，延迟0.2秒

请注意，执行本示例程序时，当IoTs2初始上电或复位期间不要触摸任何引脚或与触摸引脚相连的电极，第10～12行语句是系统初始化操作的一部分，
即使用当前每个触摸引脚的原始值“+300”后当作对应触摸引脚的阈值。这种操作是电容型触摸输入的常规思路。


--------------------------------

.. admonition:: 
  总结：

    - 人体触摸输入
    - 实体对象的属性的状态
    - 逻辑判断和逻辑程序块
    - 本节中，你总计完成了17行代码的编写工作

.. Important::
  **IoTs2的TouchIn类的接口**

    - TouchIn(board.px) (将board.px引脚实例化为人体触摸输入引脚)
    - value (属性, 只读, 有效值：0/False 或 1/True), 人体触摸引脚的状态(是否被触摸)
    - raw_value (属性, 只读, 有效值：0~65535), 人体触摸输入引脚的原始值(若大于阈值则视为被触摸，否则未被触摸)
    - threshold (属性, 可读可写的, 有效值：0～65535), 触摸引脚的阈值(非常重要，初始化触摸引脚时被设置为合适的值)

