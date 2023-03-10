import pygame

class Slider:
    def __init__(self,x,y,scr):
        self.x_cor = x
        self.y_cor = y
        self.x_change = 0
        
        self.img = pygame.image.load('./images/53-Breakout-Tiles.png')
        self.length = self.img.get_height()
        self.width = self.img.get_width()
        self.center = [self.x_cor+(self.width/2),self.y_cor+(self.length/2)]
        self.scr = scr
        
    def build(self):
        self.scr.screen.blit(self.img,(self.x_cor,self.y_cor))
        

    def move(self):
        self.x_cor += self.x_change
        if self.x_cor <=0 :
            self.x_cor = 0
        elif self.x_cor >= self.scr.width - 120 :
            self.x_cor = self.scr.width - 120
    
        self.build()