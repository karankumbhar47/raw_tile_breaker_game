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
        self.speed = 0.3
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
        

    def move_ball(self):
        print(self.speed)
        ball1 = self.img
        ball1Rect = ball1.get_rect()
        ball1Rect.x = self.x_cor
        ball1Rect.y = self.y_cor

        slider2 = self.slider.img
        slider2Rect = slider2.get_rect()
        slider2Rect.x = self.slider.x_cor
        slider2Rect.y = self.slider.y_cor
        
        # print("+==============================================")
        # print(ball1Rect.topleft)
        # print(ball1Rect.topright)
        # print(ball1Rect.bottomright)
        # print(ball1Rect.bottomleft)

        # print(slider2Rect.topleft)
        # print(slider2Rect.topright)
        # print(slider2Rect.bottomright)
        # print(slider2Rect.bottomleft)
        # print("+==============================================")

        if self.state == "moving":
            self.dx = self.speed * self.x_dir
            self.dy = self.speed * self.y_dir

            
            self.x_cor += self.speed * self.x_dir
            self.y_cor += self.speed * self.y_dir


            collide = Collision(self.slider,self.ball)
            collide.collisionDetect()
            # ball1 = self.img
            # ball1Rect = ball1.get_rect()
            # ball1Rect.x = self.x_cor
            # ball1Rect.y = self.y_cor

            # slider2 = self.slider.img
            # slider2Rect = slider2.get_rect()
            # slider2Rect.x = self.slider.x_cor
            # slider2Rect.y = self.slider.y_cor

            # # horizontal top surface collition
            # if slider2Rect.topleft[0] <= ball1Rect.midbottom[0] and slider2Rect.topright[0] >= ball1Rect.midbottom[0]:
            #     if ball1Rect.midbottom[1]<slider2Rect.midbottom[1] and ball1Rect.midbottom[1] >= slider2Rect.midtop[1]:
            #         self.bounce_from_ciel()
            #         print("h1")

            # elif ball1Rect.bottomright[0] > slider2Rect.topleft[0] and ball1Rect.bottomright[0] <= slider2Rect.midtop[0]:
            #     if ball1Rect.midbottom[1] >= slider2Rect.midtop[1] and ball1Rect.midbottom[1]< slider2Rect.midbottom[1]:
            #         self.bounce_from_ciel()
            #         print("h2")

            # elif ball1Rect.bottomleft[0] >= slider2Rect.topleft[0] and ball1Rect.bottomleft[0] < slider2Rect.topright[0]:
            #     if ball1Rect.midbottom[1] >= slider2Rect.midtop[1] and ball1Rect.midbottom[1]< slider2Rect.midbottom[1]:
            #         self.bounce_from_ciel()
            #         print("h3")
            

            # # horizontal bottom surface collition
            # elif slider2Rect.bottomleft[0] <= ball1Rect.midtop[0] and slider2Rect.bottomright[0] >= ball1Rect.midtop[0]:
            #     if ball1Rect.midtop[1]<slider2Rect.midtop[1] and ball1Rect.midtop[1] >= slider2Rect.midbottom[1]:
            #         self.bounce_from_ciel()
            #         print("b1")

            # elif ball1Rect.topright[0] > slider2Rect.bottomleft[0] and ball1Rect.topright[0] <= slider2Rect.midbottom[0]:
            #     if ball1Rect.midtop[1] >= slider2Rect.midbottom[1] and ball1Rect.midtop[1]< slider2Rect.midtop[1]:
            #         self.bounce_from_ciel()
            #         print("b2")

            # elif ball1Rect.topleft[0] > slider2Rect.bottomleft[0] and ball1Rect.topleft[0] <= slider2Rect.midbottom[0]:
            #     if ball1Rect.midtop[1] >= slider2Rect.midbottom[1] and ball1Rect.midtop[1]< slider2Rect.midtop[1]:
            #         self.bounce_from_ciel()
            #         print("b3")

            # # extreme condition
            # elif ball1Rect.bottomright == slider2Rect.topleft or ball1Rect.bottomleft == slider2Rect.topright or ball1Rect.topleft == slider2Rect.bottomright or ball1Rect.topright == slider2Rect.bottomleft:
            #     self.bounce_from_ciel()
            #     self.bounce_from_wall()
            #     print("e3")
    

            # # verticle left surface collition
            # elif ball1Rect.midright[1] >= slider2Rect.topleft[1] and ball1Rect.midright[1] <= slider2Rect.bottomleft[1]:
            #     if ball1Rect.midright[0] >= slider2Rect.topleft[0] and ball1Rect.midright[0] <= slider2Rect.topright[0]:
            #         self.bounce_from_wall()
            #         print("l1")
            
            # elif ball1Rect.topright[1] >= slider2Rect.topleft[1] and ball1Rect.topright[1] <= slider2Rect.bottomleft[1]:
            #     if ball1Rect.midright[0] >= slider2Rect.topleft[0] and ball1Rect.midright[0] <= slider2Rect.topleft[0]:
            #         self.bounce_from_wall()
            #         print("l2")

            # elif ball1Rect.bottomright[1] >= slider2Rect.topleft[1] and ball1Rect.bottomright[1] <= slider2Rect.bottomleft[1]:
            #     if ball1Rect.midright[0] >= slider2Rect.topleft[0] and ball1Rect.midright[0] <= slider2Rect.topright[0]:
            #         self.bounce_from_wall()
            #         print("l3")


            # # verticle right surface collition
            # elif ball1Rect.midleft[1] >= slider2Rect.topright[1] and ball1Rect.midleft[1] <= slider2Rect.bottomright[1]:
            #     if ball1Rect.midleft[0] >= slider2Rect.topleft[0] and ball1Rect.midleft[0] <= slider2Rect.topright[0]:
            #         self.bounce_from_wall()
            #         print("r1")
            
            # elif ball1Rect.topleft[1] >= slider2Rect.topright[1] and ball1Rect.topleft[1] <= slider2Rect.bottomright[1]:
            #     if ball1Rect.midleft[0] >= slider2Rect.topleft[0] and ball1Rect.midleft[0] <= slider2Rect.topright[0]:
            #         self.bounce_from_wall()
            #         print("r2")

            # elif ball1Rect.bottomleft[1] >= slider2Rect.topright[1] and ball1Rect.bottomleft[1] <= slider2Rect.bottomright[1]:
            #     if ball1Rect.midleft[0] >= slider2Rect.topleft[0] and ball1Rect.midleft[0] <= slider2Rect.topright[0]:
            #         self.bounce_from_wall()
            #         print("r3")

            #colltion along y direction
            
            # if object2Rect.colliderect(object1Rect.x, object1Rect.y + dy, self.width, self.length) and ((self.x_cor >= self.slider.x_cor and self.x_cor <= self.slider.x_cor + self.slider.width) or (self.x_cor + self.width >= self.slider.x_cor and self.x_cor + self.width <= self.slider.x_cor + self.slider.width) ):
            #     self.bounce_from_ciel()
            #     print(1)
            # elif object2Rect.colliderect(object1Rect.x + dx , object1Rect.y, self.width, self.length) and ((self.y_cor >= self.slider.y_cor and self.y_cor <= self.slider.y_cor + self.slider.length) or (self.y_cor + self.length >= self.slider.y_cor and self.y_cor + self.length <= self.slider.y_cor + self.slider.length) ):
            #     self.bounce_from_wall()
            #     print(2)
            # elif object2Rect.colliderect(object1Rect.x + dx, object1Rect.y + dy, self.width, self.length):
            #     self.bounce_from_ciel()
            #     self.bounce_from_wall()
            #     print(3)

            # if slider2Rect.topright
            
            



            if self.x_cor <= 0 or self.x_cor >= self.scr.width-20:
                # self.bounce_from_wall()
                self.x_dir *= -1

            if self.y_cor <= 0 :
                # self.bounce_from_ciel()
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
        # pygame.draw.rect(self.scr.screen,(255,255,255),ball1Rect,1)
        # pygame.draw.rect(self.scr.screen,(255,255,255),slider2Rect,1)

    
    def build(self,x,y):
        self.scr.screen.blit(self.img,(x,y))

    def bounce_from_wall(self):
        self.x_dir *= -1

    def bounce_from_ciel(self):
        if self.y_dir ==1:
            self.y_dir = -1
        # self.y_dir*=1

    
    def reset_position(self,x,y):
        self.x_cor = x
        self.y_cor = y
        self.x_dir = 1
        self.y_dir = -1
        self.state = "static"
        self.dx = self.speed * self.x_dir
        self.dy = self.speed * self.y_dir
        