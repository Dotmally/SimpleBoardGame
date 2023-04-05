# Muhafud Ali Farah 101285231.

#importing modules
import pygame as p
import random
import time
p.init()
#specifications and dimensions
ws = 10
hs = 9

square = 80
smalls=10
wn= p.display.set_mode((1200, hs*square))

wn.fill((255, 255, 255  ))

White = (255,87,51)
green = (255,195,0)

Current = White
#drawing my board and checkered number tiles
for i in range(10):
    for j in range(10):
        p.draw.rect(wn, Current, (i * square, j * square, square, square))
        p.draw.line(wn,(0,0,0),[800,0],[800,800],3)
        font = p.font.SysFont('Times New Roman', 24)
        title = font.render('THE BOARD GAME', True, (0, 0, 0))
        img = font.render('Player 1 roll', True, (0,0,0))
        img2 = font.render('Player 2 roll', True, (0, 0, 0))
        wn.blit(title, (900, 10))
        wn.blit(img, (900, 70))
        wn.blit(img2,(900,140))
        p.display.update()
        tiles = str((j * 10) + (i + 1))
        p.font.init()
        tilesdim = p.font.SysFont('Times New Roman', 20, 1)
        tilefont = tilesdim.render(tiles, False, (255,255,255))
        wn.blit(tilefont, ((i * square), (j * square)))
        p.display.update()
        if Current == White:
            Current = green
        else:
            Current = White
    if Current == White:
        Current = green
    else:
        Current = White


p.draw.rect(wn, (84,27,69), (0, 0, 26, 35))
p.display.update()

p.draw.rect(wn, (199,0,57), (18, 0, 26,35))
p.display.update()


time.sleep(5)
#where the location of my players will be stored
player1x = 0
player2x = 0
player1y = 0
player2y = 0
#looping the stimulation
while True:
    for i in range(10):
        for j in range(10):
            p.draw.rect(wn, (84,27,69), (800,0,400,720))
            p.draw.rect(wn, Current, (i * square, j * square, square, square))
            p.draw.line(wn, (0, 0, 0), [800, 0], [800, 800], 3)
            p.display.update()
            tiles = str((j * 10) + (i + 1))
            p.font.init()
            tilesdim = p.font.SysFont('Times New Roman', 20, 1)
            tilefont = tilesdim.render(tiles, False, (255,255,255))
            wn.blit(tilefont, ((i * square), (j * square)))
            p.display.update()
            if Current == White:
                Current = green
            else:
                Current = White
        if Current == White:
            Current = green
        else:
            Current = White
#my two dice values
    dice1 = (random.randrange(1, 5))+ (random.randrange(1, 5))
    dice2 = (random.randrange(1, 5))+ (random.randrange(1, 5))
    player1x += dice1
    player2x += dice2
#
    if  player1x>=10:
        player1x-=10
        player1y+=1
        player1y=player1y
        player1x = player1x
    if player2x>=10:
        player2x-=10
        player2y+=1
        player2y=player2y
        player2x = player2x



    font = p.font.SysFont(None, 24)
    title = font.render('THE BOARD GAME', True, (0, 0, 0))
    img = font.render('Player 1 roll', True, (0, 0, 0))
    img2 = font.render('Player 2 roll', True, (0, 0, 0))
    wn.blit(img, (900, 70))
    wn.blit(title, (900, 10))
    wn.blit(img2, (900, 140))
    img2 = font.render(str(dice1), True, (0, 0, 0))
    img3 = font.render(str(dice2), True, (0, 0, 0))
    wn.blit(img3, (900, 180))
    wn.blit(img2, (900, 100))

    p.draw.rect(wn, (84,27,69), ((player1x * 80)+18, player1y * 80, 26, 35))
    p.display.update()
    time.sleep(0)

    p.draw.rect(wn, (199,0,57), ((player2x * 80) + 36, player2y * 80, 26, 35))
    p.display.update()
    time.sleep(2)
#ending the game
    if player1y>=9:
        font = p.font.SysFont(None, 24)
        end1 = font.render('Player 1 has WON!!', True, (0, 0, 0))
        wn.blit(end1, (980, 320))
        p.display.update()
        time.sleep(2)

        break
    elif player2y>=9:
        font = p.font.SysFont(None, 24)
        end2 = font.render('Player 2 has WON!!', True, (0, 0, 0))
        wn.blit(end2, (940, 320))
        p.display.update()
        time.sleep(2)

        break
    else:
        continue