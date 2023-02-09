import pygame
import random
import time
from playsound import playsound
pygame.init()
#Game Display Surface
gd = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

car = pygame.image.load("Car_image.png")
car = pygame.transform.scale(car,(100,120))
Enemy_car = pygame.image.load("Enemy_car.png")
Enemy_car = pygame.transform.scale(Enemy_car,(100,120))
background = pygame.image.load("Fast_and_Furious.jpg")
grass = pygame.image.load("Grass_image.jpg")

white = (225,225,225)
black = (0,0,0)
red = (225,0,0)
green = (0,225,0)
light_green=(0,200,0)
blue = (0,0,225)
gray = (119,118,110)

def Message(size, mess, x_pos, y_pos):
    font = pygame.font.SysFont(None, size)
    render = font.render(mess, True, white)
    gd.blit(render, (x_pos, y_pos))
    pygame.display.update()

def Sec1(size, mess, x_pos, y_pos):
    font = pygame.font.SysFont(None, size)
    render = font.render(mess, True, red)
    gd.blit(render, (x_pos, y_pos))
    pygame.display.update()

def Sec2(size, mess, x_pos, y_pos):
    font = pygame.font.SysFont(None, size)
    render = font.render(mess, True, green)
    gd.blit(render, (x_pos, y_pos))
    pygame.display.update()

def Sec3(size, mess, x_pos, y_pos):
    font = pygame.font.SysFont(None, size)
    render = font.render(mess, True, blue)
    gd.blit(render, (x_pos, y_pos))
    pygame.display.update()

Message(100, "LOADING...", 200, 100)
clock.tick(1.2)

Sec1(70, "I don't have Friends !", 200 , 180)
clock.tick(0.7)
Sec2(70, "I have a ...", 200 , 240)
clock.tick(0.5)
Sec3(70, "Family...!", 200 , 300)
clock.tick(0.3)
    


def button(x_button,y_button,mess_b):
    pygame.draw.rect(gd,green,[x_button,y_button,100,30])
    Message(50,mess_b,x_button,y_button)
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x_button<mouse[0]<x_button+100 and y_button<mouse[1]<y_button+30:
        pygame.draw.rect(gd, light_green, [x_button, y_button, 100, 30])
        Message(50, mess_b, x_button, y_button)
        if click==(1,0,0) and mess_b=="PLAY":
            gameloop()
        elif click==(1,0,0) and mess_b=="QUIT":
            pygame.quit()
            quit()
  
def car_crash(x,x_r,y,y_r):
    if x_r<x<x_r+60 and y_r<y<y_r+90 or x_r<x+60<x_r+60 and y_r<y<y_r+90:
        Message(50,"CRASHED!",200,200)
        pygame.display.update()
        time.sleep(1)
        game_intro()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

def score(count):
    font = pygame.font.SysFont(None, 30)
    screen_text = font.render('score :' + str(count), True, white)
    gd.blit(screen_text, (0, 0))


def game_intro():
    intro=False
    while intro == False:
        gd.blit(background, (0, 0))
        #playsound(("see_you_again.mp3"))
        button(80,120,"PLAY")
        button(80,400,"QUIT")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

def gameloop():
    x = 350
    y = 480
    count = 0
    x_r = random.randrange(100,600)
    y_r = 0
    x_change = 0
    y_change = 0

    pygame.display.update()
    # Making Display Appear Permanent
    game_over = False
    while game_over == False:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:    
                    x_change=+10
                elif event.key==pygame.K_RIGHT:    
                    x_change=-10
                elif event.key==pygame.K_UP:    
                    y_change=+10            
                elif event.key==pygame.K_DOWN:    
                    y_change=-10
            
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change = 0
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    y_change = 0

        gd.fill(gray) # FIlling Colours In Display
        pygame.draw.rect(gd,gray,[x,y,100,120])
        gd.blit(car, (x, y))
        gd.blit(grass, (0,0))
        gd.blit(grass, (700,0))
        if 0<x<90 or 700<x+100:
            Message(100, "GAME-OVER", 200, 200)
            pygame.display.update()
            clock.tick(1.8)
            game_intro()
        score(count)
        gd.blit(Enemy_car,(x_r,y_r))
        y_r+=10
        if y_r==600:
            y_r = 0
            x_r = random.randrange(100,600)
            count += 1
        car_crash(x,x_r,y,y_r)
        x=x-x_change
        clock.tick(40)
        pygame.display.update()

        
        x=x-x_change
        y=y-y_change
        clock.tick(70)

        pygame.display.update() #Updating Changes In Display

game_intro()
gameloop()

pygame.quit()
quit()