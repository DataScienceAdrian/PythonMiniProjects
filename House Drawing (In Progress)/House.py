import pygame, sys
from pygame.locals import *

pygame.init()

WHITE = (255,255,255)
BROWN = (89, 71, 0)
BLUE_HOUSE = (40,38,255)
GREEN_LEAVES = (6,129,0)
YELLOW = (253,255,38)
ORANGE_ROOF = (229,150,42)



screen = pygame.display.set_mode((640,480))

screen.fill(WHITE)

def draw_tree(x,y):
    pygame.draw.rect(screen,(BROWN),(x,y-100,50,100))
    pygame.draw.circle(screen,(GREEN_LEAVES),(x+25,y-120),50)

def draw_house(x,y):
    pygame.draw.rect(screen,(BLUE_HOUSE),(x,y-180,200,180))
    pygame.draw.rect(screen,(BROWN),(x+80,y-60,40,60))


    #Rsowanie dachu
    pygame.draw.polygon(screen, ORANGE_ROOF, ((x, y - 180), (x + 100, y - 250), (x + 200, y - 180)))
    draw_window(x + 20, y - 90)
    draw_window(x + 130, y - 90)

def draw_window(x,y):
    #szkło
    pygame.draw.rect(screen,(207,229,255),(x,y-50,50,50))
    #framuga
    pygame.draw.rect(screen,(0,0,0),(x,y-50,50,50),5)
    pygame.draw.rect(screen,(0,0,0),(x+23,y-50,5,50))
    pygame.draw.rect(screen,(0,0,0),(x,y-27,50,5))

def draw_cloud(x,y,size):

    pygame.draw.circle(screen, WHITE,(x,y),int(size*.5))
    pygame.draw.circle(screen, WHITE,(int(x+size*.5),y),int(size*.6))
    pygame.draw.circle(screen, WHITE,(x+size,int(y-size*.1)),int(size*.4))

def draw_sun(x,y,size):
    pygame.draw.circle(screen, YELLOW, (x,y),int(size*.7))




pygame.draw.rect(screen, (0, 160, 3), (0, 400, 640, 80))
pygame.draw.rect(screen, (135, 255, 255), (0, 0, 640, 400))

#Wywołanie funkcji rysujących
draw_tree(60,400)
draw_tree(550,400)
draw_house(225,400)
draw_sun(150,70,80)
draw_cloud(60,120,80)
draw_cloud(200,50,40)
draw_cloud(450,100,120)


#Nie wyłączanie się konsoli
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()