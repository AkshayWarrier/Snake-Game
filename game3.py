import pygame as pg
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

start = False
restart = False
def body(x, y):
    pg.draw.rect(win, (255, 0, 0), (x, y, 32, 32))
    pg.draw.rect(win,(128,0,0),(x,y,32,32),2)

def head(x,y):
    pg.draw.rect(win, (128, 0, 0), (x, y, 32, 32))


gameover_font = pg.font.Font('Quicksand-VariableFont_wght.ttf',100)
def gameover_text():
    gameover_text = gameover_font.render("GAME OVER",True,(0,0,0))
    win.blit(gameover_text,(50,200))

menu_font = pg.font.Font('Quicksand-VariableFont_wght.ttf',100)
def menu_text():
    menu_text = menu_font.render("SNAKE GAME",True,(0,0,0))
    win.blit(menu_text,(15,200))

start_font = pg.font.Font('Quicksand-VariableFont_wght.ttf',50)
def start_text():
    start_text = start_font.render("Press Spacebar To Start",True,(0,0,0))
    win.blit(start_text,(50,300))

show_font = pg.font.Font('Quicksand-VariableFont_wght.ttf',25)
def show_length():
    show_text = show_font.render("Length:"+str(n),True,(0,0,0))
    win.blit(show_text,(0,0))



length_font = pg.font.Font('Quicksand-VariableFont_wght.ttf',50)
def length_text():
    length_text = length_font.render("Your length was "+str(n), True, (0, 0, 0))
    win.blit(length_text, (125, 300))

restart_font = pg.font.Font('Quicksand-VariableFont_wght.ttf',40)
def restart_text():
    restart_text = restart_font.render("Press spacebar to play again", True, (0, 0, 0))
    win.blit(restart_text, (75, 350))


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
    if start == False:
        menu_text()
        start_text()
    else:
        grid()
        show_length()


    #create snake
    if start == True:
        for i in range(n):
            time.sleep(0.055/n)
            top[i] += top_change[i]
            left[i] += left_change[i]
            if i == 0:
                head(left[i], top[i])
            else:
                body(left[i],top[i])
    # make boundary
    for i in range(n):
        if left[i] > 640:
            left[i] -= 704
        elif left[i] < 0:
            left[i] += 704
        elif top[i] > 640:
            top[i] -= 704
        elif top[i] < 0:
            top[i] += 704
    #If the head of the snake has touched the body then end the game
    for coordinates in zip(left[1:],top[1:]):
        if coordinates == (left[0],top[0]):
            collision = True
            break
    if collision == True:
        for i in range(n):
            left_change[i] = 0
            top_change[i] = 0
        foodx = 6000
        foody = 6000
        gameover_text()
        length_text()
        restart_text()








    #movement
    if collision == False and start == True:
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


    if start == True:
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
            if event.key == pg.K_SPACE:
                start = True
            if event.key == pg.K_SPACE and collision == True:
                start = False
                collision = False
                n = 1
                left_change = [left_change[0],]
                top_change = [top_change[0],]
                left = [left[0],]
                top = [top[0],]
                north = 0
                south = 0
                west = 0
                east = 0
                foodx = random.randrange(32, 608, 32)
                foody = random.randrange(32, 608, 32)

            if event.key == pg.K_DOWN and (top_change[0]!=-32):
                south_state = True
            elif event.key == pg.K_UP and (top_change[0]!=32):
                north_state = True
            elif event.key == pg.K_RIGHT and (left_change[0]!=-32):
                east_state = True
            elif event.key == pg.K_LEFT and (left_change[0]!=32):
                west_state = True

