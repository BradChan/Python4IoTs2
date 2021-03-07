扫描周围的WiFi热点并连接到指定的AP
================================

这一节教程中，我们将初步体验IoTs2的WiFi。WiFi是一种广泛应用于固定的或移动范围较小的设备，为此类设备提供高速的高吞吐量的无线通讯接口。
在手机、平板电脑、桌面电脑、个人数字终端等设备上WiFi是标配的功能单元，IoTs2也具有此类设备完全相同的WiFi通讯接口。

近些年，IoT设备的NFC(近场通讯)技术只能解决2厘米以内的无线电波通讯，IoT的最后几米是蓝牙，那么IoT的最后几十米是WiFi。据业内人士的专业预测，
新兴的WiFi6技术将与5G技术将分庭抗争室外和室内的无线电波通讯技术应用领域，各自都会有巨大的市场潜力。近两年的4G资费急剧下降，
室外的甚至部分室内的无线电波通讯方案已经让我们可以放弃WiFi，但是室内尤其非工业现场的住宅和办公区域仍是WiFi的天下，WiFi6是非常有竞争力的方案。

目前，WiFi是几十米到数百米距离内的无线电波通讯技术的最佳选择，虽然还有其他的选择，但综合考虑设备、流量和资费等成本，
WiFi的确是无可争议的无线电波通讯方案。那么WiFi的工作原理是啥样？从本节开始，我们通过一系列的教程帮助你逐步理解这一重要的IoT技术原理和实现方法。

本节先使用IoTs2的WiFi通道让你初步体验“scan周围WiFi热点并连接到指定的热点”，任何WiFi设备，只要具备交互能力，scan周围热点是其最重要的基础功能之一。
示例代码如下：

.. code-block::  python
  :linenos:

    import time
    import wifi
    from hiibot_iots2 import IoTs2
    iots2 = IoTs2()
    iots2.screen.rotation = 270  # rotate IoTs2 screen 
    iots2.pixels[0] = (255,0,0)  # show RED color
    avaliableAP_list = []  # to save the avaliable APs
    print('start to scan APs')
    for network in wifi.radio.start_scanning_networks():
        time.sleep(0.05)
        print("\t'%s'\t\tRSSI: %d\tChannel: %d" % (network.ssid, network.rssi, network.channel))
        avaliableAP_list.append( network.ssid ) # append the AP to the list
    wifi.radio.stop_scanning_networks()  # stop scan
    iots2.pixels[0] = (127,127,0) # show YELLOW color
    print('AP scanning Done')
    try:
        from secrets import secrets # import secrets.py module
    except ImportError:
        print("WiFi secrets are kept in secrets.py, please add them there!")
        raise
    theAP = None
    for ap in avaliableAP_list:  # check avaliable APs
        if ap==secrets["ssid"]:
            theAP = ap
            break
    if theAP==None:
        print("Not this AP, please to modify the secrects.py")
        iots2.pixels[0] = (255,0,0)  # show RED color
        while True:
            pass
    elif not wifi.radio.ipv4_address:
        macaddr = 'My MAC Address: 0x'
        for addr in wifi.radio.mac_address:
            macaddr += '{:02X}'.format(addr) 
        print( macaddr )
        print("Connecting to WiFi AP (SSID: %s) ..." % secrets["ssid"])
        print("Connecting to %s" % secrets["ssid"])
        wifi.radio.connect(secrets["ssid"], secrets["password"])
    print("Connected to %s!" % secrets["ssid"]) 
    iots2.pixels[0] = (0,0,255) 
    print("My IP address is {}".format(wifi.radio.ipv4_address))
    while True:
        time.sleep(10)

本示例程序只实现IoTs2发现(扫描)周围的WiFi热点(AP)，并按信号强度有高到低的顺序地输出到LCD屏幕或Python的串口控制台。
请将本示例程序保存到IoTs2的/CIRCUITPY/code.py文件中，IoTs2将开启内部WiFi通道，并开始扫描周围WiFi热点，
最后把scan到的热点按信号强度顺序地输出到屏幕并保存在一个列表中，然后与/CIRCUITPY/secrets.py文件中的"ssid"项的值对比，
如果附近热点的列表中有与之匹配的SSID，则检测WiFi是否已经连接到热点，如果未连接则将WiFi连接到该热点，并输出IoTs2的IP地址。

示例代码分析：

    - 第1行，导入一个Python内建的模块“time”
    - 第2行，导入一个Python内建的模块“wifi”
    - 第3行，从“/CIRCUITPY/lib/hiibot_iots2.py”模块中导入一个名叫“IoTs2”的类，即IoTs2模块类
    - 第4行，将导入的“IoTs2”类实例化为一个实体对象，名叫“iots2”
    - 第5行，将IoTs2的LCD屏幕旋转为90/270度，即横屏显示效果
    - 第6行，IoTs2的RGB彩灯显示红色
    - 第7行，定义一个空的列表，名称为avaliableAP_list
    - 第8行，向LCD屏幕或串口控制台输出字符串“start to scan APs”，提示开始扫描附近的WiFi AP
    - 第9～12行，用一个有限次的循环，逐个地将扫描到的附近热点的名称(SSID)、信号强度、所用信道等信息打印到LCD屏幕或串口控制台上，并将所有SSID保存在列表avaliableAP_list中
    - 第13行，停止WiFi的扫描操作
    - 第14行，IoTs2的RGB彩灯显示黄色
    - 第15行，向LCD屏幕或串口控制台输出字符串“AP scanning Done”，提示扫描结束
    - 第16～20行，尝试导入“/CIRCUITPY/secrets.py”文件，该文件中保存有IoTs2的联网配置信息
    - 第21～25行，根据“secrets.py”文件的"ssid"项的值，判断前面扫描到的周围热点中是否有该热点
    - 第26～30行，如果“secrets.py”文件的"ssid"项的值所给定的SSID与周围热点名称都不匹配，则让IoTs2的RGB彩灯亮红色，输出提示信息后让程序进入死循环
    - 第31～38行，如果WiFi的IP地址无效则说明未连接到指定的AP，首先打印MAC信息，然后尝试连接到指定的AP。注意，这一连接过程是阻塞式的，除非出现错误，否则一直等到连接成功
    - 第39行，提示已经连接到指定的AP，并输出该AP的SSID名称
    - 第40行，让IoTs2的RGB彩灯显示蓝色，提示已经连接成功
    - 第41行，将本机的IP地址输出到LCD屏幕或串口控制台
    - 第42行，一个无穷循环的程序块
    - 第43行(无穷循环程序块的第1行)，执行time的sleep方法，参数为10秒


-----------------------------

.. admonition:: 
  总结：

    - IoT的无线电波通讯
    - WiFi
    - 扫描周围的可用热点
    - 连接到一个指定的WiFi AP
    - MAC地址
    - IP地址(IPv4的地址)
    - 本节中，你总计完成了43行代码的编写工作

------------------------------------

.. Important::
  **WiFi类的属性和接口**

    - radio (wifi的子类，用于访问IoTs2的WiFi通讯接口)
    - radio.enable (属性值，可读可写的，有效值为False和True分别为使能和禁止IoTs2的WiFi接口
    - radio.hostname (属性值，只读的，固定为“HiiBot_IoTs2”，当IoTs2连接到一个AP后，在AP的客户端列表中将会看到该模块的名称字符串)
    - radio.mac_address (属性值，只读的，每个IoTs2的MAC地址都是固定的，这是一个6项的列表数据)
    - radio.ipv4_address (属性值，只读的，当IoTs2与一个AP连接后，AP会自动为IoTs2分配一个IPv4地址，形式为这是一个6项的列表数据。未连接到AP时，该属性值为None)
    - radio.ipv4_dns (属性值，只读的，当IoTs2与一个AP连接后自动获取dns的IPv4地址。未连接到AP时，该属性值为None)
    - radio.ipv4_gateway (属性值，只读的，当IoTs2与一个AP连接后自动获取GateWay的IPv4地址。未连接到AP时，该属性值为None)
    - radio.ipv4_subnet (属性值，只读的，当IoTs2与一个AP连接后自动获取SubNet的IPv4地址。未连接到AP时，该属性值为None)
    - radio.ping() (函数，输入参数：xx.xx.xx.xx形式的IPv4地址), 该接口的用法示例见文末的示例程序
    - radion.start_scanning_networks() (函数，无输入参数，用法见上面的示例)
    - radio.stop_scanning_networks() (函数，无输入参数，无返回值，停止正在执行的AP扫描)
    - radio.connect() (函数，两个字符串型输入参数：'ssid'和'password'，无返回值。这是一个阻塞式接口函数，除非出错将立即退出，否则将一直等待到连接到指定的AP后才会返回)
    - radio.ap_info (wifi.Network子类，用于访问IoTs2的WiFi接口的状态属性，使用“wifi.radio.ap_info.”或许以下的IoTs2 WiFi接口状态的属性值：

        - authmode: 只读的，返回'WPA_WPA2_PSK'等类型的安全认证模式的字符串
        - bssid: 只读的，返回bytearray型
        - ssid: 只读的，返回已经连接的AP名称，未连接到AP时该属性值未None
        - rssi: 只读的，返回当前的信号强度
        - chennel: 只读的，返回当前连接AP所用的信号编号(有效值范围是0~11)
        - country: 只读的，返回当前连接的AP所属的国家，如“CN”表示中国

关于wifi.radio.ping()接口函数的用法，示例代码如下：

.. code-block::  python
  :linenos:

    import wifi
    import ipaddress
    wifi.radio.connect('your_ap_name', 'your_ap_password')
    dest_ip = ipaddress.ip_address('192.168.1.1')
    wifi.radio.ping(dest_ip)

建议使用REPL模式执行上面的示例代码。