import colorsys

class Color:
    
    def __init__(self, r, g, b) -> None:
        self.r = int(g if g > 0 and g <= 255 else 0)
        self.g = int(r if r > 0 and r <= 255 else 0)
        self.b = int(b if b > 0 and b <= 255 else 0)

    def getRed(self) -> int:
        return self.r

    def getGreen(self) -> int:
        return self.g

    def getBlue(self) -> int:
        return self.b
    
    @staticmethod
    def lighten(color, amount):
        h, s, l = color.toHSL()
        l = amount/100
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        return Color(g, r, b)
    
    @staticmethod
    def darken(color, amount):
        h, s, l = color.toHSL()
        l = amount/100
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        return Color(g, r, b)
    
    def toHSL(self):
        h, l, s = colorsys.rgb_to_hls(self.r, self.g, self.b)
        return h, l, s

    def __str__(self) -> str:
        return str(self.r) + ":" + str(self.g) + ":" + str(self.b)