import pygame
import math

class Ball():
    def __init__(self,x,y,scr,slider):
        super().__init__()
        self.img = pygame.image.load('./images/58-Breakout-Tiles.png')
        self.y_cor = y
        self.x_cor = x
        self.scr = scr
        self.state = "static"
        self.speed = 3
        self.x_dir = 1
        self.y_dir = -1
        self.slider = slider
        self.lenth = self.img.get_height()
        self.width = self.img.get_width()
        self.center = [self.x_cor+(self.width/2),self.y_cor+(self.lenth/2)]
        self.radius = self.lenth/2
        self.build(self.x_cor,self.y_cor)

    def move_ball(self):
        if self.state == "moving":

            self.x_cor += self.speed * self.x_dir
            self.y_cor +=self.speed * self.y_dir

            if self.x_cor <= 0 or self.x_cor >= self.scr.width-20:
                self.bounce_from_wall()

            if self.y_cor <= 0 :
                self.bounce_from_ciel()

            if self.y_cor >= self.scr.height:
                self.reset_position(self.slider.x_cor+40,self.slider.y_cor-30)

            # distance1 = math.sqrt(((self.center[0] - self.slider.center[0])**2) + ((self.center[1] - self.slider.center[1])**2))
            # print("=======================")
            # print(self.center,self.x_cor,self.y_cor)
            # print(self.slider.center,self.slider.x_cor,self.slider.y_cor)
            # print(distance1,self.radius)
            # print("=======================")
            
            # # distance2 = math.sqrt(((self.center[0] - self.slider.x_center[0])**2) + ((self.center[1] - self.slider.center[1])**2))
            # # distance = self.slider.y_cor - self.center[1]
            # if distance1 <= 30:# and (self.center[0] >= self.slider.x_cor-self.width and self.center[0] <= (self.slider.x_cor + self.width + self.slider.width)):
            #     self.bounce_from_ciel()

            sprite1 = pygame.sprite.Sprite()
            sprite1.image = self.img
            sprite1.rect = sprite1.image.get_rect()
            sprite1.rect.x = self.x_cor
            sprite1.rect.y = self.y_cor

            sprite2 = pygame.sprite.Sprite()
            sprite2.image = self.slider.img
            sprite2.rect = sprite2.image.get_rect()
            sprite2.rect.x = self.slider.x_cor
            sprite2.rect.y = self.slider.y_cor

            # test for collision between the two sprites
            if pygame.sprite.collide_rect(sprite1, sprite2):
                # collision detected
                self.bounce_from_ciel() 
        else:
            self.x_cor = self.slider.x_cor+53-16
            self.y_cor = self.slider.y_cor-32
        
        self.build(self.x_cor, self.y_cor)
        self.center = [self.x_cor+(self.width/2),self.y_cor+(self.lenth/2)]


    
    def build(self,x,y):
        self.scr.screen.blit(self.img,(x,y))

    def bounce_from_wall(self):
        self.x_dir *= -1

    def bounce_from_ciel(self):
        self.y_dir *= -1
        

    
    def reset_position(self,x,y):
        self.x_cor = x
        self.y_cor = y
        self.x_dir = 1
        self.y_dir = -1
        self.state = "static"
        
        