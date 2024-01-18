from Color import Color
import copy

class Element:

    def __init__(self, elementData, placeMethod, color):
        self.elementData = elementData
        self.x = Element.ELEMENT_SPAWN_X
        self.y = Element.ELEMENT_SPAWN_Y
        self.placeMethod = placeMethod
        self.color = color
    
    def rotateLeft(self):
        self.elementData = [list(row) for row in zip(*self.elementData[::-1])]

    def getColor(self) -> Color:
        return self.color

    def rotateRight(self):
        rows = len(self.elementData)
        cols = len(self.elementData[0])

        tmpArray2 = [[0] * rows for _ in range(cols)]

        for y in range(cols-1, -1, -1):
            for x in range(rows):
                tmpArray2[y][x] = self.elementData[x][3-y]

        self.elementData = tmpArray2


    def moveDown(self, matrix):
        self.y += 1
        if(self.checkForBlockCollision(matrix)):
            self.y -= 1
            self.placeMethod(self)
        pass

    def moveRight(self, matrix):
        self.x += 1
        if(self.checkForWallCollision(matrix)):
            self.x -= 1

    def moveLeft(self, matrix):
        self.x -= 1
        if(self.checkForWallCollision(matrix)):
            self.x += 1

    def checkForWallCollision(self, matrix):
        left = self.getOffsetLeft()
        right = self.getOffsetRight()

        print(str(left) + ":" + str(right))

        x = self.x
        y = self.y
        data = self.elementData
        posX1 = x + right
        posX2 = x + (3 - left)

        print(str(posX1) + ":" + str(posX2))

        isWallCollision = (
                posX1 < 0 or posX1 >= len(matrix) 
                    or
                posX2 < 0 or posX2 >= len(matrix)
            )
        
        if(isWallCollision):return True
        
        for xx in range(0, len(data)):
            for yy in range(0, len(data[0])):
                if(data[xx][yy] == 0):continue
                if(matrix[xx + x][yy + y].isBlock()):
                    return True
        

        return False

    def checkForBlockCollision(self, matrix):
        #Collision for the end of the box
        offsetOfFirstElement = self.getOffsetBottom()
        if(self.y - (offsetOfFirstElement - 3) >= len(matrix[0])):
            return True
        
        xOffset = self.x
        yOffset = self.y
        data = self.elementData

        #Coliision for other elements
        for x in range(0, len(data)):
            for y in range(0, len(data[0])):
                if(data[x][y] == 0):continue
                if(matrix[x + xOffset][y + yOffset].isBlock()):
                    return True

        return False

    def getOffsetLeft(self) -> int:
        data = self.elementData
        pos = 0
        for x in range(len(data)-1, -1, -1):
            for y in range(len(data[0])):
                if data[x][y] == 1:
                    return pos
            pos += 1

    def getOffsetRight(self) -> int:
        data = self.elementData
        pos = 0
        for x in range(len(data)):
            for y in range(len(data[0])):
                if data[x][y] == 1:
                    return pos
            pos += 1

    def getOffsetBottom(self) -> int:
        data = self.elementData
        pos = 0
        for y in range(len(data[0])-1, -1, -1):
            for x in range(len(data)):
                if data[x][y] == 1:
                    return pos
            pos += 1

    def getOffsetTop(self) -> int:
        data = self.elementData
        pos = 0
        for y in range(len(data[0])):
            for x in range(len(data)):
                if data[x][y] == 1:
                    return pos
            pos += 1

    def getX(self):
        return self.x

    def getY(self) -> int:
        return self.y
    
    def getElementData(self):
        return self.elementData

    def __str__(self) -> str:
        result = ""
        for x in range(0, len(self.elementData)):
            result += "["
            for y in range(0, len(self.elementData[0])):
                result += str(self.elementData[x][y]) + ", "
            result = result[:-2]  # Korrigiere diese Zeile
            result += "]\n"
        return result
    
    def clone(self):
        return Element(copy.deepcopy(self.elementData), self.placeMethod, copy.copy(self.color))

    ELEMENT_SPAWN_X = 0
    ELEMENT_SPAWN_Y = 0