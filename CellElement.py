from Color import Color
from Element import Element

class CellElement:

    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.block = False

    def getColor(self) -> Color:
        return self.color

    def getX(self) -> int:
        return self.x

    def getY(self) -> int:
        return self.y
    
    def isBlock(self) -> bool:
        return self.block
    
    def setBlock(self, data: int, element: Element):
        if(data == 0):return
        self.color = element.getColor()
        self.block = True
    
    def setData(self, color, block):
        self.color = color
        self.block = block

    def clearBlock(self):
        self.block = False
        self.color = Color(0, 0, 0)
    
    def copyTo(self, other):
        if(not self.block):other.clearBlock()
        else: other.setData(self.getColor(), self.isBlock())
    
    def __str__(self) -> str:
        return str("█" if self.block else ".")#str(self.block)