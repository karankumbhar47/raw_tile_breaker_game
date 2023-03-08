import pygame

class Collision:
    def __init__(self,surface, object):
        self.surface = surface
        self.object = object
        self.objectRect, self.objectPoints = None, None
        self.surfaceRect, self.surfacePoints = None, None
        self.makeRect()

    def makeRect(self):
        self.objectRect = self.object.img.get_rect()
        self.objectRect.x = self.object.x_cor
        self.objectRect.y = self.object.y_cor
        self.objectPoints =[
            [self.objectRect.topleft, self.objectRect.midtop, self.objectRect.topright],
            [self.objectRect.midleft, self.objectRect.center, self.objectRect.midright],
            [self.objectRect.bottomleft, self.objectRect.midbottom, self.objectRect.bottomright]
        ]

        self.surfaceRect = self.surface.img.get_rect()
        self.surfaceRect.x = self.surface.x_cor
        self.surfaceRect.y = self.surface.y_cor
        self.surfacePoints =[
            [self.surfaceRect.topleft, self.surfaceRect.midtop, self.surfaceRect.topright],
            [self.surfaceRect.midleft, self.surfaceRect.center, self.surfaceRect.midright],
            [self.surfaceRect.bottomleft, self.surfaceRect.midbottom, self.surfaceRect.bottomright]
        ]

    def collisionDetect(self):
        self.makeRect()

        if self.objectRect.midbottom[1]<self.surfaceRect.midbottom[1] and self.objectRect.midbottom[1] >= self.surfaceRect.midtop[1]:
            self.topSurfaceCollision()
        elif self.objectRect.midright[0] >= self.surfaceRect.midleft[0] and self.objectRect.midright[0] < self.surfaceRect.midright[0]:
            self.leftSurfaceCollision()
        elif self.objectRect.midleft[0] >= self.surfaceRect.midleft[0] and self.objectRect.midleft[0] <= self.surfaceRect.midright[0]:
            self.rightSurfaceCollision()
        elif self.objectRect.bottomright == self.surfaceRect.topleft or self.objectRect.bottomleft == self.surfaceRect.topright or self.objectRect.topleft == self.surfaceRect.bottomright or self.objectRect.topright == self.surfaceRect.bottomleft:
            self.extremeSurfaceCollision()
        elif self.objectRect.midtop[1] > self.surfaceRect.midtop[1] and self.objectRect.midtop[1] <= self.surfaceRect.midbottom[1]:
            self.bottomSurfaceCollision()


    def topSurfaceCollision(self):
        if self.objectRect.midbottom[0] >=self.surfaceRect.topleft[0] and self.objectRect.midbottom[0] <= self.surfaceRect.topright[0]:
            self.object.bounce_from_ciel()
            print("h1")

        elif self.objectRect.bottomright[0] >= self.surfaceRect.topleft[0] and self.objectRect.bottomright[0] <= self.surfaceRect.midtop[0]:
            self.object.bounce_from_ciel()
            print("h2")

        elif self.objectRect.bottomleft[0] >= self.surfaceRect.topleft[0] and self.objectRect.bottomleft[0] <= self.surfaceRect.topright[0]:
            self.object.bounce_from_ciel()
            print("h3")
            
    
    def bottomSurfaceCollision(self):
        if self.objectRect.midtop[0]>= self.surfaceRect.bottomleft[0]  and self.objectRect.midtop[0] <= self.surfaceRect.bottomright[0]:
            self.object.bounce_from_ciel()
            print("b1")
            

        elif self.objectRect.topright[0] > self.surfaceRect.bottomleft[0] and self.objectRect.topright[0] <= self.surfaceRect.midbottom[0]:
            self.object.bounce_from_ciel()
            print("b2")

        elif self.objectRect.topleft[0] < self.surfaceRect.bottomright[0] and self.objectRect.topleft[0] >= self.surfaceRect.midbottom[0]:
            self.object.bounce_from_ciel()
            print("b3")

    def leftSurfaceCollision(self):
        if self.objectRect.midright[1] >= self.surfaceRect.topleft[1] and self.objectRect.midright[1] <= self.surfaceRect.bottomleft[1]:
            self.object.bounce_from_wall()
            print("l1")
            
        elif self.objectRect.topright[1] >= self.surfaceRect.topleft[1] and self.objectRect.topright[1] <= self.surfaceRect.bottomleft[1]:
            self.object.bounce_from_wall()
            print("l2")

        elif self.objectRect.bottomright[1] >= self.surfaceRect.topleft[1] and self.objectRect.bottomright[1] <= self.surfaceRect.bottomleft[1]:
            self.object.bounce_from_wall()
            print("l3")
        
    