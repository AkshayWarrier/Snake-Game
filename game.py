import pygame as pg
from pygame import mixer
import random
import time
pg.init()
win = pg.display.set_mode((640, 640))
pg.display.set_caption('Snake Game')

run = True



left = []
top = []
left_change = []
top_change = []
n = 1
for i in range(n):
    top.append(320)
    left.append(320 - 32 * i)
    left_change.append(32)
    top_change.append(0)

green = (0, 255, 0)


north = 0
south = 0
east = 0
west = 0


north_state = False
south_state = False
east_state = False
west_state = False

collision = False

def body(x, y):
    pg.draw.rect(win,(255,0,0),(x,y,30,30))
def head(x,y):
    pg.draw.rect(win, (128, 0, 0), (x, y, 30, 30))
    #pg.draw.circle(win,(0,255,255),(x+5,y+2),3)

gameover_font = pg.font.Font('Quicksand-VariableFont_wght.ttf',100)
def gameover_text():
    gameover_text = gameover_font.render("GAME OVER",True,(0,0,0))
    win.blit(gameover_text,(50,200))

length_font = pg.font.Font('Quicksand-VariableFont_wght.ttf',50)
def length_text():
    length_text = length_font.render("Your length was "+str(n), True, (0, 0, 0))
    win.blit(length_text, (125, 300))


def grid():
    for i in range(20):
        if i%2 == 0:
            x = 0
        else:
            x = 1
        for j in range(20):
            if j % 2 == x:
                pg.draw.rect(win,(255,255,255),(32*i,32*j,32,32))
            else:
                pg.draw.rect(win, (0,128,128), (32 * i, 32 * j, 32, 32))

def food(x,y):
    foodimg = pg.image.load('apple.png')
    win.blit(foodimg,(x,y))





foodx = random.randrange(32,608,32)
foody = random.randrange(32,608,32)
while run:

    pg.display.update()
    win.fill((0, 128, 128))
    grid()




    #create snake
    for i in range(n):
        time.sleep(0.055/n)
        top[i] += top_change[i]
        left[i] += left_change[i]
        if i == 0:
            head(left[i], top[i])
        else:
            body(left[i],top[i])

        # make boundary
        if left[i] > 640:
            left[i] = 0
        elif left[i] < 0:
            left[i] = 640
        elif top[i] > 640:
            top[i] = 0
        elif top[i] < 0:
            top[i] = 640

    for coordinates in zip(left[1:],top[1:]):
        if coordinates == (left[0],top[0]):
            collision = True
            break
    if collision == True:
        for i in range(n):
            left[i] = -32
            top[i] = -32
            left_change[i] = 0
            top_change[i] = 0
        foodx = 6000
        foody = 6000
        gameover_text()
        length_text()




    #movement
    if south == n:
        south = 0
        south_state = False
    elif south_state == True and top_change[south] != -32:
        top_change[south] = 32
        left_change[south] = 0
        south +=1

    if north == n:
        north = 0
        north_state = False
    elif north_state == True and top_change[north] != 32:
        top_change[north] = -32
        left_change[north] = 0
        north +=1

    if east == n:
        east = 0
        east_state = False
    elif east_state == True and left_change[east] != -32:
        top_change[east] = 0
        left_change[east] = 32
        east +=1

    if west == n:
        west = 0
        west_state = False
    elif west_state == True and left_change[west] != 32:
        top_change[west] = 0
        left_change[west] = -32
        west +=1


    food(foodx,foody)


    if (foodx,foody) == (left[0],top[0]):
        foodx = random.randrange(32, 608, 32)
        foody = random.randrange(32, 608, 32)
        left_change.append(left_change[-1])
        top_change.append(top_change[-1])
        if top_change[-1] == 32:
            top.append(top[-1]- 32)
            left.append(left[-1])
        elif top_change[-1] == -32:
            top.append(top[-1] + 32)
            left.append(left[-1])
        if left_change[-1] == 32:
            top.append(top[-1])
            left.append(left[-1]- 32)
        if left_change[-1] == -32:
            top.append(top[-1])
            left.append(left[-1] + 32)
        n = n+1

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                south_state = True
            elif event.key == pg.K_UP:
                north_state = True
            elif event.key == pg.K_RIGHT:
                east_state = True
            elif event.key == pg.K_LEFT:
                west_state = True

