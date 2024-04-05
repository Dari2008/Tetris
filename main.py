from Element import Element
from Color import Color
from CellElement import CellElement
from Score import Score
from LedMatrix import LedMatrix
from time import sleep
import glob
import random
import keyboard

class Main:
        
    ELEMENTS = []
    SPACE_AT_TOP_THAT_MUST_BE_FREE = 3

    def __init__(self) -> None:
        
        self.loadAllElements()
        self.newElementBag()

        self.matrix = []
        self.lost = False
        self.score = Score()
        self.ledMatrix = LedMatrix(18)
        self.ledMatrix.clear()

        self.currentElement: Element = None
        self.tmpElement: Element = self.currentElement

        for x in range(10):
            tmp = []
            for y in range(15):
                tmp.append(CellElement(Color(0, 0, 0), x, y))
            self.matrix.append(tmp)

        self.newRandomElement()

        self.initMovement()

        while True:
            sleep(1*self.score.getMultiplier())
            if(self.lost):break
            self.updateGameFrame()

    def newElementBag(self):
        print("new Bag created:")
        self.currentElementBag = Main.ELEMENTS.copy()

        for element in Main.ELEMENTS.copy():
            self.currentElementBag.append(element)

    def updateGameFrame(self, onlyControllNoMoveDown=False):
        if(self.lost): return
        if(self.currentElement != None and not onlyControllNoMoveDown):
            self.currentElement.moveDown(self.matrix)
        self.lost = self.lost or self.checkForLoose()

        if(self.lost):
            for x in range(0, len(self.matrix)):
                for y in range(0, len(self.matrix[0])):
                    if(self.score.isNewHighscore()):
                        self.ledMatrix.setColorAtPixel(Color(0, 255, 0), x, y)
                    else:
                        self.ledMatrix.setColorAtPixel(Color(255, 0, 0), x, y)
            self.ledMatrix.show()
            self.printMatrix()
            return
        
        self.printMatrix()
        self.updateMatrix()

    def updateMatrix(self):
        # pass

        dataOfElement = self.currentElement.getElementData()
        xOfElement = self.currentElement.getX()
        yOfElement = self.currentElement.getY()


        self.tmpElement.setElementData(self.currentElement.getElementData())
        self.tmpElement.setX(self.currentElement.getX())
        self.tmpElement.setY(self.currentElement.getY())
        tmpElementData = self.tmpElement.getElementData()
        self.tmpElement.moveDownCompletly(self.matrix, True)
        xOfTmpElement = self.tmpElement.getX()
        yOfTmpElement = self.tmpElement.getY()


        for y in range(0, len(self.matrix[0])):
            for x in range(0, len(self.matrix)):
                print(x, y)
                if xOfElement <= x and xOfElement >= x and yOfElement <= y and yOfElement >= y:
                    if(dataOfElement[x-xOfElement][y-yOfElement] == 1):
                        self.ledMatrix.setColorAtPixel(self.currentElement.getColor(), x, y)
                    else:
                        self.ledMatrix.setColorAtPixel(self.matrix[x][y].getColor(), x, y)
                elif xOfTmpElement <= x and xOfTmpElement >= x and yOfTmpElement <= y and yOfTmpElement >= y:
                    if(tmpElementData[x-xOfTmpElement][y-yOfTmpElement] == 1):
                        self.ledMatrix.setColorAtPixel(self.tmpElement.getColor(), x, y)
                    else:
                        self.ledMatrix.setColorAtPixel(self.matrix[x][y].getColor(), x, y)
                else:
                    self.ledMatrix.setColorAtPixel(self.matrix[x][y].getColor(), x, y)
        self.ledMatrix.show()

    def checkForFullLines(self):
        fullLines = 0
        for y in range(0, len(self.matrix[0])):
            blocks = 0
            for x in range(0, len(self.matrix)):
                if(self.matrix[x][y].isBlock()):
                    blocks += 1
            if(blocks == len(self.matrix)):
                self.removeRowAndMoveOthersDown(y)
                fullLines += 1
                
        if(fullLines==1):self.score.rowFull()
        elif(fullLines > 1):self.score.multipleLineFull(fullLines)
        


    def removeRowAndMoveOthersDown(self, row):

        for x in range(0, len(self.matrix)):
            self.matrix[x][row].clearBlock()

        for x in range(0, len(self.matrix)):
            for y in range(row, -1, -1):
                if(y == 0):
                    self.matrix[x][y].clearBlock()
                else:
                    if(y-1 < 0):
                        self.matrix[x][y].clearBlock()
                    else:
                        self.matrix[x][y-1].copyTo(self.matrix[x][y])
                

        


    def checkForLoose(self) -> bool:
        for x in range(0, len(self.matrix)):
            for y in range(0, Main.SPACE_AT_TOP_THAT_MUST_BE_FREE):
                if(self.matrix[x][y].isBlock()):
                    return True
        return False

    def placeElement(self, element: Element):
        xOffset = element.getX()
        yOffset = element.getY()
        offsetOfFirstElement = element.getOffsetBottom()
        data = element.getElementData()

        self.score.elementPlaced()

        for x in range(0, len(data)):
            for y in range(0, len(data[0])):
                if((x + xOffset) >= len(self.matrix)):continue
                if((y + yOffset - offsetOfFirstElement) >= len(self.matrix[0])):continue
                if((y + yOffset) >= len(self.matrix[0])):continue
                if(data[x][y] == 0):continue

                self.matrix[x + xOffset][y + yOffset].setBlock(data[x][y], element)
        self.newRandomElement()

        self.checkForFullLines()


    def printMatrix(self, showCurrentElement=True):
        return
        spacer = ""
        result = ""
        dataOfElement = self.currentElement.getElementData()
        xOfElement = self.currentElement.getX()
        yOfElement = self.currentElement.getY()

        for y in range(0, len(self.matrix[0])):
            result += "["
            for x in range(0, len(self.matrix)):
                if(showCurrentElement and self.currentElement != None):

                    if(xOfElement <= x <= xOfElement + len(dataOfElement) - 1 and yOfElement <= y <= yOfElement + len(dataOfElement[0]) - 1):
                        for xx in range(0, len(dataOfElement)):
                            for yy in range(0, len(dataOfElement[0])):
                                    if(x == xOfElement + xx and y == yOfElement + yy):
                                        if(dataOfElement[xx][yy] == 1):
                                            result += str("█") + spacer#self.currentElement.getColor()
                                            continue
                                        else:
                                            result += str(self.matrix[x][y]) + spacer
                    else:
                        result += str(self.matrix[x][y]) + spacer
                else:
                    result += str(self.matrix[x][y]) + spacer
            if(len(spacer) != 0):
                result = result[:-len(spacer)]
            result += "]\n"
        print(result)

    def loadElement(self, path) -> Element:
        with open(path, "r") as file:
            content = file.readlines()
            if(len(content) != 5):return None
            colorLine = content.pop(0)
            elementLine1 = content.pop(0)
            elementLine2 = content.pop(0)
            elementLine3 = content.pop(0)
            elementLine4 = content.pop(0)

            if(len(colorLine.split(";")) != 3):return None
            if(len(elementLine1.split(",")) != 4):return None
            if(len(elementLine2.split(",")) != 4):return None
            if(len(elementLine3.split(",")) != 4):return None
            if(len(elementLine4.split(",")) != 4):return None

            color = Color(
                    int(colorLine.split(";")[0]), 
                    int(colorLine.split(";")[1]), 
                    int(colorLine.split(";")[2])
                )
             
            element = Element([
                [int(elementLine1.split(",")[0]), int(elementLine2.split(",")[0]), int(elementLine3.split(",")[0]), int(elementLine4.split(",")[0])],
                [int(elementLine1.split(",")[1]), int(elementLine2.split(",")[1]), int(elementLine3.split(",")[1]), int(elementLine4.split(",")[1])],
                [int(elementLine1.split(",")[2]), int(elementLine2.split(",")[2]), int(elementLine3.split(",")[2]), int(elementLine4.split(",")[2])],
                [int(elementLine1.split(",")[3]), int(elementLine2.split(",")[3]), int(elementLine3.split(",")[3]), int(elementLine4.split(",")[3])]
            ], self.placeElement, color)
            return element
        
    def newRandomElement(self):
        if(len(self.currentElementBag) == 0):
            self.newElementBag()
        num = random.randint(0, len(self.ELEMENTS)-1)
        self.currentElement = self.currentElementBag[num].clone()
        self.currentElementBag.remove(self.currentElementBag[num])
        self.tmpElement = self.currentElement.clone()


    def loadAllElements(self):
        path = "./elements/*.element"
        for file in glob.glob(path):
            element = self.loadElement(file)
            if(element == None):continue
            Main.ELEMENTS.append(element)

    def initMovement(self):
        def onRotateLeft():
            self.currentElement.rotateLeft(self.matrix)
            self.updateGameFrame(onlyControllNoMoveDown=True)

        def onRotateRight():
            self.currentElement.rotateRight(self.matrix)
            self.updateGameFrame(onlyControllNoMoveDown=True)

        def onMoveLeft():
            self.currentElement.moveLeft(self.matrix)
            self.updateGameFrame(onlyControllNoMoveDown=True)

        def onMoveRight():
            self.currentElement.moveRight(self.matrix)
            self.updateGameFrame(onlyControllNoMoveDown=True)

        def onMoveDown():
            self.currentElement.moveDown(self.matrix)
            self.updateGameFrame(onlyControllNoMoveDown=True)

        def onMoveCopletlyDown():
            self.currentElement.moveDownCompletly(self.matrix)
            self.updateGameFrame(onlyControllNoMoveDown=True)

        keyboard.add_hotkey('a', onRotateRight)
        keyboard.add_hotkey('d', onRotateLeft)
        keyboard.add_hotkey('left', onMoveLeft)
        keyboard.add_hotkey('right', onMoveRight)
        keyboard.add_hotkey('down', onMoveDown)
        keyboard.add_hotkey('space', onMoveCopletlyDown)


if __name__ == "__main__":
    print("Starting...")
    Main()