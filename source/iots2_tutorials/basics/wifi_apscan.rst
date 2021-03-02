扫描周围的WiFi热点
==========================

这一节教程中，我们将初步体验BlueFi的WiFi。

BlueFi的名字从何而来？Blue(Tooth-Wi)Fi，真正地实现蓝牙和WiFi同时共存的单板机。在蓝牙键盘那一节中我们已经体验过BlueFi的蓝牙的便
捷性，然而蓝牙仅仅局限于10米以内的无线电波通讯解决方案，而且近几年发展起来的低功耗蓝牙(BLE)技术使得蓝牙耳机拥有百亿级市场，这也是我
们以非常慎重的态度来增强BlueFi的蓝牙技术的缘由。

最近的IoT设备是NFC(近场通讯)技术(只能解决2厘米以内的无线电波通讯)，IoT的最后几米是蓝牙，那么IoT的最后几十米是WiFi。据业内人士的专业
预测，新兴的WiFi6技术将与5G技术将分庭抗争室外和室内的无线电波通讯技术应用领域，各自都会有巨大的市场潜力。近两年的4G资费急剧下降，
室外的甚至部分室内的无线电波通讯方案已经让我们可以放弃WiFi，但是室内尤其非工业现场的住宅和办公区域仍是WiFi的天下，WiFi6是非常有竞争
力的方案。

目前，WiFi是几十米到数百米距离内的无线电波通讯技术的最佳选择，虽然还有其他的选择，但综合考虑设备、流量和资费等成本，WiFi的确是无可争议
的无线电波通讯方案。那么WiFi的工作原理是啥样？从本节开始，我们通过一系列的教程帮助你逐步理解这一重要的IoT技术原理和实现方法。

本节先使用BlueFi的WiFi通道让你初步体验“scan周围WiFi热点”，任何WiFi设备，只要具备交互能力，scan周围热点是其最重要的基础功能之一。

.. code-block::  python
  :linenos:

    import time
    from hiibot_bluefi.wifi import WIFI
    from hiibot_bluefi.basedio import NeoPixel
    wifi = WIFI()
    pixels = NeoPixel()
    pixels.fillPixels( (255,0,0) )
    if wifi.esp.status != 0xFF:
        pixels.fillPixels( (0,255,0) ) 
        print("WiFi be found and in idle mode")

    print("MAC addr:", [hex(i) for i in wifi.esp.MAC_address])

    for ap in wifi.esp.scan_networks():
        print("\t%s  RSSI: %d" % (str(ap['ssid'], 'utf-8'), ap['rssi']))

    pixels.fillPixels( (0,0,255) )
    wifi.esp.reset()
    print("Program Done!")

    while True:
        pass


本示例程序只实现BlueFi发现周围的WiFi热点，并按信号强度有高到低的顺序列出来。请将本示例程序保存到BlueFi的
/CIRCUITPY/code.py文件中，BlueFi将开启内部WiFi通道，在LCD屏幕上显示自己的MAC地址，并开始扫描周围WiFi热点，最后把scan到的
热点按信号强度顺序地列出来，程序结束。

WiFi单元属于BlueFi上功率最大的组件，当我们使用WiFi完毕后，应使用“wifi.esp.reset()”关闭WiFi功能以达到节能之目的。
