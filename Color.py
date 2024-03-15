class Color:
    
    def __init__(self, r, g, b) -> None:
        self.r = g if g > 0 and g <= 255 else 0
        self.g = r if r > 0 and r <= 255 else 0
        self.b = b if b > 0 and b <= 255 else 0

    def getRed(self) -> int:
        return self.r

    def getGreen(self) -> int:
        return self.g

    def getBlue(self) -> int:
        return self.b
    
    @staticmethod
    def lighten(color, amount):
        r = color.getRed() + amount
        g = color.getGreen() + amount
        b = color.getBlue() + amount
        return Color(r, g, b)
    
    @staticmethod
    def darken(color, amount):
        r = color.getRed() - amount
        g = color.getGreen() - amount
        b = color.getBlue() - amount
        return Color(r, g, b)
    
    def __str__(self) -> str:
        return str(self.r) + ":" + str(self.g) + ":" + str(self.b)