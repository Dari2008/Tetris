class Color:
    
    def __init__(self, r, g, b) -> None:
        self.r = g
        self.g = r
        self.b = b

    def getRed(self) -> int:
        return self.r

    def getGreen(self) -> int:
        return self.g

    def getBlue(self) -> int:
        return self.b
    
    def __str__(self) -> str:
        return str(self.r) + ":" + str(self.g) + ":" + str(self.b)