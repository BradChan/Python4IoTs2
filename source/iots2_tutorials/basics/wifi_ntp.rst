联网获取本地时间
==========================

前一个向导中我们已经认识了IoTs2的WiFi，启动WiFi扫描周围AP(WiFi热点)并连接到指定的AP。
本向导帮助我们如何将IoTs2的WiFi连接到周围的一个可用的AP，如果这个AP与互联网是连通的，我们就可以使用网络时间服务校准本地的日期和时间。

所谓可用的AP，IoTs2必须能够扫描到，而且需要你知道这个AP的密码。网络时间服务是一种公益性的网络服务，我国已经建有十余个开放性的网络时间服务器。
网络时间服务器使用网络时间服务协议(NTP, Network Time Protocol)向服务请求方提供标准的时间校准服务。NTP的诞生完全是为网络设备提供时间同步服务，
传统的计时器需要定期手工校准时间，譬如利用电台的半点或整点报时来手工校准，今天的大多数智能设备都能够连接到互联网，并使用NTP服务器自动校准时间。

本向导的目的是回答两个问题：1) 如何让IoTs2连接到互联网？2) 如何使用NTP服务器校准本地计时器?

---------------------------

让IoTs2接入互联网
---------------------------

电脑、Pad、手机等设备可以通过WiFi与无线路由器连接，并通过无线路由器连接到互联网，我们就可以使用搜索引擎找到自己需要的信息或者观看视频等。
IoTs2几乎与智能手机或平板有完全相同的联网和使用网络的方法，因为IoTs2也有一个内置的“无线网络设备/网卡”。

根据前一个向导的经验，如果IoTs2的WiFi能够扫描到周围的一些AP，而且你已经知道其中某些AP的密码，我们下一步就是将这个AP的名称和密码告诉IoTs2，
并编程让IoTs2连接到这个AP。如果这个AP与互联网是连通的，我们的IoTs2即可通过这个AP接入互联网。

如何将AP的名称（ssid)和密码(password)告诉IoTs2呢? 我们有两种方法：

  - 第1种方法是将这个AP的ssid和password两个字符串分别保存在“/CIRCUITPY/secrets.py”文件的对应位置，IoTs2需要联网时自动去这个文件中读取这些信息
  - 第2种方法是将这个AP的ssid和password两个字符串直接用Python程序接口传给IoTs2的wifi.radio类

虽然两种方法是等价的，建议使用第1种方法，即便是你分享自己的代码给其他人时，你的AP信息不会泄露给别人。secrets.py文件的格式如下：

.. code-block::  
  :linenos:

  secrets = {
    "ssid": "your_ap_name",
    "password": "your_ap_password",
    "timezone": "Asia/Shanghai",  # Check http://worldtimeapi.org/timezones
    "broker":"www.hiibotiot.com",
    "hiibotiot_user":"anyone",
    "hiibotiot_password":"12345678"
  }

这是一个JSON格式化的文本型“key:value”信息对(即字典)，也可以用Python字典型数据结构来访问。每一个“:”前的字符串是“key”，
“:”后的字符串是这个“key”对应的“value”。

下面我们使用第2种方法设计一个让BlueFi连接到互联网的程序示例。程序代码如下：

.. code-block::  python
  :linenos:

  import wifi
  from hiibot_iots2 import IoTs2
  iots2 = IoTs2()
  iots2.screen.rotation = 270
  wifi.radio.enabled = True
  while not wifi.radio.ipv4_address:
      # ConnectionError: No network with that ssid?
      wifi.radio.connect('your_ap_name', 'your_ap_password') 
  print("Connected to", str(wifi.radio.ap_info.ssid, "utf-8"), "\tRSSI: {}".format(wifi.radio.ap_info.rssi) )
  print("My IP address is {}".format(wifi.radio.ipv4_address))
  wifi.radio.enabled = False
  while True:
        pass

根据前一节的内容，我们不难理解上面的程序代码，如果不修改第8行代码中的字符串‘your_ap_name’和‘your_ap_password’，
直接将程序保存到IoTs2的/CIRCUITPY/code.py文件中，我们将会看到“ConnectionError: No network with that ssid”错误提示。
你的AP名称和连接密码正好是‘your_ap_name’和‘your_ap_password’的概率极低，将你的IoTs2附近可用的AP和密码分别填入这两个字符串中，
我们将会看到正确的结果。

第9~10行将已经连接到的AP名称、当前的信号强度和IP地址输出到LCD屏幕和串口控制台上。第11行将WiFi关闭，关闭WiFi的目的是可以降低IoTs2的功耗，
本示例仅仅是为了演示连接WiFi热点而已。

与第1种设置WiFi名称和密码相比，第2种方法使用本示例第8行的Python接口程序将AP名称和密码作为参数直接传递给该接口。
如果你分享这个示例代码给别人时，你的AP名称和密码也同时泄露出去了。

下面示例采用第1种方法设置AP的名称和密码：

.. code-block::  python
  :linenos:

  import wifi
  # Get wifi details and more from a /CIRCUITPY/secrets.py file
  try:
      from secrets import secrets
  except ImportError:
      print("WiFi secrets are kept in secrets.py, please add them there!")
      raise
  from hiibot_iots2 import IoTs2
  iots2 = IoTs2()
  iots2.screen.rotation = 270
  wifi.radio.enabled = True
  while not wifi.radio.ipv4_address:
      wifi.radio.connect(secrets["ssid"], secrets["password"])
  print("Connected to", str(wifi.radio.ap_info.ssid, "utf-8"), "\tRSSI: {}".format(wifi.radio.ap_info.rssi) )
  print("My IP address is {}".format(wifi.radio.ipv4_address))
  wifi.radio.enabled = False
  while True:
        pass

与前一个示例相比，该示例的第13行代码，即用于连接AP的Python接口程序，我们并没有传递参数，
执行该程序语句时会自动到“/CIRCUITPY/secrets.py”文件中读取AP的名称和密码，并自动连接该AP。

如果你分享这个程序代码时，记得提醒代码使用者需要自己修改“/CIRCUITPY/secrets.py”文件中的“ssid”和“password”两个key的value。


用互联网同步本地时间
---------------------------

当我们搞清楚如何让IoTs2的WiFi连接到互联网之后，我们就可以使用NTP服务校准/同步本地的日期和时间。什么是NTP? 
请自行使用搜索引擎查阅相关资料，NTP是TCP/IP协议栈中的一种应用层协议。

下面我们使用国际时间NTP服务器(域名：http://worldtimeapi.org/)来校准本地时间，这个服务器提供多种NTP服务接口，本示例使用“按照
本地的IP地址返回当地的日期和时间信息”，这个NTP服务器的服务接口：

  - http://worldtimeapi.org/api/timezone 返回所有时区的当前日期和时间(如果你需要设计一个五星级酒店大堂使用的数字计时器)
  - http://worldtimeapi.org/api/timezone/:Asia/Shanghai 返回上海时区(中国时间)的当前日期和时间
  - http://worldtimeapi.org/api/ip/:ipv4_addr 返回指定IP所在地区的当前日期和时间

本示例程序的代码如下：

.. code-block::  python
  :linenos:

  import time
  import rtc
  import wifi
  import ipaddress
  import ssl
  import wifi
  import socketpool
  import adafruit_requests
  from hiibot_iots2 import IoTs2
  iots2 = IoTs2()
  iots2.screen.rotation = 180
  iots2.pixels[0] = (255,0,0)
  the_rtc = rtc.RTC()
  response = None
  weekDayAbbr = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  try:
      from secrets import secrets
  except ImportError:
      print("WiFi secrets are kept in secrets.py, please add them there!")
      raise
  print("Connecting to %s" % secrets["ssid"])
  wifi.radio.connect(secrets["ssid"], secrets["password"])
  print("Connected to %s!" % secrets["ssid"])
  iots2.pixels[0] = (0,0,255)
  print("My IP address is {}".format(wifi.radio.ipv4_address))
  pool = socketpool.SocketPool(wifi.radio)
  requests = adafruit_requests.Session(pool, ssl.create_default_context())
  response = requests.get("http://worldtimeapi.org/api/timezone/Asia/Shanghai", timeout=60.0)
  iots2.pixels[0] = (0,255,255)
  rgb_gright = 0.1
  ######### fade IoTs2 RGB pixels #########
  def fadeRGB() :
      global rgb_gright
      rgb_gright += 0.005
      if rgb_gright>0.1:
          rgb_gright = 0.0
      iots2.pixels.brightness = rgb_gright
      iots2.pixels.show()
      time.sleep(0.1)
  ######### Parse Date&Time from JSON #########
  if response.status_code == 200:
      print("We got a NTP server")
      iots2.pixels[0] = (0,255,0)
      json = response.json()
      print(json)  # print all message
      current_time = json["datetime"]
      the_date, the_time = current_time.split("T")
      print(the_date)
      year, month, mday = [int(x) for x in the_date.split("-")]
      the_time = the_time.split(".")[0]
      print(the_time)
      hours, minutes, seconds = [int(x) for x in the_time.split(":")]
      # We can also fill in these extra nice things
      year_day = json["day_of_year"]
      week_day = json["day_of_week"]
      # Daylight Saving Time (夏令时)?
      is_dst = json["dst"] 
      now = time.struct_time(
          (year, month, mday, hours, minutes, seconds+1, week_day, year_day, is_dst) )
      the_rtc.datetime = now
      while True:
          print( "  {}-{}-{}".format(
              the_rtc.datetime.tm_year,  
              the_rtc.datetime.tm_mon,  
              the_rtc.datetime.tm_mday, ) 
              )
          print( "  " + weekDayAbbr[the_rtc.datetime.tm_wday] )
          print( "  {}:{}:{}".format(
              the_rtc.datetime.tm_hour, 
              the_rtc.datetime.tm_min, 
              the_rtc.datetime.tm_sec, ) 
              )
          ipv4 = ipaddress.ip_address('182.61.200.6')
          print('  ping time:', wifi.radio.ping(ipv4))
          for _ in range(520):
              fadeRGB()
  else:
      print("Getting time failed")

你首先将本示例代码保存到IoTs2的/CIRCUITPY/code.py文件中，务必记得修改secrets.py文件中的ssid和password两个选项的值，
当IoTs2执行本示例程序时，如果与AP成功连接后调用“http://worldtimeapi.org/”的时间服务接口，即第28行代码，从NTP服务器请求本地时间，
并将请求结果保存在response变量中。

如果你用web浏览器打开http://worldtimeapi.org/页面时，将会看到该服务的返回结果说明。根据说明我们可以知道，
reponse是一个JSON格式化的文本字符串信息，本示例程序的第42～55行通过解析这个JSON格式化的信息流确定本地的日期和时间，
并分别保存在year, month, mday, hours, minutes, seconds,year_day和week_day等变量中。

在本示例程序的最后一个程序块(无穷循环程序块)中，读取本地RTC的日期和时间，并格式化后输出到IoTs2的LCD屏幕和串口控制台上，
你会发现“秒”数据的不断变化。同时，为了更好滴理解“wifi.radio.ping()”接口函数的用法，无穷循环中也不断地你用该接口ping百度服务器，
即'182.61.200.6'地址，并输出ping操作的耗时。

你或许会问，这样的方法同步本地时间，是否存在误差？当然存在，受你的无线网络状况、执行NTP服务的CPU速度等因素影响，这种方法校准
的本地时间与国际时间相差几十到几百毫秒。

如果这个误差太大，不能满足你的应用，你觉得如何减少这一误差呢？

-------------------------------

.. admonition:: 
  总结：

    - 将AP的名称和密码告知IoTs2
    - 让IoTs2连接到互联网
    - 从互联网的NTP服务器获取IoTs2本地的当前日期和时间

