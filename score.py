from button import Button
import pygame

class Score:
    def __init__(self,scr,tile):
        self.score = 0
        self.life = 3
        self.gameOver = False
        self.scr = scr
        restartBtn = pygame.image.load('./images/restart_btn.png')
        self.restartBtn = Button(self.scr.width//2 - 40 , self.scr.length//2-10,restartBtn,self.scr)
        self.nextLevel = False
    def restart(self):
        if self.gameOver:
            if self.game_over :
			if self.restart_button.draw():
				.reset(100, screen_height - 130)
				game_over = 0

