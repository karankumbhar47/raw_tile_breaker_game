import pygame
import math
import time
from collision import Collision

class Ball():
    def __init__(self,x,y,scr,slider):
        self.img = pygame.image.load('./images/58-Breakout-Tiles.png')
        self.y_cor = y
        self.x_cor = x
        self.scr = scr
        self.state = "static"
        self.speed = 0.5
        self.speedOriginal = self.speed
        self.x_dir = 1
        self.y_dir = -1
        self.slider = slider
        self.length = self.img.get_height()
        self.width = self.img.get_width()
        self.center = [self.x_cor+(self.width/2),self.y_cor+(self.length/2)]
        self.radius = self.length/2
        self.build(self.x_cor,self.y_cor)
        self.dx = self.speed * self.x_dir
        self.dy = self.speed * self.y_dir
        self.ball = None
        # self.scoreMeasures = Score(self.scr)
        self.life = 3
        self.heartImg = pygame.image.load('./images/60-Breakout-Tiles.png')
        self.heartImg = pygame.transform.scale(self.heartImg,(32,32))
        self.gameOver = False
        

    def move_ball(self):
        # print(self.speed)
        ball1 = self.img
        ball1Rect = ball1.get_rect()
        ball1Rect.x = self.x_cor
        ball1Rect.y = self.y_cor

        slider2 = self.slider.img
        slider2Rect = slider2.get_rect()
        slider2Rect.x = self.slider.x_cor
        slider2Rect.y = self.slider.y_cor
    

        if self.state == "moving":
            self.dx = self.speed * self.x_dir
            self.dy = self.speed * self.y_dir

            
            self.x_cor += self.speed * self.x_dir
            self.y_cor += self.speed * self.y_dir


            collide = Collision(self.slider,self.ball)
            collide.collisionDetect()



            if self.x_cor <= 0 or self.x_cor >= self.scr.width-20:
                self.x_dir *= -1

            if self.y_cor <= 0 :
                self.y_dir *= -1

            if self.y_cor+self.length >= self.scr.height:
                self.reset_position(self.slider.x_cor + self.slider.width/2 - self.radius,self.slider.y_cor - self.length)
                time.sleep(0.01)


        else:
            self.x_cor = self.slider.x_cor + self.slider.width/2 - self.radius
            self.y_cor = self.slider.y_cor - self.length
        
        self.x_cor += self.speed * self.x_dir
        self.y_cor += self.speed * self.y_dir
        self.build(self.x_cor, self.y_cor)
        self.build_heart()

    def build_heart(self):
        y = 0
        x = self.scr.width//2 - 48
        for i in range(self.life):
            self.scr.screen.blit(self.heartImg,(x,y))
            x += self.heartImg.get_width() + 5


    def build(self,x,y):
        self.scr.screen.blit(self.img,(x,y))

    def bounce_from_wall(self):
        self.x_dir *= -1

    def bounce_from_ciel(self):
        if self.y_dir ==1:
            self.y_dir = -1
        # self.y_dir*=1

    def reset_position(self,x,y):
        self.life -= 1
        if self.life ==0:
            self.gameOver = True
        self.x_cor = x
        self.y_cor = y
        self.x_dir = 1
        self.y_dir = -1
        self.state = "static"
        self.dx = self.speed * self.x_dir
        self.dy = self.speed * self.y_dir
        