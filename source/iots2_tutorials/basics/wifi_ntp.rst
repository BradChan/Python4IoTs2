联网获取本地时间
==========================

前一个向导中我们已经认识了BlueFi的WiFi，并启动WiFi扫描周围AP(WiFi热点)。本向导帮助我们如何将BlueFi的WiFi连接
到周围的一个可用的AP，如果这个AP与互联网是连通的，我们就可以使用网络时间服务校准本地的日期和时间。

所谓可用的AP，BlueFi必须能够扫描到，而且需要你知道这个AP的密码。网络时间服务是一种公益性的网络服务，我国已经建有十余个开放性的网络时间
服务器。网络时间服务器使用网络时间服务协议(NTP, Network Time Protocol)向服务请求方提供标准的时间校准服务。NTP的诞生完全是为网络设备
提供时间同步服务，传统的计时器需要定期手工校准时间，譬如利用电台的半点或整点报时来手工校准，今天的大多数智能设备都能够连接到互联网，并使用
NTP服务器自动校准时间。

本向导的目的是回答两个问题：1) 如何让BlueFi连接到互联网？2) 如何使用NTP服务器校准本地计时器?

---------------------------

让BlueFi接入互联网
---------------------------

电脑、Pad、手机等设备可以通过WiFi与无线路由器连接，并通过无线路由器连接到互联网，我们就可以使用搜索引擎找到自己需要的信息或者观看视频等。
BlueFi几乎与智能手机或平板有完全相同的联网和使用网络的方法，因为BlueFi也有一个内置的“无线网络设备/网卡”。

根据前一个向导的经验，如果BlueFi的WiFi能够扫描到周围的一些AP，而且你已经知道其中某些AP的密码，我们下一步就是将这个AP的名称和密码告诉
BlueFi，并编程让BlueFi连接到这个AP。如果这个AP与互联网是连通的，我们的BlueFi即可通过这个AP接入互联网。

如何将AP的名称（ssid)和密码(password)告诉BlueFi呢? 我们有两种方法：

  - 第1种方法是将这个AP的ssid和password两个字符串分别保存在“/CIRCUITPY/secrets.py”文件的对应位置，BlueFi需要联网时自动去这个文件中读取这些信息
  - 第2种方法是将这个AP的ssid和password两个字符串直接用Python程序接口传给BlueFi的网卡

虽然两种方法是等价的，建议使用第1种方法，即便是你分享自己的代码给其他人时，你的AP信息不会泄露给别人。secrets.py文件的格式如下：

.. code-block::  
  :linenos:

  secrets = {
    "ssid": "your_ap_name",
    "password": "your_ap_password",
    "timezone": "Asia/Shanghai", 
    "broker": 'www.hiibotiot.com',
    "user": 'your_iot_name',
    "pass": 'your_iot_password'
  }

这是一个JSON格式化的文本型“key:value”信息对，也可以用Python字典型数据结构来访问。每一个“:”前的字符串是“key”，“:”后的字符串是这个“key”
对应的“value”。

下面我们使用第2种方法设计一个让BlueFi连接到互联网的程序示例。程序代码如下：

.. code-block::  python
  :linenos:

  from hiibot_bluefi.wifi import WIFI
  wifi=WIFI()

  while not wifi.esp.is_connected:
      try:
          wifi.esp.connect_AP(b"your_ap_name", b"your_ap_password")
      except RuntimeError as e:
          print("could not connect to AP, retrying: ", e)
          continue
  print("Connected to", str(wifi.wifi.ssid, "utf-8"), "\tRSSI: {}".format(wifi.wifi.signal_strength) )
  print("My IP address is {}".format(wifi.wifi.ip_address()))

  wifi.esp.reset()

  while True:
      pass

本示例的前2行程序的作用分别是，从“/CIRCUITPY/lib/hiibot_bluefi/”文件夹的“wifi.py”模块种导入“WIFI”类Python接口，并实例化
为“wifi”名称。然后我们就可以引用“wifi”使用BlueFi的无线WiFi网卡。

第4～9行是一个条件循环，检测条件是“wifi.esp.is_connected”，当BlueFi的WiFi连接到AP后“wifi.esp.is_connected”被置为True。显然，
如果WiFi未连接到AP，这个条件是成立的，则执行第6行程序，即连接指定的AP(指定该AP的名称和密码)，如果连接失败就用BlueFi的LCD显示屏和
串口控制台输出“could not connect to AP, retrying: ('Failed to connect to ssid', b'your_ap_name')”，并再次返回第6行尝试
再次连接，如此重复。如果你给的AP名称和密码有任何错误，将导致第4～9行程序成为一个死循环。根据提示信息，你就可以掌握循环的次数。

一旦成功地连接到指定的AP，BlueFi将输出提示信息并输出自己的IP地址。

由于本示例仅仅是测试联网，当程序执行到第13行时，我们关闭BlueFi的WiFi以节电。相比较其他功能单元，BlueFi的WiFi属于高耗能，使用之后应
及时关闭。

与第1种设置WiFi名称和密码相比，第2种方法使用本示例第6行的Python接口程序将AP名称和密码作为参数直接传递给该接口。如果你分享这个示例代码给
别人时，你的AP名称和密码也同时泄露出去了。

下面示例采用第1种方法设置AP的名称和密码：

.. code-block::  python
  :linenos:

  from hiibot_bluefi.wifi import WIFI
  wifi=WIFI()

  # Get wifi details and more from a /CIRCUITPY/secrets.py file
  try:
      from secrets import secrets
  except ImportError:
      print("WiFi secrets are kept in secrets.py, please add them there!")
      raise

  while not wifi.esp.is_connected:
      try:
          wifi.wifi.connect()
      except RuntimeError as e:
          print("could not connect to AP, retrying: ", e)
          continue
  print("Connected to", str(wifi.wifi.ssid, "utf-8"), "\tRSSI: {}".format(wifi.wifi.signal_strength) )
  print("My IP address is {}".format(wifi.wifi.ip_address()))

  wifi.esp.reset()

  while True:
      pass

与前一个示例相比，该示例的第13行代码，即用于连接AP的Python接口程序，我们并没有传递参数，执行该程序语句时会自动到“/CIRCUITPY/secrets.py”文件
中读取AP的名称和密码，并自动连接该AP。

如果你分享这个程序代码时，记得提醒代码使用者需要自己修改“/CIRCUITPY/secrets.py”文件中的“ssid”和“password”两个key的value。


用互联网同步本地时间
---------------------------

当我们搞清楚如何让BlueFi的WiFi连接到互联网之后，我们就可以使用NTP服务校准/同步本地的日期和时间。什么是NTP? 请自行使用搜索引擎
查阅相关资料，NTP是TCP/IP协议栈中的一种应用层协议。

下面我们使用国际时间NTP服务器(域名：http://worldtimeapi.org/)来校准本地时间，这个服务器提供多种NTP服务接口，本示例使用“按照
本地的IP地址返回当地的日期和时间信息”，这个NTP服务器的服务接口：

  - http://worldtimeapi.org/api/timezone 返回所有时区的当前日期和时间(如果你需要设计一个五星级酒店大堂使用的数字计时器)
  - http://worldtimeapi.org/api/timezone/:Asia/Shanghai 返回上海时区(中国时间)的当前日期和时间
  - http://worldtimeapi.org/api/ip/:ipv4_addr 返回指定IP所在地区的当前日期和时间

本示例程序的代码如下：

.. code-block::  python
  :linenos:

  import time
  from hiibot_bluefi.wifi import WIFI
  import rtc

  print("we will get local time from a NTP")
  TIME_API = "http://worldtimeapi.org/api/ip"

  wifi = WIFI()
  the_rtc = rtc.RTC()

  response = None
  while True:
      try:
          print("Fetching json from", TIME_API)
          response = wifi.wifi.get(TIME_API)
          break
      except (ValueError, RuntimeError) as e:
          print("Failed to get data, retrying\n", e)
          continue

  wifi.esp.reset() # close wifi to save power

  json = response.json()
  current_time = json["datetime"]
  the_date, the_time = current_time.split("T")
  year, month, mday = [int(x) for x in the_date.split("-")]
  the_time = the_time.split(".")[0]
  hours, minutes, seconds = [int(x) for x in the_time.split(":")]

  # We can also fill in these extra nice things
  year_day = json["day_of_year"]
  week_day = json["day_of_week"]
  is_dst = json["dst"]

  now = time.struct_time( (year, month, mday, hours, minutes, seconds, week_day, year_day, is_dst) )
  print(now)
  the_rtc.datetime = now

  while True:
      str_date = "{}/{}/{} - Week {} ".format(the_rtc.datetime.tm_year, the_rtc.datetime.tm_mon, \
                                              the_rtc.datetime.tm_mday, the_rtc.datetime.tm_wday+1)
      str_time = "{}:{}:{} ".format(the_rtc.datetime.tm_hour, the_rtc.datetime.tm_min, the_rtc.datetime.tm_sec)
      print(str_date, str_time)
      time.sleep(1)

你首先将本示例代码保存到BlueFi的/CIRCUITPY/code.py文件中，务必记得修改secrets.py文件中的ssid和password两个选项的值，
当BlueFi执行本示例程序的第15行，即“response = wifi.wifi.get(TIME_API)”，自动使用secrets.py的信息连接指定的AP，
与AP成功连接后调用“http://worldtimeapi.org/”的时间服务接口，按BlueFi的本地IP获取当前日期和时间，并将返回结果保存在
response变量中。

如果你用web浏览器打开http://worldtimeapi.org/页面时，将会看到该服务的返回结果说明。根据说明我们可以知道，reponse是
一个JSON格式化的文本字符串信息，本示例程序的第23～28行通过解析这个JSON格式化的信息流确定本地的日期和时间，并分别保存在
year, month, mday, hours, minutes, seconds等6个变量中，然后在第30和第31行中解析分别解析出当前是一年中的第几天、
本周当中的第几天并保存到year_day和week_day变量中。

在第35行代码中，我们按照time类的struct_time成员变量结构将当前日期和时间信息组成一个系统内常用的日期和时间信息结构，并保存到
变量now中，第37行代码是将now更新到本地RTC。至此，BlueFi本地的RTC单元的日期和时间已经与国际时间保持一致了。

在本示例程序的最后一个程序块(无穷循环程序块)中，读取本地RTC的日期和时间，并格式化后输出到BlueFi的LCD屏幕和串口控制台上，
你会发现“秒”数据的不断变化。

你或许会问，这样的方法同步本地时间，是否存在误差？当然存在，受你的无线网络状况、执行NTP服务的CPU速度等因素影响，这种方法校准
的本地时间与国际时间相差几十到几百毫秒。

如果这个误差太大，不能满足你的应用，你觉得如何减少这一误差呢？

-------------------------------

.. admonition:: 
  总结：

    - 将AP的名称和密码告知BlueFi
    - 让BlueFi连接到互联网
    - 从互联网的NTP服务器获取BlueFi本地的当前日期和时间

