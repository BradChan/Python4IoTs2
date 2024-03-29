将IoTs2连接到MU编辑器
========================

绝大多数情况，将IoTs2连接到宿主计算机系统都是为了更新/下载程序。与其他嵌入式系统或单板机不同的时，当我们使用USB数据线
将IoTs2插入自己的电脑时，IoTs2被映射成一个“移动磁盘”。根据IoTs2的工作状态，这个可移动磁盘使用两个固定的名称：IOTS2BOOT和
CIRCUITPY。


.. Attention:

  - IoTs2使用常用的USB Type-C数据线与电脑连接
  - 很多设备使用USB Type-C接口供电。因此市面上很多USB电源线，他们并不是数据线！此类电源线无法让IoTs2与电脑连接
  - 验证IoTs2是否与电脑可靠连接的方法就是，检查电脑的资源管理器是否出现IOTS2BOOT或CIRCUITPY磁盘

-------------------------------------

我们会在以下几种情况使用IoTs2磁盘：
  
  - 更新IoTs2固件(Python脚本解释器)

    - 按着Boot按钮(IO21)同时按下复位按钮并释放复位按下，当IoTs2的RGB彩灯变为绿色时，释放Boot按钮，出现IOTS2BOOT磁盘
    - 下载最新的IoTs2固件
    - 拖放IoTs2固件(Python脚本解释器)到IOTS2BOOT磁盘

  - 更新IoTs2v2固件(Python脚本解释器)

    - 按下复位按钮约1～2秒并释放复位按钮，当IoTs2v2彩灯亮紫色的0.5秒内按下Boot按钮(IO0)，等待IoTs2v2的RGB彩灯变为绿色时，与之连接的电脑上出现IOTS2BOOT磁盘
    - 下载最新的IoTs2v2固件
    - 拖放IoTs2v2固件(Python脚本解释器)到IOTS2BOOT磁盘

  - 更新用户程序

    - 将IoTs2/IoTs2v2插入电脑USB端口，出现CIRCUITPY磁盘
    - 将用户程序文件(必须使用main.py或code.py)拖放至CIRCUITPY磁盘

-------------------------------------

使用USB数据线将IoTs2与电脑连接好，按着Boot按钮(IO21)同时按下复位按钮并释放复位按下，当IoTs2的RGB彩灯变为绿色时，
释放Boot按钮，出现IOTS2BOOT磁盘。在这个状态下，你可以拖放新版固件文件(必须是UF2格式)到IOTS2BOOT磁盘，即可升级固件.

使用USB数据线将IoTs2v2与电脑连接好，按下复位按钮约1~2秒并释放复位按钮，当IoTs2v2彩灯亮紫色时按下Boot按钮(Io0)，当IoTs2的RGB彩灯变为绿色时，
出现IOTS2BOOT磁盘。在这个状态下，你可以拖放新版固件文件(必须是UF2格式)到IOTS2BOOT磁盘，即可升级固件.

当IoTs2被复位或正常通电后，使用USB数据线将IoTs2与电脑连接好，如果不按Boot按钮(IO21)，
IoTs2自动执行用户的Python程序，并在电脑上出现一个名为CIRCUITPY的磁盘。
在这个状态下，LCD显示器会显示程序的执行结果，除非用户程序有意将LCD屏幕关闭或使用显示器显示其他内容。

当IoTs2v2被复位或正常通电后，使用USB数据线将IoTs2v2与电脑连接好，当IoTs2v2彩灯亮紫色期间(约0.5秒)，如果不按Boot按钮(IO0)，
IoTs2v2自动执行用户的Python程序，并在电脑上出现一个名为CIRCUITPY的磁盘。
在这个状态下，LCD显示器会显示程序的执行结果，除非用户程序有意将LCD屏幕关闭或使用显示器显示其他内容。

.. image:: /../_static/images/iots2_setup/circuitpy_status.jpg
  :scale: 10%
  :align: center

在出现CIRCUITPY磁盘时，IoTs2上的全部资源都受用户程序控制，LCD的显示内容、彩灯状态等都与用户程序有关。

-------------------------------------

如果系统未按预期出现相应的磁盘，请首先检查USB数据线和连接的可靠性。如果IoTs2的电源指示灯(IoTs2正面的左上角的绿色LED)都
不能正常工作，请更换到其他USB端口，电脑的某些USB端口或许已经不可靠的或损坏！

-------------------------------------

1. 当IoTs2与MU编辑器成功连接时
----------------------------------

如果你的电脑上已经安装了MU编辑器程序(具体安装步骤见前一小节)，请首先打开MU编辑器，当IoTs2通过USB数据线与宿主计算机成功
连接时，MU编辑器会自动侦测IoTs2，并提示“检测到新的CircuitPython设备”，并提醒你是否切换到“CircuitPython模式”。

.. image:: /../_static/images/iots2_setup/mu_mode.jpg
  :scale: 10%
  :align: center

MU编辑器(V1.1及以后)支持6种不同的模式，其中4种类别的硬件编程，MU编辑器会根据侦测到的硬件类型自动切换到对应模式。

IoTs2使用CircuitPython编程语言，这是一种与Python3几乎完全相同的、支持单板机的脚本编程语言。CircuitPython由美国知名开源
开源硬件供应商——Adafruit发起，并得到全球很多人的维护和支持，同时支持很多种不同的嵌入式硬件系统，方便我们使用流行的Python语言
开发和设计各种嵌入式计算机系统或单板机。


2. CIRCUITPY磁盘
----------------------------------

当IoTs2与电脑连接后，自动执行用户程序。用户程序的文件名必须使用“code.py”或"main.py"，而且只能选择使用其中一个。用户程序
code.py文件保存在一个名叫"CIRCUITPY"的磁盘上。如果你熟悉Python编程语言，使用任意的文本编辑器修改"/CIRCUITPY/code.py"
程序文件，然后保存该文件，你会发现IoTs2自动执行你修改好的程序。

.. image:: /../_static/images/iots2_setup/edit_save_codepy.jpg
  :scale: 20%
  :align: center

IoTs2自动检测用户程序文件是否被修改，如果发现被修改，自动执行软复位(soft reset)，并开始执行修改后的程序。任何时候，你只要
打开/保存"CIRCUITPY"磁盘上的文件，IoTs2都将自动执行软复位，重新执行用户程序(CIRCUITPY磁盘上名称为code.py或main.py)。

建议你使用MU编辑器编写自己的Python程序，程序代码编辑完成后，点击“保存”按钮，请选择保存到"CIRCUITPY"磁盘的根目录中，而且程序
名称必须使用code.py或main.py(只能选择其中一种)。每次修改程序并保存后，IoTs2都会自动执行软复位，重新执行新保存的程序。使用
MU编辑器将给你带来极大的方便。

有C语言编程经历的人都知道，C程序需要专门的软件工具把我们的C程序代码转成目标计算机系统的指令，这个过程叫做编译和连接，软件工具
叫做工具链。然而，Python脚本程序可以被许多计算机系统直接执行，无需编译，这种便捷性或许正式Python语言在全球流行的关键原因之一。
IoTs2不仅支持Python脚本语言，而且采用USB MSC(大容量存储设备类)模式，与电脑连接后是一个可移动磁盘，而且磁盘卷标/名称固定为
CIECUITPY，你的Python程序文件只需要拖放到CIRCUITPY磁盘即可，无需任何专用的软件下载工具。


3. 问题及其解决
----------------------------------

你在使用过程中，或许会遇到以下问题，这里列举每一种问题的解决方法：

  1) IoTs2与电脑连接后，未出现名为“CIRCUITPY”的磁盘，出现“NONAME”或其他名称的磁盘

    - 电脑的磁盘名称或卷标是可以修改的，你可以将"NONAME"卷标名称修改为"CIRCUITPY"即可。

  2) IoTs2与电脑连接后，未出现名为“CIRCUITPY”的磁盘，出现名为"IOTS2BOOT"的磁盘

    - 如果按下Boot按钮同时按下IoTs2的复位按钮然后释放复位按钮，IoTs2将自动进入Bootloader模式。拔掉USB数据线，重新插入电脑即可。

  3) IoTs2v2与电脑连接后，未出现名为“CIRCUITPY”的磁盘，出现名为"IOTS2BOOT"的磁盘

    - 如果IoTs2v2被复位后板上彩灯亮紫色期间(约0.5秒)按下Boot按钮(IO0)，IoTs2v2将自动进入二级Bootloader模式。拔掉USB数据线，重新插入电脑即可。

  4) IoTs2v2与电脑连接后，未出现名为“CIRCUITPY”或“IOTS2BOOT”的磁盘，但设备管理器中有新增的虚拟串口COMx/cu.xx/ttyACM0等

    - 如果IoTs2v2被复位时并按着Boot按钮(IO0)，IoTs2v2将自动进入ROM-Bootloader模式。拔掉USB数据线，重新插入电脑即可。

  5) IoTs2与电脑连接后，未出现任何(增加的可移动)磁盘

    - 首先确保IoTs2正常启动，左上角绿色电源指示灯亮，而且LCD屏幕有字符或其他信息。如果IoTs2没有正常供电和正常启动，不会出现CIRCUITPY磁盘，线检查供电是否正常。
    - 首先检查使用的USB是否是数据线，市面上很多USB供电线，并不是USB数据线。更换为USB数据线即可。
    - 更换电脑的USB端口，确保USB端口未损坏，且接触良好。
  
  6) IoTs2需要专用驱动程序吗？

    - Windonws7及之后的系统都无需驱动
    - macOS和Linux系统无需驱动

  

