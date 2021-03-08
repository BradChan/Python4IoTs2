# The MIT License (MIT)
#
# Copyright (c) 2020 HiiBot for Hangzhou Leban Tech. Ltd
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`iots2 extend board -- RunGo`
================================================================================

the board-supported-package for the RunGo car chassis to support HiiBot IoTs2 module, include
  (RunGo that a car chassis from HiiBot)
1) 3x NeoPixel RGB pixels, IO0 be used
2) 1x Color sensor (on the bottom of RunGo car chassis), IO7 (colorSensor) be used (analogIn)
3) 2x Lighting sensor, IO8 (leftLightingSensor), and IO9 (rightLightingSensor) were used
4) 2x Head LED, IO17 (rightHeadLED), and IO18 (leftHeadLED) were used
5) 2x Tracking module for tracking, IO3 (leftTrackSensor) and IO4 (rightTrackSensor) were used
6) 1x Ultrasonic module for range measurement (Distance sensor), IO11 (trig) and IO10 (echo) were used
7) 2x Motor, IO41 (rightMotor1IN), IO42 (rightMotor2IN), IO12 (leftMotor1IN), and IO40 (leftMotor2IN) were used

those interface are used as following:


* Author(s): HiiBot

Implementation Notes
--------------------

**Hardware:**
.. "* `HiiBot IoTs2 - a funny production with WiFi`_"

**Software and Dependencies:**
* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases
 * Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
 * Adafruit's Register library: https://github.com/adafruit/Adafruit_CircuitPython_Register

"""
import time
import board
from analogio import AnalogIn
from pulseio import PWMOut
import neopixel
from debouncedButton import Debouncer
from digitalio import DigitalInOut, Direction, Pull
_USE_PULSEIO = False
try:
    from pulseio import PulseIn
    _USE_PULSEIO = True
except ImportError:
    pass  # This is OK, we'll try to bitbang it!


__version__ = "0.1.0-auto.0"
__repo__ = "https://github.com/HiiBot/Hiibot_CircuitPython_IoTs2.git"

__CW  = 0
__CCW = 1

class RunGo:

    groundColor_list = ((128,128,128),(255,0,0),(128,128,0),(0,255,0),(0,128,128),(0,0,255),(128,0,128))
    groundColor_name = ('White','Red','Yellow','Green','Cyan','Blue','Purple')

    def __init__(self, enButtons = True):
        self._buttonA = None
        self._buttonB = None
        self._enbuttons = False
        if enButtons:
            self._enbuttons = True
            self._buttonA = DigitalInOut(board.IO43)
            self._buttonA.switch_to_input(pull=Pull.UP)
            self._db_buttonA = Debouncer(self._buttonA, 0.01, True)
            self._buttonB = DigitalInOut(board.IO44)
            self._buttonB.switch_to_input(pull=Pull.UP)
            self._db_buttonB = Debouncer(self._buttonB, 0.01, True)

        # 3x Neopixels RGB pixels: IO0
        self._pixels = neopixel.NeoPixel( board.IO0, 3,  \
                    brightness=0.5, auto_write=False, pixel_order=neopixel.GRB )
        self._colors = [(255,0,0), (0,255,0), (0,0,255)]
        for i in range(3):
            self._pixels[i] = self._colors[i]
        self._pixels.show()
        self._pixelsRotationDt = 0.2
        self._pixelsRotationSt = time.monotonic()
        # Sense color Sensor (颜色传感器):  IO7
        self._colorSensor = AnalogIn(board.IO7)
        # Lighting Sensor (光强度传感器):  IO8--leftLightSensor, IO9--rightLightSensor
        self._leftLightSensor = AnalogIn(board.IO8)
        self._rightLightSensor = AnalogIn(board.IO9)
        # left and right head-LED: IO17--rightHeadLED, IO18--leftHeadLED
        self._leftHeadLED = DigitalInOut(board.IO18)
        self._leftHeadLED.direction = Direction.OUTPUT
        self._leftHeadLED.value = 0
        self._rightHeadLED = DigitalInOut(board.IO17)
        self._rightHeadLED.direction = Direction.OUTPUT
        self._rightHeadLED.value = 0
        # Ultrasonic module (超声波模块):  IO11--trig, IO10--echo
        self._timeout = 0.1
        self._trig = DigitalInOut(board.IO11)
        self._trig.direction = Direction.OUTPUT
        self._trig.value = 0
        if _USE_PULSEIO:
            self._echo = PulseIn(board.IO10)
            self._echo.pause()
            self._echo.clear()
        else:
            self._echo = DigitalInOut(board.IO10)
            self._echo.direction = Direction.INPUT
        # Tracking sensors (循迹传感器): IO4--rightTracker, IO3--rightTracker
        self._leftTracker = DigitalInOut(board.IO4)
        self._leftTracker.direction = Direction.INPUT
        self._rightTracker = DigitalInOut(board.IO3)
        self._rightTracker.direction = Direction.INPUT
        # Motor (Right):  IO41--rightMotor1IN, IO42--rightMotor2IN
        self._rightMotor1IN = PWMOut(board.IO41, frequency=100, duty_cycle=0)
        self._rightMotor2IN = PWMOut(board.IO42, frequency=100, duty_cycle=0)        
        # Motor (Left):  IO12--leftMotor1IN, IO40--leftMotor2IN
        self._leftMotor1IN = PWMOut(board.IO12, frequency=100, duty_cycle=0)     
        self._leftMotor2IN = PWMOut(board.IO40, frequency=100, duty_cycle=0)

    # state of button A
    @property
    def button_A(self):
        """ to check the state of Button-A on the RunGo
        
        this example to check the state of Button-A 
        
        To use with the IoTs2:
        
        .. code-block:: python
            
            import time
            from hiibot_iots2_rungo import RunGo
            car = RunGo()
            while True:
                if car.button_A:
                    print('A be pressed')
                time.sleep(0.05)
        """
        if self._enbuttons:
            return not self._buttonA.value
        else:
            return False

    # state of button B
    @property
    def button_B(self):
        """ to check the state of Button-B on the RunGo
        
        this example to check the state of Button-B 
        
        To use with the IoTs2:
        
        .. code-block:: python
            
            import time
            from hiibot_iots2_rungo import RunGo
            car = RunGo()
            while True:
                if car.button_B:
                    print('B be pressed')
                time.sleep(0.05)
        """
        if self._enbuttons:
            return not self._buttonB.value
        else:
            return False

    def buttons_update(self):
        """ to update the state of Button-A, and Button-B on the RunGo
        
        this example to update the state of Button-A, and Button-B 
        
        To use with the IoTs2:
        
        .. code-block:: python
            
            from hiibot_iots2_rungo import RunGo
            car = RunGo()
            while True:
                car.buttons_update()
                if car.button_A_wasPressed:
                    print('A be pressed')
                if car.button_B_wasPressed:
                    print('B be pressed')
        """
        if self._enbuttons:
            self._db_buttonA.read()
            self._db_buttonB.read()
        else:
            pass

    @property
    def button_A_wasPressed(self):
        """ to check the state of Button-A on the RunGo
        
        this example to check the state of Button-A 
        
        To use with the IoTs2:
        
        .. code-block:: python
            
            from hiibot_iots2_rungo import RunGo
            car = RunGo()
            while True:
                car.buttons_update()
                if car.button_A_wasPressed:
                    print('A be pressed')
        """
        if self._enbuttons:
            return self._db_buttonA.wasPressed
        else:
            return False

    @property
    def button_A_wasReleased(self):
        """ to check the state of Button-A on the RunGo
        
        this example to check the state of Button-A 
        
        To use with the IoTs2:
        
        .. code-block:: python
            
            from hiibot_iots2_rungo import RunGo
            car = RunGo()
            while True:
                car.buttons_update()
                if car.button_A_wasReleased:
                    print('A be released')
        """
        if self._enbuttons:
            return self._db_buttonA.wasReleased
        else:
            return False

    def button_A_pressedFor(self, t_s):
        """ to check the state of Button-A on the RunGo
        
        this example to check the state of Button-A 
        
        To use with the IoTs2:
        
        .. code-block:: python
            
            from hiibot_iots2_rungo import RunGo
            car = RunGo()
            while True:
                car.buttons_update()
                if car.button_A_pressedFor(2.0):
                    print('A be preased longly over 2.0 second')
        """
        if self._enbuttons:
            return self._db_buttonA.pressedFor(t_s)
        else:
            return False

    @property
    def button_B_wasPressed(self):
        """ to check the state of Button-B on the RunGo
        
        this example to check the state of Button-B 
        
        To use with the IoTs2:
        
        .. code-block:: python
            
            from hiibot_iots2_rungo import RunGo
            car = RunGo()
            while True:
                car.buttons_update()
                if car.button_B_wasPressed:
                    print('B be pressed')
        """
        if self._enbuttons:
            return self._db_buttonB.wasPressed
        else:
            return False

    @property
    def button_B_wasReleased(self):
        """ to check the state of Button-B on the RunGo
        
        this example to check the state of Button-B 
        
        To use with the IoTs2:
        
        .. code-block:: python
            
            from hiibot_iots2_rungo import RunGo
            car = RunGo()
            while True:
                car.buttons_update()
                if car.button_B_wasReleased:
                    print('B be released')
        """
        if self._enbuttons:
            return self._db_buttonB.wasReleased
        else:
            return False

    def button_B_pressedFor(self, t_s):
        """ to check the state of Button-B on the RunGo
        
        this example to check the state of Button-B 
        
        To use with the IoTs2:
        
        .. code-block:: python
            
            from hiibot_iots2_rungo import RunGo
            car = RunGo()
            while True:
                car.buttons_update()
                if car.button_B_pressedFor(2.0):
                    print('B be preased longly over 2.0 second')
        """
        if self._enbuttons:
            return self._db_buttonB.pressedFor(t_s)
        else:
            return False

    @property
    def pixels(self):
        """ to control the pixels[0..2] on the bottom of RunGo
        
        this example to control the color of three RGB LEDs 
        
        To use with the IoTs2:
        
        .. code-block:: python
            
            import time
            from hiibot_iots2_rungo import RunGo
            car = RunGo()
            colors = [(255,0,0), (0,255,0), (0,0,255)]
            while True:
                for i in range(3):
                    car.pixels[i] = colors[i]
                car.pixels.show()
                # round colors
                tc = colors[0]
                colors[0] = colors[1]
                colors[1] = colors[2]
                colors[2] = tc
                time.sleep(0.5)
        """
        return self._pixels

    @property
    def pixelsColor(self):
        c = (self._colors[0], self._colors[1], self._colors[2])
        return c

    @pixelsColor.setter
    def pixelsColor(self, colors):
        ln = min(len(colors), 3)
        for i in range( ln ):
            self._pixels[i] = colors[i]
            self._colors[i] = colors[i]
        self._pixels.show()

    def pixelsRotation(self, dt=None):
        if not dt==None:
            self._pixelsRotationDt = dt
        et = time.monotonic()
        if (et-self._pixelsRotationSt)>=self._pixelsRotationDt:
            self._pixelsRotationSt = et
            tc = self._colors[0]
            self._colors[0] = self._colors[1]
            self._colors[1] = self._colors[2]
            self._colors[2] = tc
            for i in range(3):
                self._pixels[i] = self._colors[i]
            self._pixels.show()


    def motor(self, lspeed=50, rspeed=-50):
        """ Dual DC-Motor control interface to achieve forward, backward, turn left and turn right
        
        this example to demostrate car forward, backward, turn left and turn right
        
        To use with the IoTs2:
        
        .. code-block:: python
            
            import time
            from hiibot_iots2_rungo import RunGo
            car = RunGo()
            car.motor(50, 50)   # forward with 50 speed (max-speed: 255)
            time.sleep(1.2)     # runing time (1.2s)
            car.motor(-50, -50) # backward with 50 speed (max-speed: 255)
            time.sleep(1.2)     # runing time (1.2s)
            car.motor(-50, 50)  # turn left with car center
            time.sleep(2.0)     # runing time (2s)
            car.motor(50, -50)  # turn right with car center
            time.sleep(2.0)     # runing time (2s)
            car.stop()
            print("program done!")
        """
        lspeed = min(lspeed, 255)
        lspeed = max(-255, lspeed)
        ldir = 0x01 if lspeed<0 else 0x00  # 正反转: 0x00,CCW, 0x01,CW
        lspeed = abs(lspeed)
        lspeed = lspeed*255  # 0~65535
        rspeed = min(rspeed, 255)
        rspeed = max(-255, rspeed)
        rdir = 0x01 if rspeed<0 else 0x00  # 正反转: 0x00,CCW, 0x01,CW
        rspeed = abs(rspeed)
        rspeed = rspeed*255  # 0~65535
        if rdir==0x01:
            self._rightMotor2IN.duty_cycle = rspeed
            self._rightMotor1IN.duty_cycle = 0
        if rdir==0x0 :
            self._rightMotor1IN.duty_cycle = rspeed
            self._rightMotor2IN.duty_cycle = 0
        if ldir==0x01:
            self._leftMotor1IN.duty_cycle = lspeed
            self._leftMotor2IN.duty_cycle = 0
        if ldir==0x0 :
            self._leftMotor2IN.duty_cycle = lspeed
            self._leftMotor1IN.duty_cycle = 0


    def moveTime(self, mtdir=0, mtspeed=50, mt=2.0):
        """ Dual DC-Motor control interface to achieve forward, backward, turn left and turn right
        
        this example to demostrate car forward, backward, turn left and turn right
        
        To use with the IoTs2:
        
        .. code-block:: python
            
            import time
            from hiibot_iots2_rungo import RunGo
            car = RunGo()
            car.moveTime(0, 50, 1.2)   # forward with 50 speed, and running 1.2s
            car.moveTime(1, 50, 1.2)   # backward with 50 speed, and running 1.2s
            car.moveTime(2, 50, 2.0)   # turn left with car center, , and running 2.0s
            car.moveTime(3, 50, 2.0)   # turn right with car center, , and running 2.0s
            print("program done!")
        """
        if mtdir>=0 and mtdir<=3:
            self.move(mtdir, mtspeed)
            time.sleep(mt)
            self.motor(0,0)

    def move(self, mdir=0, mspeed=50):
        """ Dual DC-Motor control interface to car move(forward, backward, turn left and turn right)
        
        this example to demostrate car move 
        
        To use with the IoTs2:
        
        .. code-block:: python
            
            import time
            from hiibot_iots2_rungo import RunGo
            car = RunGo()
            car.move(0, 50)   # forward with 50 speed, and running 1.2s
            time.sleep(1.2)   # runing time (1.2s)
            car.move(1, 50)   # backward with 50 speed, and running 1.2s
            time.sleep(1.2)   # runing time (1.2s)
            car.move(2, 50)   # turn left with car center, , and running 2.0s
            time.sleep(2.0)   # runing time (2.0s)
            car.move(3, 50)   # turn right with car center, , and running 2.0s
            time.sleep(2.0)   # runing time (2.0s)
            car.stop()
            print("program done!")
        """
        sp = abs(mspeed)
        if mdir==0:    # Forward
            self.motor(sp, sp)
        elif mdir==1: # Backward
            self.motor(-sp, -sp)
        elif mdir==2: # Rotate-Left
            self.motor(-sp, sp)
        elif mdir==3: # Rotate-Right
            self.motor(sp, -sp)

    def stop(self):
        # stop car
        self.motor(0,0)

    @property
    def leftLightSensor(self):
        """ get the brightness value of the left-lighting-sensor
        
        this example to get the brightness of left lighting sensor 
        
        To use with the IoTs2:
        
        .. code-block:: python
            
            import time
            from hiibot_iots2_rungo import RunGo
            car = RunGo()
            while True:
                print(car.leftLightSensor)
                time.sleep(0.5)
        """
        return self._leftLightSensor.value
    
    @property
    def rightLightSensor(self):
        """ get the brightness value of the right-lighting-sensor
        
        this example to get the brightness of right lighting sensor 
        
        To use with the IoTs2:
        
        .. code-block:: python
            
            import time
            from hiibot_iots2_rungo import RunGo
            car = RunGo()
            while True:
                print(car.rightLightSensor)
                time.sleep(0.5)
        """
        return self._rightLightSensor.value
    
    def _getRawRGB_light(self):
        __colorComps = ( (255,0,0), (0,255,0), (0,0,255) )
        __bt = self._pixels.brightness
        self._pixels.brightness = 1.0
        self._pixels.fill(0x0)
        self._pixels.show()
        __Craw = [0,0,0]
        i=0
        for cc in __colorComps:
            self.pixels[0] = cc
            self.pixels.show()
            time.sleep(0.1)
            __Craw[i] = int(self._colorSensor.value * 255 // (2 ** 16))
            i += 1
            self._pixels.fill(0x0)
            self._pixels.show()
            time.sleep(0.1)
        self._pixels.brightness = __bt
        return __Craw[0], __Craw[1], __Craw[2]

    @staticmethod
    def _rgb2hsv(r, g, b):
        __rR, __rG, __rB = r/255, g/255, b/255
        __Cmax, __Cmin = max(__rR, __rG, __rB), min(__rR, __rG, __rB)
        __Cdelta = __Cmax - __Cmin
        V = __Cmax   # HSV: Value
        if __Cmax == 0.0:
            S = 0.0  # HSV: Saturation
        else:
            S = __Cdelta/__Cmax # HSV: Saturation
        if __Cdelta==0.0:
            H = 0    # HSV: Hue
        elif __Cmax==__rR:
            H = 60*(((__rG - __rB)/__Cdelta)%6)  # HSV: Hue [--Red++]
        elif __Cmax==__rG:
            H = 60*(((__rB - __rR)/__Cdelta)+2)  # HSV: Hue [--Green++]
        else:
            H = 60*(((__rR - __rG)/__Cdelta)+4)  # HSV: Hue [--Blue++]
        H = int(H)
        return H, S, V

    @property
    def groundColorID(self):
        rawR, rawG, rawB = self._getRawRGB_light()
        H, S, V = self._rgb2hsv(rawR, rawG, rawB)
        if S<0.075:
            return 0 # white
        if H<30 or H>=330:     # 330~359, 0~29
            return 1 # red
        elif H>=30 and H<90:   # 30~89
            return 2 # yellow
        elif H>=90 and H<150:  # 90~149
            return 3 # green
        elif H>=150 and H<210: # 150~209
            return 4 # cyan
        elif H>=210 and H<270: # 210~269
            return 5 # blue
        else:                  # 270~329
            return 6 # purple

    @property
    def groundColor(self):
        return self.groundColor_name[ self.groundColorID ]

    @property
    def groundColorValue(self):
        return self.groundColor_list[ self.groundColorID ]

    @property
    def leftHeadLED(self):
        """ get the status value of the left-head-led
        
        this example to get the state of left head LED 
        
        To use with the IoTs2:
        
        .. code-block:: python
            
            import time
            from hiibot_iots2_rungo import RunGo
            car = RunGo()
            while True:
                car.leftHeadLED = not car.leftHeadLED
                time.sleep(0.5)
        """
        return self._leftHeadLED.value
    
    @leftHeadLED.setter
    def leftHeadLED(self, value):
        """ to control the left-head-led on or off
        
        this example to control the state of left head LED 
        
        To use with the IoTs2:
        
        .. code-block:: python
            
            import time
            from hiibot_iots2_rungo import RunGo
            car = RunGo()
            while True:
                car.leftHeadLED = not car.leftHeadLED
                time.sleep(0.5)
        """
        self._leftHeadLED.value = value

    @property
    def rightHeadLED(self):
        """ get the status value of the right-head-led
        
        this example to get the state of right head LED 
        
        To use with the IoTs2:
        
        .. code-block:: python
            
            import time
            from hiibot_iots2_rungo import RunGo
            car = RunGo()
            while True:
                car.rightHeadLED = not car.rightHeadLED
                time.sleep(0.5)
        """
        return self._rightHeadLED.value
    
    @rightHeadLED.setter
    def rightHeadLED(self, value):
        """ to control the right-head-led on or off
        
        this example to control the state of right head LED 
        
        To use with the IoTs2:
        
        .. code-block:: python
            
            import time
            from hiibot_iots2_rungo import RunGo
            car = RunGo()
            while True:
                car.rightHeadLED = not car.rightHeadLED
                time.sleep(0.5)
        """
        self._rightHeadLED.value = value

    @property
    def distance(self):
        """Return the distance measured by the sensor in cm.
        
        This is the function that will be called most often in user code. The
        distance is calculated by timing a pulse from the sensor, indicating
        how long between when the sensor sent out an ultrasonic signal and when
        it bounced back and was received again.
        
        If no signal is received, we'll throw a RuntimeError exception. This means
        either the sensor was moving too fast to be pointing in the right
        direction to pick up the ultrasonic signal when it bounced back (less
        likely), or the object off of which the signal bounced is too far away
        for the sensor to handle. In my experience, the sensor can detect
        objects over 460 cm away.
        
        :return: Distance in centimeters.
        :rtype: float
        this example to control the state of right head LED 
        
        To use with the IoTs2:
        
        .. code-block:: python
            
            import time
            from hiibot_iots2_rungo import RunGo
            car = RunGo()
            while True:
                print(car.distance)
                time.sleep(0.5)
        """
        return self._dist_two_wire()  # at this time we only support 2-wire meausre

    def _dist_two_wire(self):
        if _USE_PULSEIO:
            self._echo.clear()  # Discard any previous pulse values
        self._trig.value = True  # Set trig high
        time.sleep(0.00001)  # 10 micro seconds 10/1000/1000
        self._trig.value = False  # Set trig low
        pulselen = 65535
        ok_echo=True
        timestamp = time.monotonic()
        if _USE_PULSEIO:
            self._echo.resume()
            while not self._echo:
                # Wait for a pulse
                if (time.monotonic() - timestamp) > self._timeout:
                    self._echo.pause()
                    ok_echo = False
                    break  # output a error result vs stop running
                    #raise RuntimeError("Timed out")
            self._echo.pause()
            if ok_echo:
                pulselen = self._echo[0]
        else:
            # OK no hardware pulse support, we'll just do it by hand!
            # hang out while the pin is low
            while not self._echo.value:
                if time.monotonic() - timestamp > self._timeout:
                    break
                    #raise RuntimeError("Timed out")
            timestamp = time.monotonic()
            # track how long pin is high
            while self._echo.value:
                if time.monotonic() - timestamp > self._timeout:
                    break
                    #raise RuntimeError("Timed out")
            pulselen = time.monotonic() - timestamp
            pulselen *= 1000000  # convert to us to match pulseio
        if pulselen >= 65535:
            ok_echo = False
            #raise RuntimeError("Timed out")
        
        # positive pulse time, in seconds, times 340 meters/sec, then
        # divided by 2 gives meters. Multiply by 100 for cm
        # 1/1000000 s/us * 340 m/s * 100 cm/m * 2 = 0.017
        return pulselen * 0.017 

    @property
    def leftTracker(self):
        """
        return l sensor status: True/1, no-reflected signal, maybe just above the black line
                                False/0, the state of the reflected signal
        """
        return self._leftTracker.value

    @property
    def rightTracker(self):
        """
        return r sensor status: True/1, no-reflected signal, maybe just above the black line
                                False/0, the state of the reflected signal
        """
        return self._rightTracker.value

    def tracking(self, lr_mode=0):
        """
        lr_mode: 0, the width of back-line greater than the width between the l and r sensors 
                 3, the width of white-line greater than the width between the l and r sensors
                 1, a barrow back-line be used, and l sensor be used to track
                 2, a barrow back-line be used, and r sensor be used to track
        """
        if lr_mode==0:
            return self._leftTracker.value and self._rightTracker.value
        elif lr_mode==1:
            return self._leftTracker.value and not self._rightTracker.value
        elif lr_mode==2:
            return not self._leftTracker.value and self._rightTracker.value
        elif lr_mode==3:
            return not self._leftTracker.value and not self._rightTracker.value
        else:
            return False

    def trackSide(self, side=0, lr_mode=1):
        if side==0 and lr_mode==0:
            return self._leftTracker.value
        elif side==0 and lr_mode==1:
            return not self._leftTracker.value
        elif side==1 and lr_mode==0:
            return not self._rightTracker.value
        elif side==1 and lr_mode==1:
            return self._rightTracker.value
        else:
            return False
