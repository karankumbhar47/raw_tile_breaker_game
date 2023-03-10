import pygame
import math
import random
from collision import Collision
import pickle
from os import path
from particle import ParticlePrinciple
from pygame import mixer
import time

clock = pygame.time.Clock()
class SubTile:
    def __init__(self, img, x, y) -> None:
        self.img = img
        self.x_cor = x
        self.y_cor = y


class Tile:
    def __init__(self, src, ball, level):
        self.mudTileImg = pygame.image.load('./images/19-Breakout-Tiles.png')
        self.mudTileBreakImg = pygame.image.load(
            './images/20-Breakout-Tiles.png')
        self.steelTileImg = pygame.image.load('./images/17-Breakout-Tiles.png')
        self.steelTileBreakImg = pygame.image.load(
            './images/18-Breakout-Tiles.png')
        self.steelTileBreakImg = pygame.transform.scale(
            self.steelTileBreakImg, (106, 28))
        self.unbreakableTileImg = pygame.image.load(
            './images/07-Breakout-Tiles.png')
        self.unbreakableBreakTileImg = pygame.image.load(
            './images/08-Breakout-Tiles.png')
        self.unbreakableBreakTileImg = pygame.transform.scale(
            self.unbreakableBreakTileImg, (106, 28))
        self.unbreakableBreakedTileImg = pygame.image.load(
            './images/62-Breakout-Tiles.png')
        self.unbreakableBreakedTileImg = pygame.transform.scale(
            self.unbreakableBreakedTileImg, (106, 28))
        self.num = 0
        self.remove = None
        self.src = src
        self.width = self.mudTileImg.get_width()
        self.height = self.mudTileImg.get_height()
        self.tile = None
        self.positionArray = self.createTiles(level)
        self.ball = ball
        self.particle1 = ParticlePrinciple(self.src)

    def build(self, x, y, tileImg):
        self.src.screen.blit(tileImg, (x, y))

    def createTiles(self, level):
        # startTileX = [100,153]
        # startTileY = 100
        # tileXpointsA = [startTileX[0]+(self.width*i) for i in range(0,1)]
        # tileXpointsB = [startTileX[1]+(self.width*i) for i in range(0,5)]
        # tileYpoints = [startTileY+(self.height*i) for i in range(0,1)]

        if path.exists(f'level{level}_data'):
            pickle_in = open(f'level{level}_data', 'rb')
        data = pickle.load(pickle_in)

    def createTiles(self,level):
        # startTileX = [100,153]
        # startTileY = 100
        # tileXpointsA = [startTileX[0]+(self.width*i) for i in range(0,1)]
        # tileXpointsB = [startTileX[1]+(self.width*i) for i in range(0,5)]
        # tileYpoints = [startTileY+(self.height*i) for i in range(0,1)]
        tilePositionArray = []
        if path.exists(f'level{level}_data'):
            pickle_in = open(f'level{level}_data', 'rb')
            data = pickle.load(pickle_in)
        row_count = 0
        tile_width = 106
        tile_height = 28
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(
                        self.unbreakableTileImg, (tile_width, tile_height))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_width
                    img_rect.y = row_count * tile_height
                    tile = [img_rect.x, img_rect.y, self.unbreakableTileImg, 300]
                    tilePositionArray.append(tile)
                    self.num += 1

                if tile == 2:
                    img = pygame.transform.scale(
                        self.steelTileImg, (tile_width, tile_height))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_width
                    img_rect.y = row_count * tile_height
                    tile = [img_rect.x, img_rect.y, self.steelTileImg, 200]
                    tilePositionArray.append(tile)
                    self.num += 1

                if tile == 3:
                    img = pygame.transform.scale(
                        self.mudTileImg, (tile_width, tile_height))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_width
                    img_rect.y = row_count * tile_height
                    tile = [img_rect.x, img_rect.y, self.mudTileImg, 100]
                    tilePositionArray.append(tile)
                    self.num += 1

                col_count += 1
            row_count += 1

        return tilePositionArray

    def displayPattern(self):
        self.particle1.emit()
        for i in range(len(self.positionArray)):
            self.build(
                self.positionArray[i][0], self.positionArray[i][1], self.positionArray[i][2],)

    def collition(self, score):
        for i in self.positionArray:
            tile = SubTile(i[2], i[0], i[1])
            self.collisionDetect(tile, self.ball)
            # test for collision between the two sprites
            if self.remove == 1:
                bullet_sound = mixer.Sound('./audio/laser.wav')
                i[3] -= 100
                if i[2] == self.steelTileImg and i[3] == 100:
                    i[2] = self.steelTileBreakImg
                    bullet_sound.play()
                elif i[2] == self.unbreakableTileImg and i[3] == 200:
                    i[2] = self.unbreakableBreakTileImg
                    bullet_sound.play()
                elif i[2] == self.unbreakableBreakTileImg and i[3] == 100:
                    i[2] = self.unbreakableBreakedTileImg
                    bullet_sound.play()

                if i[3] == 0:
                    explosion_sound = mixer.Sound('./audio/explosion.wav')
                    explosion_sound.play()
                    time.sleep(0.01)
                    for j in range(random.randint(1,20)):
                        self.particle1.add_particles(i[0] + 53,i[1]+14)
                    if i[2] == self.unbreakableBreakedTileImg:
                        score+=300
                    elif i[2] == self.steelTileBreakImg:
                        score +=200
                    else:
                        score += 100
                    self.positionArray.remove(i)
                    self.num -= 1
                self.remove = 0
                break
            # clock.tick(60000)
        return score

    def collisionDetect(self, tile, ball):
        self.makeRect(ball, tile)

        if self.objectRect.midbottom[1] < self.surfaceRect.center[1] and self.objectRect.midbottom[1] >= self.surfaceRect.midtop[1]:
            self.topSurfaceCollision()

        elif self.objectRect.midtop[1] > self.surfaceRect.center[1] and self.objectRect.midtop[1] <= self.surfaceRect.midbottom[1]:
            self.bottomSurfaceCollision()

        elif self.objectRect.midright[0] >= self.surfaceRect.midleft[0] and self.objectRect.midright[0] < self.surfaceRect.center[0]:
            self.leftSurfaceCollision()

        elif self.objectRect.midleft[0] > self.surfaceRect.center[0] and self.objectRect.midleft[0] <= self.surfaceRect.midright[0]:
            self.rightSurfaceCollision()

        elif self.objectRect.bottomright == self.surfaceRect.topleft or self.objectRect.bottomleft == self.surfaceRect.topright or self.objectRect.topleft == self.surfaceRect.bottomright or self.objectRect.topright == self.surfaceRect.bottomleft:
            self.extremeSurfaceCollision()

    def topSurfaceCollision(self):
        if self.objectRect.midbottom[0] >= self.surfaceRect.topleft[0] and self.objectRect.midbottom[0] <= self.surfaceRect.topright[0]:
            self.yChangeTop()
            self.remove = 1

        elif self.objectRect.bottomright[0] > self.surfaceRect.topleft[0] and self.objectRect.bottomright[0] <= self.surfaceRect.midtop[0]:
            self.yChangeTop()
            self.remove = 1

        elif self.objectRect.bottomleft[0] >= self.surfaceRect.topleft[0] and self.objectRect.bottomleft[0] < self.surfaceRect.topright[0]:
            self.yChangeTop()
            self.remove = 1

    def bottomSurfaceCollision(self):
        if self.objectRect.midtop[0] >= self.surfaceRect.bottomleft[0] and self.objectRect.midtop[0] <= self.surfaceRect.bottomright[0]:
            self.yChangeBottom()
            self.remove = 1

        elif self.objectRect.topright[0] > self.surfaceRect.bottomleft[0] and self.objectRect.topright[0] <= self.surfaceRect.midbottom[0]:
            self.yChangeBottom()
            self.remove = 1

        elif self.objectRect.topleft[0] < self.surfaceRect.bottomright[0] and self.objectRect.topleft[0] >= self.surfaceRect.midbottom[0]:
            self.yChangeBottom()
            self.remove = 1

    def leftSurfaceCollision(self):
        if self.objectRect.midright[1] >= self.surfaceRect.topleft[1] and self.objectRect.midright[1] <= self.surfaceRect.bottomleft[1]:
            self.xChangeLeft()
            self.remove = 1

        elif self.objectRect.topright[1] >= self.surfaceRect.topleft[1] and self.objectRect.topright[1] <= self.surfaceRect.bottomleft[1]:
            self.xChangeLeft()
            self.remove = 1

        elif self.objectRect.bottomright[1] >= self.surfaceRect.topleft[1] and self.objectRect.bottomright[1] <= self.surfaceRect.bottomleft[1]:
            self.xChangeLeft()
            self.remove = 1

    def rightSurfaceCollision(self):
        if self.objectRect.midleft[1] >= self.surfaceRect.topleft[1] and self.objectRect.midleft[1] <= self.surfaceRect.bottomleft[1]:
            self.xChangeRight()
            self.remove = 1

        elif self.objectRect.topleft[1] >= self.surfaceRect.topright[1] and self.objectRect.topleft[1] <= self.surfaceRect.bottomright[1]:
            self.xChangeRight()
            self.remove = 1

        elif self.objectRect.bottomleft[1] >= self.surfaceRect.topright[1] and self.objectRect.bottomleft[1] <= self.surfaceRect.bottomright[1]:
            self.xChangeRight()
            self.remove = 1

    def yChangeTop(self):
        if self.ball.y_dir == 1:
            self.ball.y_dir = -1
        self.ball.y_cor += self.ball.speed * self.ball.y_dir
        self.ball.x_cor += self.ball.speed * self.ball.x_dir
        self.ball.build(self.ball.x_cor, self.ball.y_cor)

    def yChangeBottom(self):
        if self.ball.y_dir == -1:
            self.ball.y_dir = 1
        self.ball.x_cor += self.ball.speed * self.ball.x_dir
        self.ball.y_cor += self.ball.speed * self.ball.y_dir
        self.ball.build(self.ball.x_cor, self.ball.y_cor)

    def xChangeLeft(self):
        if self.ball.x_dir == 1:
            self.ball.x_dir = -1
        self.ball.x_cor += self.ball.speed * self.ball.x_dir
        self.ball.y_cor += self.ball.speed * self.ball.y_dir
        self.ball.build(self.ball.x_cor, self.ball.y_cor)

    def xChangeRight(self):
        if self.ball.x_dir == -1:
            self.ball.x_dir = 1
        self.ball.y_cor += self.ball.speed * self.ball.y_dir
        self.ball.x_cor += self.ball.speed * self.ball.x_dir
        self.ball.build(self.ball.x_cor, self.ball.y_cor)

    def makeRect(self, object, surface):
        self.objectRect = object.img.get_rect()
        self.objectRect.y = object.y_cor
        self.objectRect.x = object.x_cor

        self.surfaceRect = surface.img.get_rect()
        self.surfaceRect.y = surface.y_cor
        self.surfaceRect.x = surface.x_cor
