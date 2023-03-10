import pygame
import random
import time
from ball import Ball
from screen import Screen
from slider import Slider
from tile import Tile
from pygame import mixer
# from button import Button
from PIL import ImageGrab, ImageFilter
from display import Display
# import win32gui
import pyautogui



pygame.init()

clock = pygame.time.Clock()
fps = 60

#variable
main_menu = 1
screen_height = 800
screen_width = 836
level = 1
levelMax = 5
score =0
pause = False

#creating screen object
scr = Screen(screen_height,screen_width)



def reset(scr):
    screen_height = scr.height
    #creating slider object 
    slider = Slider(0,screen_height-50,scr)
    #creating ball object
    ball = Ball(slider.x_cor + slider.width/2 ,slider.y_cor ,scr,slider)
    ball.ball = ball
    #creating tile object
    tile = Tile(scr,ball,level)
    return slider,ball,tile


slider,ball,tile = reset(scr)


# loading button images
restartBtn = pygame.image.load('./images/restart_btn.png')
saveBtn = pygame.image.load('./images/save_btn.png')
startBtn = pygame.image.load('./images/start_btn.png')
startBtn = pygame.transform.scale(startBtn,(180,80))
exitBtn = pygame.image.load('./images/exit_btn.png')
exitBtn = pygame.transform.scale(exitBtn,(180,80))

#creating button 
# restartBtn = Button(screen_width//2 - 100, screen_height//2 -20,restartBtn,scr)
# startBtn = Button(screen_width//2 - 200, screen_height//2 -40,startBtn,scr)
# exitBtn = Button(screen_width//2 + 50, screen_height//2 -40,exitBtn,scr)
display = Display(scr)
if main_menu == 0:
    mixer.music.load('./audio/background.wav').play()

# giving title and logo and some additional images
pygame.display.set_caption("Tile Breakers")
game_icon = pygame.image.load('./images/brick-breaker.png')
pygame.display.set_icon(game_icon)
water = pygame.image.load('./images/27-Breakout-Tiles.png')
backgroundImg = pygame.image.load('./images/background.jpg')
backgroundImg = pygame.transform.scale(backgroundImg,(screen_width,screen_height))
font = pygame.font.Font('freesansbold.ttf', 32)
heartImg = pygame.image.load('./images/60-Breakout-Tiles.png')
lifeArray = [heartImg]*3

# tile_width = 106
# tile_height = 28
# margin = 0
# def draw_grid():
# 	for c in range(30):
# 		#vertical lines
# 		pygame.draw.line(scr.screen, (255,255,255), (100 + (c * tile_width), 0), (c * tile_width +100, screen_height - margin))
# 		#horizontal lines
# 		pygame.draw.line(scr.screen, (255,255,255), (0, c * tile_height+ 100), (screen_width, c * tile_height +100))

resetCall = 0
life= [3,-1]
running = True
while running:
    # clock.tick(fps)

    #filling color into screen
    scr.screen.fill((0,0,0))

    scr.screen.blit(backgroundImg,(0,0))
    if main_menu==1:
        main_menu,running = display.mainMenuDisplay(main_menu,running)
    elif main_menu==0:
        #key events
        if ball.gameOver==0:
            slider.move()
            ball.move_ball()
            score = tile.collition(score)
            tile.displayPattern()
            if pause ==1:
                screenshot = pygame_blurred_screenshot
            else:
                screenshot = None
            main_menu,ballSpeed,resetCall,pause= display.gameWindow(score,level,ball,pause,screenshot)
            ball.speed = ballSpeed
            # if ball.speed == 0:
            # print(ball.speed)
            # text = font.render("Score :" + str(score), True, (255,255,255))
            # scr.screen.blit(text,(0,0))
            # text = font.render("level "+str(level), True, (255,255,255),)
            # scr.screen.blit(text,(screen_width -110,10))
    


        if ball.gameOver==1:
            tile.positionArray = []
            
            main_menu,score,level,game_over,resetCall = display.restartDisplay(score)
            ball.gameOver = game_over
            

            #     score = 0
            # if restartBtn.draw():
            #     level = 1
            #     ball.game_over = 0
        
        if tile.num == 0:
            tile.positionArray =[]
            tile.displayPattern()
            time.sleep(1)
            if level == levelMax:
                if ball.life == ball.maxlife:
                    ball.life = 3
                    score += 10000
                else:
                    ball.life+=1
            level = level%levelMax 
            level +=1
            life = [ball.life,1]
            resetCall = display.levelNext(level)
            # ball.x_cor = x
            # slider.x_cor = x

            
                
                
        
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #key pressed downword
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and ball.speed !=0:
                slider.x_change = -2.6
            if event.key == pygame.K_RIGHT and ball.speed != 0:
                slider.x_change = 2.6
            if event.key == pygame.K_SPACE:
                # ball.x_cor += ball.dx * (1/5)
                # ball.y_cor += ball.dy  * (1/5)
                # ball.build(ball.x_cor,ball.y_cor)
                ball.state = "moving"
            if event.key == pygame.K_ESCAPE and main_menu+ball.gameOver ==0 :
                pause = not(pause)
                screenshot = ImageGrab.grab(bbox=None)
                blurred_screenshot = screenshot.filter(ImageFilter.GaussianBlur(radius=10))
                pygame_blurred_screenshot = pygame.image.frombuffer(blurred_screenshot.tobytes(), blurred_screenshot.size, blurred_screenshot.mode)
            if event.key == pygame.K_f:
                ball.speed = 2
            if event.key == pygame.K_p:
                if ball.speed > 0:
                    ball.speed =0
                else:
                    ball.speed = ball.speedOriginal

        #key release upward
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                slider.x_change = 0
            if event.key == pygame.K_f :
                ball.speed = ball.speedOriginal
    if resetCall == 1:
        slider,ball,tile = reset(scr)
        score = 0
        if life[1] >0:
            ball.life = life[0]
            life[1]= -1
        else:
            score = 0
        resetCall = 0
        
    pygame.display.update()
    # clock.tick(60)
pygame.quit()