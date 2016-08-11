"""
Assignment 7: GUI Game
"""

from __future__ import division
try:
  from tkinter import *
except:
  from Tkinter import *
from random import randint
from time import sleep

class Game(object):
  def __init__(self):
    self.root = Tk()
    self.root.wm_title("Laser Pong")
    self.NewGame()
    self.root.bind("<Key>", self.Input)
    self.root.bind("<KeyRelease>", self.InputRelease)
    self.root.mainloop()

  def NewGame(self, e = None):
    self.goals = 0
    self.boxesDestroyed = 0
    self.AI = 10
    self.timeScore = 0
    self.pointScore = 0
    self.lives = 3
    self.pause = False
    self.pauseTimer = 2
    self.gameCanvas = Canvas(self.root, width=800, height=600, bg="white")
    self.Reset()
    self.gameCanvas.grid(row=0,column=0)
    self.root.after(20, self.GameLoop)
    self.root.after(1000, self.Timer)

  def Reset(self):
    self.timeLeftToDestroy = 60
    self.timeTracker = 0
    self.boxes = []
    self.boxHP = []
    self.inputChar = ""
    self.xPos = 30
    self.gunXPos = 30
    self.yPos = 300
    self.xPos2 = 770
    self.yPos2 = 300
    self.xPos3 = 400
    self.yPos3 = 300
    self.randSpeedVals = [4,7]
    self.xSpeed = randint(self.randSpeedVals[0], self.randSpeedVals[1])
    self.ySpeed = randint(-8, 8)
    self.AITestTimer = 0
    self.AIPassOrFail = randint(1, self.AI)
    self.gunExtend = False
    self.gunRetract = True
    self.gunMode = False
    self.bullets = []
    self.bulletXPos = []
    self.bulletYPos = []
    self.canFire = True
    self.powerUp = 0
    self.powerShot = 0
    self.powerXPos = 0
    self.powerYPos = 0
    self.firedPower = False
    self.powerTimer = 3
    self.nurfTimer = 3
    self.power1 = False
    self.power2 = False
    self.power3 = False
    self.power4 = False
    self.power5 = False
    self.leftPaddleSpeed = 10
    self.rightPaddleSpeed = 10
    self.gameCanvas.delete(ALL)
    self.ball = self.gameCanvas.create_oval(self.xPos3-15,self.yPos3-15,\
      self.xPos3+15,self.yPos3+15,fill='grey',outline='black',width=5)
    self.gun = self.gameCanvas.create_rectangle(self.gunXPos-15,\
      self.yPos-5,self.gunXPos+15,self.yPos+5,fill='grey',\
      outline='red',width=5)
    self.leftPaddle = self.gameCanvas.create_rectangle(self.xPos-15,\
      self.yPos-50,self.xPos+15,self.yPos+50,fill='black',\
      outline='red',width=5)
    self.rightPaddle = self.gameCanvas.create_rectangle(self.xPos2-15,\
      self.yPos2-50,self.xPos2+15,self.yPos2+50,fill='black',\
      outline='blue',width=5)
    self.scoreTime = self.gameCanvas.create_text(10,5,anchor=NW,text = \
      "Time: " + str(self.timeScore))
    self.scorePoints = self.gameCanvas.create_text(10,20,anchor=NW,text = \
      "Points: " + str(self.pointScore))
    self.livesText = self.gameCanvas.create_text(10,35,anchor=NW,text = \
      "Lives: " + str(self.lives))
    self.timeDestroy = self.gameCanvas.create_text(790, 10, anchor=NE, text=\
      "Time left to destroy a box: " + str(self.timeLeftToDestroy), font \
      = ("Comic Sans", 12))

  def Input(self, e):
    if self.power5 == True:
      if str(e.char) == "w":
        self.inputChar = "s"
      elif str(e.char) == "s":
        self.inputChar = "w"
      else:
        self.inputChar =  str(e.char)
    else:
      self.inputChar =  str(e.char)

  def InputRelease(self, e):
    self.inputChar =  ""
    self.canFire = True

  def Timer(self):
    self.rectX = randint(200, 500)
    self.rectY = randint(0, 525)
    if self.AITestTimer < 1:
      self.AITestTimer += 1
    else:
      self.AITestTimer = 0
      self.AIPassOrFail = randint(1, self.AI)
    if self.timeTracker < 15:
      self.timeTracker += 1
    else:
      self.timeTracker = 0
      self.randSpeedVals[0] += 1
      self.randSpeedVals[1] += 1
      self.AI += 2
    if (self.timeTracker%3) == 0 and len(self.boxes) < 10:
      self.boxes.append(self.gameCanvas.create_rectangle(self.rectX, self.rectY, \
        randint(self.rectX + 20, self.rectX +100), randint(self.rectY + \
        20, self.rectY + 100), fill='black'))
      self.boxHP.append(10)
    elif (self.timeTracker%3) == 0 and len(self.boxes) >= 10:
      self.gameCanvas.delete(self.boxes[0])
      del self.boxes[0]
      self.boxes.append(self.gameCanvas.create_rectangle(self.rectX, self.rectY, \
        randint(self.rectX + 20, self.rectX +100), randint(self.rectY + \
        20, self.rectY + 100), fill='black'))
      self.boxHP.append(10)
    if self.power1 == True and self.powerTimer > 0:
      self.gameCanvas.itemconfig(self.rightPaddle, outline = 'yellow')
      self.rightPaddleSpeed = 3
      self.powerTimer -= 1
    elif self.power2 == True and self.powerTimer > 0:
      self.gameCanvas.itemconfig(self.rightPaddle, outline = 'orange')
      self.rightPaddleSpeed = 0
      self.powerTimer -= 1
    elif self.powerTimer == 0:
      self.power1 = False
      self.power2 = False
      self.rightPaddleSpeed = 10
      self.gameCanvas.itemconfig(self.rightPaddle, outline = 'blue')
    if self.power3 == True and self.nurfTimer > 0:
      self.gameCanvas.itemconfig(self.leftPaddle, outline = 'yellow')
      self.leftPaddleSpeed = 4
      self.nurfTimer -= 1
    elif self.power4 == True and self.nurfTimer > 0:
      self.gameCanvas.itemconfig(self.leftPaddle, outline = 'orange')
      self.leftPaddleSpeed = 0
      self.nurfTimer -= 1
    elif self.power5 == True and self.nurfTimer > 0:
      self.gameCanvas.itemconfig(self.leftPaddle, outline = 'green')
      self.nurfTimer -= 1
    elif self.nurfTimer == 0:
      self.power3 = False
      self.power4 = False
      self.power5 = False
      self.leftPaddleSpeed = 10
      self.gameCanvas.itemconfig(self.leftPaddle, outline = 'red')
    self.timeScore += 1
    self.gameCanvas.itemconfig(self.scoreTime,text="Time: " + str(self.\
      timeScore))
    if self.pause == False:
      self.root.after(1000, self.Timer)
    self.timeLeftToDestroy -= 1
    self.gameCanvas.itemconfig(self.timeDestroy,text="Time left to destroy a box: " \
      + str(self.timeLeftToDestroy))

  def Unpause(self):
    if self.timeLeftToDestroy == 0:
      self.gameCanvas.create_text(400, 560, anchor=S, font = ("Comic Sans",\
        20), text = "You waited too long to destroy a box.", fill=\
        "dark grey")
    if self.lives > 1:
      self.gameCanvas.create_text(400, 600, anchor=S, font = ("Comic Sans",\
        20), text = str(self.lives) + " lives remaining. Keep going.", \
        fill="dark grey")
    elif self.lives == 1:
      self.gameCanvas.create_text(400, 600, anchor=S, font = ("Comic Sans",\
        20), text = str(self.lives) + " life remaining. Keep going.", \
        fill="dark grey")
    else:
      self.gameCanvas.create_text(400, 600, anchor=S, font = ("Comic Sans",\
        20), text = str(self.lives) + " lives remaining. Game over.", \
        fill="dark grey")
    if self.pauseTimer == 0 and self.lives > 0:
      self.pause = False
      self.Reset()
      self.GameLoop()
      self.Timer()
    elif self.pauseTimer == 0 and self.lives == 0:
      self.GameOverScreen()
    self.pauseTimer -= 1
    if self.pauseTimer >=0:
      self.root.after(1000, self.Unpause)

  def GameOverScreen(self):
    self.gameCanvas.delete(ALL)
    self.gameCanvas.create_text(400, 150, font=("Comic Sans",35), text = \
      "Score")
    self.gameCanvas.create_text(400, 200, font=("Comic Sans",18), text = \
      "Time last: %d" % self.timeScore)
    self.gameCanvas.create_text(400, 250, font=("Comic Sans",18), text = \
      "Boxes Destroyed: %d" % self.boxesDestroyed)
    self.gameCanvas.create_text(400, 300, font=("Comic Sans",18), text = \
      "Goals: %d" % self.goals)
    self.gameCanvas.create_text(400, 350, font=("Comic Sans",18), text = \
      "Total Score: %d x (%d + (%d x 5)) = " % (self.timeScore, \
      self.boxesDestroyed, self.goals))
    self.gameCanvas.create_text(400, 400, font=("Comic Sans",35), text = \
      "%d" % (self.timeScore*self.pointScore))
    replay = self.gameCanvas.create_text(400, 500, font=("Comic Sans",25),\
      text = "Play again?")
    self.gameCanvas.tag_bind(replay, "<Button-1>", self.NewGame)
    quit = self.gameCanvas.create_text(400, 550, font=("Comic Sans",25),\
      text = "Quit?")
    self.gameCanvas.tag_bind(quit, "<Button-1>", self.Quit)

  def Quit(self, e=None):
    self.root.quit()

  def GameLoop(self):

    ###Gun
    if self.inputChar == " " and self.gunRetract == True and self.gunXPos \
      == 30:
      self.gunRetract = False
      self.gunExtend = True
      self.gameCanvas.itemconfig(self.leftPaddle, fill="grey")
    elif self.inputChar == " " and self.gunExtend == True and self.gunXPos\
      == 60:
      self.gunExtend = False
      self.gunRetract = True
    if self.gunExtend == True and self.gunXPos < 60:
      self.gunXPos += 1
    if self.gunRetract == True and self.gunXPos > 30:
      self.gunXPos -= 1
    if self.gunXPos == 30:
      self.gunMode = False
      self.gameCanvas.itemconfig(self.leftPaddle, fill="black")
    else:
      self.gunMode = True
    if self.gunMode == True and self.inputChar == "o" and self.canFire == \
      True:
      self.bullets.append(self.gameCanvas.create_rectangle(self.gunXPos \
        -15,self.yPos-5, self.gunXPos+15,self.yPos+5,fill='green',
        outline='green',width=5))
      xInstance = self.gunXPos
      yInstance = self.yPos
      self.bulletXPos.append(xInstance)
      self.bulletYPos.append(yInstance)
      self.canFire = False
    if self.gunMode == True and self.inputChar == "p" and self.canFire == \
      True and self.powerUp != 0 and self.firedPower == False:
      if self.powerUp == 1:
        self.powerShot = self.gameCanvas.create_rectangle(self.gunXPos \
        -15,self.yPos-5, self.gunXPos+15,self.yPos+5,fill='yellow',
        outline='black',width=5)
      if self.powerUp == 2:
        self.powerShot = self.gameCanvas.create_rectangle(self.gunXPos \
        -15,self.yPos-5, self.gunXPos+15,self.yPos+5,fill='orange',
        outline='black',width=5)
      self.powerXPos = self.gunXPos
      self.powerYPos = self.yPos
      self.firedPower = True
    if self.powerUp == 0:
      self.gameCanvas.itemconfig(self.gun, fill="grey")
    elif self.powerUp == 1:
      self.gameCanvas.itemconfig(self.gun, fill="yellow")
    elif self.powerUp == 2:
      self.gameCanvas.itemconfig(self.gun, fill="orange")

    ###Bullets
    hits=[]
    for i in self.bullets:
      for j in self.boxes:
        if self.gameCanvas.coords(i)[2] >= self.gameCanvas.coords(j)\
          [0] and self.gameCanvas.coords(i)[1] <= self.gameCanvas.\
          coords(j)[3] and self.gameCanvas.coords(i)[3] >= self.\
          gameCanvas.coords(j)[1] and self.gameCanvas.coords(i)[0]\
          <= self.gameCanvas.coords(j)[2]:
          self.boxHP[self.boxes.index(j)] -= 1
          hits.append(i)
      if self.gameCanvas.coords(i)[0] >= 800:
        hits.append(i)
      self.bulletXPos[self.bullets.index(i)] += 30
    for i in hits:
      try:
        del self.bulletXPos[self.bullets.index(i)]
        del self.bulletYPos[self.bullets.index(i)]
        self.gameCanvas.delete(i)
        del self.bullets[self.bullets.index(i)]
      except: continue
    del hits[:]
    if self.firedPower == True:
      if self.gameCanvas.coords(self.powerShot)[2] >= self.gameCanvas.coords\
        (self.rightPaddle)[0] and self.gameCanvas.coords(self.powerShot\
        )[1] <= self.gameCanvas.coords(self.rightPaddle)[3] and self.\
        gameCanvas.coords(self.powerShot)[3] >= self.gameCanvas.coords\
        (self.rightPaddle)[1] and self.gameCanvas.coords(self.powerShot)\
        [0] <= self.gameCanvas.coords(self.rightPaddle)[2]:
        if self.powerUp == 1:
          self.power1 = True
          self.power2 = False
        if self.powerUp == 2:
          self.power1 = False
          self.power2 = True
        self.powerTimer = 3
        self.firedPower = False
        self.gameCanvas.delete(self.powerShot)
        self.powerUp = 0

      if self.powerXPos >= 800:
        self.firedPower = False
        self.gameCanvas.delete(self.powerShot)
        self.powerUp = 0
      self.powerXPos += 30

    ###Boxes
    zeroHP = []
    for i in self.boxHP:
      if i == 0:
        self.gameCanvas.delete(self.boxes[self.boxHP.index(i)])
        del self.boxes[self.boxHP.index(i)]
        zeroHP.append(self.boxHP.index(i))
        powerOrHurt = randint(1,10)
        if powerOrHurt > 3:
          self.powerUp = randint(1,2)
        else:
          nurf = randint(1,3)
          self.nurfTimer = 3
          if nurf == 1:
            self.power3 = True
            self.power4 = False
            self.power5 = False
          elif nurf == 2:
            self.power3 = False
            self.power4 = True
            self.power5 = False
            #too OP to be 3 seconds
            self.nurfTimer = 2
          elif nurf == 3:
            self.power3 = False
            self.power4 = False
            self.power5 = True
        self.boxesDestroyed += 1
        self.pointScore += 1
        self.gameCanvas.itemconfig(self.scorePoints,text="Points: " + \
          str(self.pointScore))
        self.timeLeftToDestroy = 60
        self.gameCanvas.itemconfig(self.timeDestroy,text="Time left to destroy a box: " \
          + str(self.timeLeftToDestroy))
    for i in zeroHP:
      del self.boxHP[i]

    ###Left Paddle
    if self.yPos > 50 and self.yPos < 550:
      if self.inputChar == "w":
        self.yPos-=self.leftPaddleSpeed
      elif self.inputChar == "s":
        self.yPos+=self.leftPaddleSpeed
    elif self.yPos <= 50:
      self.yPos = 51
    elif self.yPos >= 550:
      self.yPos = 549

    ###Ball
    if self.yPos3 > 15 and self.yPos3 < 585:
      self.xPos3 += self.xSpeed
      self.yPos3 += self.ySpeed
      if self.gunMode == False:
        if self.xPos3 <= self.xPos + 30 and self.xPos3 >= self.xPos and \
          self.yPos3 >= self.yPos - 50 and self.yPos3 <= self.yPos +50:
          self.xSpeed = randint(self.randSpeedVals[0], \
            self.randSpeedVals[1])
          self.ySpeed = randint(-8, 8)
          self.xPos3 = self.xPos + 31
      if self.xPos3 >= self.xPos2 - 30 and self.xPos3 <= self.xPos2 \
        and self.yPos3 >= self.yPos2 - 50 and self.yPos3 <= self.yPos2 \
        +50:
        self.xSpeed = -randint(self.randSpeedVals[0], \
          self.randSpeedVals[1])
        self.ySpeed = randint(-8, 8)
        self.xPos3 = self.xPos2 - 31
      for i in self.boxes:
        if self.xPos3 >= (self.gameCanvas.coords(i)[0] - 15) and \
          self.xPos3 <= self.gameCanvas.coords(i)[0] and self.yPos3 \
          >= self.gameCanvas.coords(i)[1] and self.yPos3 <= \
          self.gameCanvas.coords(i)[3] and self.xSpeed > 0:
          self.xPos3 = self.gameCanvas.coords(i)[0] - 16
          self.xSpeed *= -1
        elif self.xPos3 >= self.gameCanvas.coords(i)[0] and \
          self.xPos3 <= (self.gameCanvas.coords(i)[2] + 15) and \
            self.yPos3 \
          >= self.gameCanvas.coords(i)[1] and self.yPos3 <= \
          self.gameCanvas.coords(i)[3] and self.xSpeed < 0:
          self.xPos3 = self.gameCanvas.coords(i)[2] + 16
          self.xSpeed *= -1
        elif self.xPos3 >= self.gameCanvas.coords(i)[0] and \
          self.xPos3 <= self.gameCanvas.coords(i)[2] and self.yPos3 \
          >= (self.gameCanvas.coords(i)[1] - 15) and self.yPos3 <= \
          self.gameCanvas.coords(i)[3] and self.ySpeed > 0:
          self.yPos3 = self.gameCanvas.coords(i)[1] - 16
          self.ySpeed *= -1
        elif self.xPos3 >= self.gameCanvas.coords(i)[0] and \
          self.xPos3 <= self.gameCanvas.coords(i)[2] and self.yPos3 \
          >= self.gameCanvas.coords(i)[1] and self.yPos3 <= \
          (self.gameCanvas.coords(i)[3] + 15) and self.ySpeed < 0:
          self.yPos3 = self.gameCanvas.coords(i)[3] + 16
          self.ySpeed *= -1
    elif self.yPos3 <= 15:
      self.ySpeed *= -1
      self.yPos3 = 16
    elif self.yPos3 >= 585:
      self.ySpeed *= -1
      self.yPos3 = 584
    if self.xPos3 > 800:
      self.goals += 1
      self.pointScore += 5
      self.gameCanvas.itemconfig(self.scorePoints,text="Points: " + \
        str(self.pointScore))
      self.pause = True
      self.pauseTimer = 2
      self.Unpause()
    if self.xPos3 < 0 or self.timeLeftToDestroy == 0:
      self.lives -= 1
      self.gameCanvas.itemconfig(self.livesText,text="Lives: " + \
        str(self.lives))
      self.pause = True
      self.pauseTimer = 2
      self.Unpause()

    ###Right Paddle
    if self.AIPassOrFail > 1:
      if self.yPos2 > 50 and self.yPos2 < 550:
        if self.yPos3 < self.yPos2 - 25:
          self.yPos2-=self.rightPaddleSpeed
        elif self.yPos3 > self.yPos2 + 25:
          self.yPos2+=self.rightPaddleSpeed
      elif self.yPos2 <= 50:
        self.yPos2 = 51
      elif self.yPos2 >= 550:
        self.yPos2 = 549

    ###UpdatePositions
    self.gameCanvas.coords(self.ball, self.xPos3-15,self.yPos3-15,\
      self.xPos3+15,self.yPos3+15)
    for i in self.bullets:
      self.gameCanvas.coords(i, self.bulletXPos[self.bullets.index(i)]- \
        15,  self.bulletYPos[self.bullets.index(i)]-5, \
        self.bulletXPos[self.bullets.index(i)]+15, \
        self.bulletYPos[self.bullets.index(i)]+5)
    self.gameCanvas.coords(self.powerShot, self.powerXPos-15,self.powerYPos\
      -5, self.powerXPos+15,self.powerYPos+5)
    self.gameCanvas.coords(self.gun, self.gunXPos-15,self.yPos-5, \
      self.gunXPos+15,self.yPos+5)
    self.gameCanvas.coords(self.leftPaddle, self.xPos-15,self.yPos-50,\
      self.xPos+15,self.yPos+50)
    self.gameCanvas.coords(self.rightPaddle, self.xPos2-15,self.yPos2-50,\
      self.xPos2+15,self.yPos2+50)
    if self.pause == False:
      self.root.after(20, self.GameLoop)
Game()
