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
        self.strip = PixelStrip(LedMatrix.LED_COUNT, LedMatrix.LED_PIN, LedMatrix.LED_FREQ_HZ, LedMatrix.LED_DMA, LedMatrix.LED_INVERT, LedMatrix.LED_BRIGHTNESS, LedMatrix.LED_CHANNEL)
        self.strip.begin()

    def getPin(self):
        return self.pin

    def clear(self):
        for i in range(0, self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(0, 0, 0))
        self.strip.show()
    
    def setColorAtPixel(self, color: LogicColor, x: int, y: int):
        width = LedMatrix.WIDTH
        height = LedMatrix.HEIGHT

        i = 0

        if y % 2 == 0:
            i = x + y*width
        else:
            i = (width - x) + y*width

        if(i >= self.strip.numPixels()):return

        self.strip.setPixelColor(i, Color(color.getRed(), color.getGreen(), color.getBlue()))

    def show(self):
        self.strip.show()
         
    WIDTH = 10
    HEIGHT = 15