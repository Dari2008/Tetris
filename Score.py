import datetime
import os
import atexit

class Score:
    
    def __init__(self, startScore=0, user="", gameDataFile="./gameData/", logFile="./gameData/highScoreRecord.score", highScoreFile="./gameData/highScore.score"):
        self.score = startScore
        self.user = user
        self.logFile = logFile
        self.highScoreFile = highScoreFile
        self.highScore = 0
        if(not os.path.exists(gameDataFile)):os.mkdir(gameDataFile)
        if(not os.path.exists(highScoreFile)):
            with open(self.highScoreFile, "w+") as file:
                pass

        with open(self.highScoreFile, "r+") as file:
                red = file.read()
                self.highScore = int("0" if red == "" else red)
        self.initAtExit()

    def rowFull(self):
        self.score += Score.ROW_FULL_POINTS
        
    def elementPlaced(self):
        self.score += Score.ELEMENT_PLACED_POINTS

    def multipleLineFull(self, rows):
        self.score += (Score.ROW_FULL_POINTS * rows + Score.ROW_FULL_POINTS * rows)

    def initAtExit(self):
        atexit.register(self.checkForNewHighScore)

    def checkForNewHighScore(self):
        if(self.score > self.highScore):
            self.log("New High Score: " + str(self.score))
            self.saveHighScore()
        elif (self.score == self.highScore):
            self.log("Same High Score: " + str(self.score))
        

    def saveHighScore(self):
        with open(self.highScoreFile, "w+") as file:
            file.write(str(self.score))

    def log(self, data, withTimeStamp=True):
        with open(self.logFile, "a+") as file:
            if(withTimeStamp):
                timeStamp = datetime.datetime.now().strftime("[%d.%m.%Y - %H:%M]")
                file.write(timeStamp + ": " + data + "\n")
            else:
                file.write(data + "\n")

    def getMultiplier(self) -> float:
        capped_score = max(0, min(self.score, 1000))
        min_speed = 0.1
        capped_score += min_speed
        
        multiplier = 1 - capped_score / 1000
        
        return max(0, multiplier)



    ELEMENT_PLACED_POINTS = 1
    ROW_FULL_POINTS = 10