import pygame

class Ball():
    def __init__(self,x,y,scr,slider):
        super().__init__()
        self.img = pygame.image.load('./images/58-Breakout-Tiles.png')
        self.y_cor = y
        self.x_cor = x
        self.scr = scr
        self.build(self.x_cor,self.y_cor)
        self.state = "static"
        self.speed = 1
        self.x_dir = 1
        self.y_dir = 1
        self.slider = slider
        # self.move_speed = 0.1

    def move_ball(self):
        self.x_cor+=self.speed * self.x_dir
        self.y_cor-=self.speed * self.y_dir

        if self.x_cor <= 1 or self.x_cor >= self.scr.width:
            self.bounce_from_wall()
        if self.y_cor <= 1 :
            self.bounce_from_ciel()
        if self.y_cor >= self.scr.height-1:
            self.reset_position(self.slider.x_cor+40,self.slider.y_cor-20)
        # if self.y_cor >= self.slider.x_chor


        self.build(self.x_cor,self.y_cor)
    
    def build(self,x,y):
        self.scr.screen.blit(self.img,(x,y))

    def bounce_from_wall(self):
        self.x_dir *= -1

    def bounce_from_ciel(self):
        self.y_dir *= -1
        # self.move_speed *= 0.9

    def bounce_from_slider(self):
        self.y_dir *= -1
    
    def reset_position(self,x,y):
        self.x_cor = x
        self.y_cor = y
        self.state = "static"
        # self.move_speed = 0.1
        # self.x_cor *= -1
        