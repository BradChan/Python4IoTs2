=========================
IoTs2支持的其他编程语言
=========================

除了Python编程语言之外，IoTs2还支持C/C++等编译型编程语言和Scratch等图形化编程语言。

Scratch图形化编程语言本身是另一种脚本语言——Javascript(看名字像是Java语言，事实上与Java语言无任何关系)，
但是IoTs2并不能直接执行Javascript程序，我们将Scratch图形化程序自动转换为Python脚本程序，
这样的“语言转换器”是一种代码自动生成器。因此，本质上使用Scratch图形化编程语言编写的程序是一种图形化形式的Python脚本程序。
与直接编辑Python脚本代码的形式相比，使用Scratch图形化编程语言编写程序时不会出现拼写关键词、变量名等困难，
所以Scratch图形化编程语言非常适合青少年或初学编程者使用。

如果需要使用Scratch图形化编程语言来编写IoTs2的应用程序，请使用Chrome等浏览器打开 https://www.ezaoyun.com/ 网址，
并进入“在线创作”页面，点击“cppBlockly(Scratch)”按钮，即可进入在线版Scratch图形化编程环境，在该窗口的右下角“硬件”标签页选择IoTs2即可。

C/C++等编译型编程语言程序代码必须经过专用的编译器、链接器等软件工具转换成机器码，这意味着我们在使用C/C++对IoTs2编程之前必须先在电脑上安装这些工具软件。
譬如Arduino IDE和ESP IDF等应用程序都支持IoTs2的C/C++开发。安装C/C++编程语言的开发环境并不是一件难事儿，
我们可以根据乐鑫官网(https://www.espressif.com/)的相关文档安装C/C++编程语言的开发环境所需要的工具软件或应用程序。
乐鑫官方的Arduino软件包网址：https://github.com/espressif/arduino-esp32，请参照此链接的说明搭建Arduino IDE的开发环境。

