import pygame

class Screen:
    def __init__(self,height,width):
        self.height = height
        self.width = width
        self.screen = self.build()
    
    def build(self):
        screen= pygame.display.set_mode((self.width,self.height))
        return screen 