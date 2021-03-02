====================
使用REPL
====================

认识和使用REPL之前，我们需要首先了解一点脚本语言的特性。Python是最流行的脚本语言之一，我们每天都在使用JavaScript脚本语言(简称JS)浏览网页和某些App，
除了Python和JS之外，PHP、Ruby、Lua、Perl等都是脚本语言。

与脚本语言相对的编译型语言，如C/C++和Java语言。使用编译型语言编写的程序，必须“编译-链接”才能被目标计算机执行。然而，
使用脚本语言编程可以实现REPL的效果。在正式解释REPL之前，你可以这么想象REPL：输入一行代码，立即执行并给出结果。输入一行代码，
执行这一行代码，如此重复。

用脚本语言编写的程序，几乎就是如上所述的“逐行执行，并立即输出执行结果”，而且无需“编译-链接”。

-----------------------------

1. REPL是什么？
-----------------------------

如果你现在使用英汉词典(近期出版的)、搜索引擎、wiki百科等工具查询“REPL"，必然会得到答复。REPL的正式解释是

  - Read-Eval-Print Loop (“读取-求值-输出”的循环)

进一步解释，REPL就是

  - “读取”你输入的一行脚本程序，“求值”是执行该程序语句，并“输出”执行结果，如此循环。

所谓的脚本程序，如Python或JS等脚本程序都是逐行地“REPL”，计算机自动连续执行这些脚本程序即可实现编程者的意图/任务。REPL几乎是所有脚本
编程语言都支持的一种程序执行模式，编程者输入一行脚本程序，计算机立即执行这个程序语句，并输出执行结果。显然，REPL是调试脚本程序的模式。
如果你调试过C/C++等编译型语言的程序，你肯定喜欢断点(break point)、单步(single step)等功能，这些功能本质上是帮助我们单步执行程序
并给出每一步的节行结果，我们从每一步的结果中很快就能发现bug。

如果你认为自己编写Python程序的过程中无需调试，的确不需要REPL。否则，REPL就是每一位Python编程者的调试工具。


2. 在MU编辑器中使用REPL
-----------------------------

REPL是一种很重要的脚本程序调试工具，每一种脚本语言的REPL都有自己的协议和规则。MU编辑器支持Python脚本语言的REPL，这就是我们推荐使用
MU编辑器编写IoTs2的Python脚本程序的理由。

当MU编辑器在宿主计算机上运行时，使用USB数据线将IoTs2与宿主计算机连接，MU编辑器会自动侦测和切换为IoTs2编程模式，点击MU编辑器的“串口”
按钮，MU编辑器下方将出现一个特殊的窗口，习惯上把这个窗口称作“串口控制台(console)”。在MU编辑器的控制台中，输入“ctrl+C”，IoTs2将立即
停止执行code.py或main.py程序，并进入REPL模式，按下回车键，MU编辑器的控制台将出现“>>”提示符。这就是MU编辑器区别于Pycharm、Visual 
Studio和Sublime Text等文本编辑器的关键，MU编辑器天生支持REPL。

MU编辑器的REPL使用控制台实现人-机交互(你输入一个脚本程序语句供REPL读取，然后执行，并输出执行结果。然后你再输入下一个脚本程序语句，
重复这一过程(loop))。

.. image:: /../_static/images/iots2_setup/repl1.jpg
  :scale: 10%
  :align: center

如上图所示，在控制台的">>"提示符后面输入“import random”，即导入Python内建的"random"模块(随机数发生器模块)；
然后输入“r=random.randint(0, 100)”脚本语句并按回车键表示输入完毕，REPL将立即执行该语句，即生成一个0~100之间的一个随机的整数，
并把这个数据赋于一个名叫“r”的变量；最后输入“r”并按回车键，REPL立即将这个随机数输出到控制台。

当你需要调试Python程序时，REPL就是“单步执行”Python程序的模式；REPL就是调试Python程序最佳工具。


3. REPL的妙用1——help("modules")
-------------------------------------

如果你想了解IoTs2支持多少种内建的(built-in)模块，在“>>”提示符后面输入“help("modules")”，你将会看到以下的执行结果输出：

.. image:: /../_static/images/iots2_setup/help_modules.jpg
  :scale: 4%
  :align: center

你是否发现前面用过的“random”在其中吗？


4. REPL的妙用2——help(random)
-------------------------------------

如果你想了解一个模块所支持的全部API接口，尝试使用“help(modulename)”。以Python内建的"random"为例，在REPL模式首先输入
"import random"并按回车键，即导入random模块；然后输入“help(random)”，
IoTs2将会想控制台输出内建的"random模块"所支持的所有接口都列举出来，如下图所示：

.. image:: /../_static/images/iots2_setup/help_random.jpg
  :scale: 4%
  :align: center


5. REPL的妙用3——dir(random)
-------------------------------------

在导入"random"模块之后，使用“help(random)”语句将会给我们列举random模块所支持的全部类(class)、变量和方法(function)。
仍以random模块为例，使用"dir(random)"将以列表(list)格式显示出random模块所支持的类、变量和方法名称。如下图所示:

.. image:: /../_static/images/iots2_setup/dir_random.jpg
  :scale: 4%
  :align: center


6. REPL的妙用4——random. (+tab键)
-------------------------------------

如果你曾经使用过一些支持面向对象编程的编辑软件，在编辑程序时，“输入一个对象名称和点，然后按Tab键，编辑软件会立即把这个对象的所有接口方法都
列举出来”这种辅助式交互可以让程序员不必记住一个对象的全部接口，用到时输入“ClassName.”并按Tab键，编辑软件会帮你列出所有方法，选择即可。
Python的REPL也具备这一辅助功能。以random模块为例，导入random模块后，再“>>”提示符后面输入“random.”并按Tab键，REPL会把random模块
支持的所有类、变量和方法全部列出来。

使用IoTs2学习Python编程，你不必记住每一个模块的全部接口，当你需要了解一个模块有哪些具体接口(包括类、变量、方法等)时，在串口控制台
按"Ctrl+C"终止当前正在执行的程序，进入REPL模式，输入"import modulename"并按回车，然后输入“modulename.”并按Tab键，你将看到
这个模块所支持的接口。以random模块为例，如下图：

.. image:: /../_static/images/iots2_setup/tab_random.jpg
  :scale: 4%
  :align: center


.. Tip::

  - 进入REPL的方法：
     在串口控制台(鼠标停留在控制台窗口，点击鼠标左键)，同时按下“Ctrl+C”键，即可进入REPL模式，出现REPL“>>”提示符


  - 退出REPLD的方法：
     在串口控制台(鼠标停留在控制台窗口，点击鼠标左键)，同时按下“Ctrl+D”键，即可退出REPL模式，IoTs2立即重新开始执行code.py或main.py程序



