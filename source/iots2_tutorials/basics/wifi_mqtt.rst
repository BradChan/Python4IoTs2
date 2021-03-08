物联网(IoT)和MQTT
==========================

物联网(IoT)已经彻底改变我们今天的生活方式。如果没有IoT技术做支撑，共享单车、共享汽车等便捷的生活方式几乎不可能实现。当然，IoT的应用远不止这些。

QQ、wechat(微信)是人-人互联的即时通软件，MQTT(消息队列遥测传输，Message Queuing Telemetry Transport))是实现物-物互联的即时通协议。
MQTT已经成为全球公认的IoT标准。

虽然QQ和MQTT都诞生于上世纪末，但QQ很早就被全世界华人社区所接受并逐步淘汰传统的电话通讯，QQ即时通软件的成功成就了腾讯。然而，
MQTT直到近10年才被广泛接受。虽然他们的技术方面几乎相近，但两种即时通所面向的业务领域却完全不同，
MQTT是随着IoT技术的发展日趋成熟才逐步走进我们的视野。

本向导中我们将认识MQTT，并掌握MQTT的简单应用。

关于MQTT
------------------------

MQTT是构建在TCP/IP协议栈之上的基于客户端-服务器的消息发布/订阅(publish/subscribe)传输协议，属于轻量级的即时通讯协议，
可以以极少的代码和有限的网络带宽的条件下为连接远程设备提供实时可靠的消息服务，在物联网、小型设备、移动应用等方面已有广泛的应用。
按照七层OSI模型，MQTT与HTTP等一样属于TCP/IP的应用层协议。

这里的几个关键词需要稍作解释：1) 构建在TCP/IP协议栈之上，根据MQTT所使用的TCP/IP协议栈的类型(如TCP, TLS(具备安全层传输控制的TCP), 
WS(web-socket)和WSS(具备安全加密传输的WS))，又将MQTT分为4种；2) 基于客户端-服务器，说明MQTT系统的设备分为两种角色：客户端和服务器，
一般来说消息的发布者和订阅者都是客户端，服务器仅仅负责消息的路由和分发；3) 消息发布/订阅，这是MQTT协议的基本工作模式，与传统的网络通讯相比，
这种消息发布/订阅模式可以极大地降低网络带宽的需求，传统的消息发布和接收是一对一或一对多(广播)，一对一必定会增加网络带宽需求，
而MQTT的消息发布者并不关心消息发个谁，只有订阅该消息的订阅者才会自动收到MQTT服务器转发的消息。

.. image:: /../../_static/images/iots2_tutorials/mqtt_orgin.png
  :scale: 100%
  :align: center

据考证，MQTT协议是上世纪末IBM在帮助石油和天然气公司客户设计有效的数据传输协议时首次提出，当时，为了实现数千英里长的石油和天然气管道的无人值守监控，
采取的设计方案是将管道上的传感器数据通过卫星通信传输到监控中心。如上图所示。今天我们所看到的MQTT协议的特征恰好满足当年石油和天然气公司向IBM提出的需求。

MQTT的消息发布者/订阅者之间关系示意，如下图所示：

.. image:: /../../_static/images/iots2_tutorials/mqtt_0.png
  :scale: 100%
  :align: center


MQTT的工作流程
------------------------

下面我们用三张图来简要说明MQTT的连接服务器、消息订阅、消息发布和推送的基本流程，先了解这些流程对于后面如何使用MQTT协议非常有益。

.. image:: /../../_static/images/iots2_tutorials/mqtt_1.jpg
  :scale: 100%
  :align: center

(某个客户端使用TCP协议连接到MQTT服务器/消息代理的流程)

.. image:: /../../_static/images/iots2_tutorials/mqtt_2.jpg
  :scale: 100%
  :align: center

(某个客户端订阅指定的主题topic消息的流程)

.. image:: /../../_static/images/iots2_tutorials/mqtt_3.jpg
  :scale: 100%
  :align: center

(客户端A发布一个主题消息并由MQTT服务器/代理推送给该消息的订阅者的流程)


将IoTs2连接到MQTT服务器
----------------------------

当我们初步了解MQTT协议和工作流程之后，我们开着手让IoTs2连接到MQTT服务器，为了简化问题，
我们首先是使用匿名方式登录MQTT服务器免去注册获取ID和密码的过程。

我们用一个示例程序来掌握如何让IoTs2连接到MQTT服务器并订阅和发布消息。具体的代码如下：

.. code-block::  python
  :linenos:

  import time
  from hiibot_iots2 import IoTs2
  from hiibot_iots2_mqtt import MQTTClient
  iots2 = IoTs2()
  iots2.pixels[0] = (255, 63, 0)
  iots2.screen.rotation = 180
  mqttClient = MQTTClient()
  msgTopic1 = "/test/topic1"
  msgTopic2 = "/test/topic2"
  msgTopic3 = "/test/topic3"
  def testTopic1(message):
      print('New message (topic="{}", message="{}")'.format(msgTopic1, message))
      mqttClient.publishMessage(msgTopic2, message)
  def testTopic2(message):
      print('New message (topic="{}", message="{}")'.format(msgTopic2, message))
      mqttClient.publishMessage(msgTopic3, message)
  mqttClient.subscribeTopic(msgTopic1, testTopic1)
  mqttClient.subscribeTopic(msgTopic2, testTopic2)
  mqttClient.connect()
  while True:
      mqttClient.loop()
      time.sleep(0.005)

根据前两个向导，IoTs2的WiFi必须首先连接到一个指定的AP，只要该AP与互联网是连通的，那么IoTs2就可以与MQTT服务器(消息转发代理)连接，
即可订阅、发布特定主题的消息。虽然上面的代码中并没有WiFi及其连接相关的代码，我们使用“/CIRCUITPY/lib/hiibot_iots2_mqtt.py”模块中的MQTTClient类，
在该类中会根据联网的需要适时地让IoTs2的WiFi连接到AP，并连接到MQTT代理，这些操作都在第7行代码中完成，

示例程序包含有两个函数cb_testTopic1和cb_testTopic2。你会不会觉得奇怪？这两个函数并没有被其他程序调用。这两个函数属于“发生特定事件后响应
该事件的回调函数”，你可以把他们想象成Scratch中的事件。示例程序的第25和26行分别从MQTT服务器订阅了两个主题消息，并指定cb_testTopic1函数作为
收到“/test/topic1”主题消息的事件响应，指定cb_testTopic2函数作为收到“/test/topic2”主题消息的事件响应。

该示例程序的最关键的程序语句是第24行和第27行。第24行是实例化MQTTClient类(MQTT的client类)，传入的网络参数包括：wifi，即连接MQTT服务器
的网络；sever，即MQTT服务器的网址。mqttClient是MQTTClient类的实例化变量。执行第27行语句才是真正连接到指定的MQTT服务器/代理。

在最后的无穷循环程序块中，调用MQTTClient类的loop()方法，与MQTT服务器持续不断地联系(发送心跳、接收订阅消息、侦测并更新网络连接等)。

你把本示例代码保存到BlueFi的/CIRCUITPY/code.py文件中，根据BlueFi屏幕或串口控制台提示的信息，你可以确定其连网状态、是否与MQTT服务器已经
成功连接等。


BlueFi和电脑互推消息
-------------------------------------

如果你只有一个BlueFi，如何体验MQTT的消息发布/订阅机制？可以借助于电脑端的MQTT客户端应用程序，这种客户端应用程序非常多，而且都是免费使用的。
推荐你使用“MQTTBox软件”，点击此处 `打开MQTTBox网站并下载MQTTBox软件`_ 该软件支持Linux、maxOS和Windows三种平台，选择适合自己系统的
软件点击下载并安装(如果安装过程需要向导，请参考该网页的相关文档)，然后你就可以使用这个MQTT客户端软件发布或订阅MQTT的主题消息。

.. _打开MQTTBox网站并下载MQTTBox软件: http://workswithweb.com/mqttbox.html


下图中演示如何使用MQTTBox软件创建新的MQTT客户端、订阅指定主题的消息、发布特定主题的消息。

.. image:: /../../_static/images/iots2_tutorials/mqtt_box_use.gif
  :scale: 60%
  :align: center

其中的关键步骤如下：

  - 点击“Creat MQTT Client”按钮，创建一个MQTT客户端
  - 在弹出的窗口中填写MQTT客户端的主要参数选项值，包括“MQTT Client Name”(随意输入都可以)、“Host”(www.hiibotiot.com:2883)，并展开“Protocol”选项选择“mtqq/tcp”，最后点击“save”按钮
  - 当MQTT客户端的窗口上方的出现绿色“Connect”按钮后，表明你创建的MQTT客户端已经与服务器连接上
  - 在“Topic to subscribe”下方的第一个输入框中输入订阅的主题“/test/topic3”
  - 在“Topic to public”下方的第一个输入框中输入待发布的主题“/test/topic1”，并在“Payload”下方输入框中输入消息内容(随意输入)

然后点击“Public”按钮，你看到下图的消息了吗？

.. image:: /../../_static/images/bluefi_basics/mqtt_4.jpg
  :scale: 60%
  :align: center

现在可以确认你的电脑和BlueFi通过MQTT服务器(www.hiibotiot.com:2883)相互订阅消息，当我们通过电脑发布一个主题为“/test/topic1”
消息为“hello world”之后，根据本示例的程序代码，BlueFi已经订阅了该主题消息，当MQTT服务器将电脑发布的这个消息推送给BlueFi之后，
在cb_testTopic1回调函数中将这条消息打印到串口控制台和BlueFi的LCD屏幕上，然后将此消息内容尾部添加“ (BlueFi relay1)”并以
“/test/topic2”作为主题将该消息发布出去。然后会发生什么？因为BlueFi已订阅“/test/topic2”主题消息，这个主题消息虽然是BlueFi发布的，
自己又订阅该主题消息，这个消息会被MQTT服务器再推送给BlueFi，在cb_testTopic2回调函数中将这条消息打印到串口控制台和BlueFi的LCD屏幕上，
然后将此消息内容尾部添加“ (BlueFi relay2)”并以“/test/topic3”作为主题将该消息发布出去。你电脑端的MQTTBox软件创建的MQTT客户端已
订阅“/test/topic3”主题消息，所以你在电脑上看到“hello world (BlueFi relay1) (BlueFi relay2)”消息，应该就很容易明白了。

通过这个示例，我们初步掌握MQTT的消息发布/订阅机制，并初步了解如何使用电脑搭建MQTT客户端，以及如何用BlueFi实现MQTT客户端，通过
订阅/发布消息，电脑和BlueFi之间可以相互发送IoT信息。

假设BlueFi是MQTT客户端，如果麦克风侦测到很大的声音，让BlueFi自动发布一个主题为“/security/home”消息为“Someone broke into”，
在手机或电脑上执行MQTT客户端软件，并确保已经连接到MQTT服务器，并订阅“/security/home”主题消息，当你手机或电脑端看到该消息时，
这代表着某种特殊意义。看到这里，你是否觉得用BlueFi设计一个家庭安全警报系统很容易？

-----------------------------

.. admonition::  IoT和MQTT

  - MQTT是一种应用层协议，实现物-物互联的即时通讯协议
  - MQTT采用客户端和服务器架构，客户端发布/订阅指定主题消息，服务器管理消息并向订阅者推送新发布的主题消息
  - BlueFi实现MQTT客户端，必须先让BlueFi与互联网连接，然后与MQTT服务器连接
  - BlueFi和电脑之间能够通过MQTT服务器和消息的发布/订阅机制相互推送消息

