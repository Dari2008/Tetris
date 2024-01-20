from rpi_ws281x import PixelStrip
from rpi_ws281x import Color as PixelColor
from Color import Color as Color

class LedMatrix:

    def __init__(self, pin):
        self.pin = pin
        self.strip = PixelStrip(10*15, 10, 800000, pin, False, 255, 0)
        self.strip.begin()

    def getPin(self):
        return self.pin
    
    def setColorAtPixel(self, color: Color, x: int, y: int):
        i = y*LedMatrix.WIDTH

        if(y%2 == 0):
            i += x
        else:
            i += (15 - x)

        if(i >= self.strip.numPixels()):return

        self.strip.setPixelColor(i, PixelColor(color.getRed(), color.getGreen(), color.getBlue()))

         
    WIDTH = 15
    HEIGHT = 10