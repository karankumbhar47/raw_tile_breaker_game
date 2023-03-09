import pygame
import math
import random
from collision import Collision

class SubTile:
    def __init__(self,img,x,y) -> None:
        self.img=img
        self.x_cor = x
        self.y_cor = y

class Tile:
    def __init__(self,src,ball):
        self.mudTileImg = pygame.image.load('./images/17-Breakout-Tiles.png')
        self.steelTileImg = pygame.image.load('./images/19-Breakout-Tiles.png')
        self.unbreakableTileImg = pygame.image.load('./images/07-Breakout-Tiles.png')
        self.num = 0
        
        self.src = src
        self.width = self.mudTileImg.get_width()
        self.height = self.mudTileImg.get_height()

        self.positionArray = self.createTiles()
        self.ball = ball


    def build(self,x,y,tileImg):
        self.src.screen.blit(tileImg,(x,y))
        

    def createTiles(self):
        startTileX = [100,153]
        startTileY = 100
        tileXpointsA = [startTileX[0]+(self.width*i) for i in range(0,6)]
        tileXpointsB = [startTileX[1]+(self.width*i) for i in range(0,5)]
        tileYpoints = [startTileY+(self.height*i) for i in range(0,11)]
        tilePositionArray = []
        for i in range(len(tileYpoints)):
            for j in range(len(tileXpointsA)):
                randomTile = random.choice([self.mudTileImg,self.steelTileImg,self.unbreakableTileImg])
                if randomTile == self.mudTileImg:
                    tilePositionArray.append([tileXpointsA[j],tileYpoints[i],randomTile,100])
                    self.num+=1
                elif randomTile == self.steelTileImg:
                    tilePositionArray.append([tileXpointsA[j],tileYpoints[i],randomTile,200])
                    self.num+=1
                else:
                    tilePositionArray.append([tileXpointsA[j],tileYpoints[i],randomTile,300])
                    self.num+=1

        return tilePositionArray
    
    def displayPattern(self):
        for i in range(len(self.positionArray)):
            self.build(self.positionArray[i][0],self.positionArray[i][1],self.positionArray[i][2],)


    def collition(self,score):
        for i in self.positionArray:
            tile = SubTile(i[2],i[0],i[1])
            collide = Collision(tile,self.ball)
            collide.collisionDetect()
            # test for collision between the two sprites
            if collide.remove ==1:
                i[3] -= 100
                score+=100
                if i[3]==0:
                    self.positionArray.remove(i)
                    self.num-=1
                collide.remove =0
        return score
