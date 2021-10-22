安装MU编辑器
====================

几乎所有的嵌入式系统或单板机都没有桌面计算机的键盘、鼠标和大屏幕显示器等标准外设，对这些系统编程或开发时都必须借助于桌面计算机。
通常，我们把用于开发嵌入式系统或单板机的桌面计算机称作“宿主计算机”，待开发和编程的嵌入式系统或单板机称作“目标计算机”，两者通
过USB等标准的通讯接口连接。并且，宿主计算机系统必须预先安装必要的编程软件、编译软件和程序下载工具软件。同时，目标计算机系统
也应该具备一个小型的软件系统能够与宿主计算机系统连接，下载用户程序。

.. image:: /../_static/images/iots2_setup/cross_dev.jpg
  :scale: 100%
  :align: center

(备注： 上图中以ARM Cortex-M系列处理器的单板机开发为例)

IoTs2已经尽可能地简化宿主计算机上所需要的软件环境，仅使用任何桌面计算机系统都具备的文本编辑器就可以对IoTs2编程、下载，
宿主计算机上无需任何特殊的编程软件、编译软件和下载工具软件。使用文本编辑器编辑Python代码，保存为code.py文件，并将code.py文件
拖放至IoTs2磁盘(磁盘名称：CIRCUITPY)即可。

.. image:: /../_static/images/iots2_setup/edit_save_codepy.jpg
  :scale: 20%
  :align: center

欲善其事必先利其器！如果我们能够借助于更合适的工具，Python代码编程的效率也必将提升。尤其程序员们最喜爱某些编程环境的语法高亮、
输入记忆和自动填充、代码块自动缩进等功能都是简化代码编辑工作，提升编程效率(减少错误，减少调试时间)的利器。

随着Python语言在全球的流行，大多数桌面计算机系统都已经安装各种各样的Python代码编辑器，如Pycharm、Visual Studio、
Sublime Text等，这些软件可用于IoTs2的代码编辑、保存文件到IoTs2磁盘。

面向嵌入式系统或单板机Python编程的开源软件工具——MU，不仅支持Python3(适合桌面计算机的数值计算和网络等)编程，还支持硬件编程。
强烈推荐你使用开源的MU编辑器作为IoTs2的代编编辑、下载和调试工具。


1. 下载MU软件包
------------------------

在浏览器中打开开源MU编辑器的官网(https://codewith.mu)，点击"Download"进入下载页面，根据自己的宿主计算机系统选择下载合适的
MU软件包。

.. image:: /../_static/images/iots2_setup/dl_mu.jpg
  :scale: 20%
  :align: center

.. Attnetion:

  - 如何知道自己的电脑是32-Bit还是64-Bit？选中“我的电脑”，点击鼠标右键并从弹出菜单中选择“属性”，在弹出的窗口中点击“系统”标签即可查看
  - macOS电脑，要求OS版本必须是10.11 El Capitan或更新的版本

如果你觉得自己没有固定的电脑可用，甚至于可以下载一个U盘上可运行的MU软件包。


2. 安装MU编辑器
------------------------

1) 安装到Windows电脑

(此动画暂缺)

针对Windows系统的详细安装向导请遵照MU官网的说明 https://codewith.mu/en/howto/1.0/install_windows

2) 安装到Apple macOS电脑

macOS电脑的MU安装包的文件名为xxx.dmg，具体名称取决于你下载、保存文件时的选择。双击macOS系统的xxx.dmg(App软件包)，出现一个名称为
“mu-editor”可卸载磁盘，打开这个磁盘，你将会看到：

.. image:: /../_static/images/iots2_setup/macos_installer.png
  :scale: 10%
  :align: center

将"mu-editor"图标拖放至"Application"文件夹即可。熟悉macOS电脑的人都知道，Apple推荐使用自己的App Store安装App。显然，这样安装
的MU编辑器与App Store安装的App不同，macOS会提醒你这个App涉及安全隐私。开源的MU编辑器不涉及电脑的非安全因素，安装和运行MU时不必担
心他会损坏或影响你的电脑安全。

首次运行MU编辑器时，请打开Application文件夹，选中“MU”应用程序，点击鼠标右键，并选择“运行”，当macOS提示你是否继续执行时，选择信任
和继续。第二次及以后再启动MU编辑器应用程序，你就可以直接双击或单击MU图标即可。

针对macOS系统的详细安装向导请遵照MU官网的说明 https://codewith.mu/en/howto/1.0/install_macos


3) 制作运行MU编辑器的U盘
--------------------------------------

详见 https://codewith.mu/en/howto/1.0/use_portamu