from rpi_ws281x import PixelStrip, Color
from Color import Color as LogicColor

class LedMatrix:

    LED_COUNT = 10*15     # Number of LED pixels.
    LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
    # LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
    LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA = 10          # DMA channel to use for generating signal (try 10)
    LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
    LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
    LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53 // 10*15, 10, 800000, pin, False, 255, 0

    def __init__(self, pin):
        self.pin = pin
        self.strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        self.strip.begin()

    def getPin(self):
        return self.pin

    def clear(self):
        for i in range(0, self.strip.numPixels()):
            self.setPixelColor(i, Color(0, 0, 0))
        self.strip.show()
    
    def setColorAtPixel(self, color: LogicColor, x: int, y: int):
        i = y*LedMatrix.WIDTH

        if(y%2 == 0):
            i += x
        else:
            i += (15 - x)

        if(i >= self.strip.numPixels()):return

        self.strip.setPixelColor(i, Color(color.getRed(), color.getGreen(), color.getBlue()))

    def show(self):
        self.strip.show()
         
    WIDTH = 15
    HEIGHT = 10