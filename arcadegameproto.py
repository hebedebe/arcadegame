import os
import pygame
import time
import keyboard
import random

player = '\033[01;35m*'
Projectile = '\033[01;34m!'
uneditedplayerpos = 25
difficulty = 1
fire = False
#playerpos = uneditedplayerpos

firepoint = 0
levelcompiled = ''
newloc = 0
level = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
        "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ]

class projectile():
    def move():
        newloc = firepoint + 1
        level[newloc] = Projectile

while True:
    fire = True
    firepoint += 1
    firechance = random.randint(difficulty,1200)
    if firechance <= difficulty:
        fire = True

    try:
        if keyboard.is_pressed('up'):
            if uneditedplayerpos > 10:
                uneditedplayerpos -= 10
        if keyboard.is_pressed('down'):
            if uneditedplayerpos < 41:
                uneditedplayerpos += 10
        if keyboard.is_pressed('left'):
            if uneditedplayerpos != 1 and uneditedplayerpos != 11 and uneditedplayerpos != 21 and uneditedplayerpos != 31 and uneditedplayerpos != 41:
                uneditedplayerpos -= 1
        if keyboard.is_pressed('right'):
            if uneditedplayerpos != 10 and uneditedplayerpos != 20 and uneditedplayerpos != 30 and uneditedplayerpos != 40 and uneditedplayerpos != 50:
                uneditedplayerpos += 1
    except:
        pass
    playerpos = uneditedplayerpos
    moveup = False
    moveupright = False
    moveright = False
    movedownright = False
    movedown = False
    movedownleft = False
    moveleft = False
    moveupleft = False

    warningcolumns = [0, 11, 12, 23, 24, 35, 36, 47, 48, 59]
    levelcompiled = ""

    if fire:
        #firepoint = warningcolumns[random.randint(0,9)]
        pass

    i = 0
    w = 0

    #print(0 % 2)
    #print(12 % 2)
    #print(13 % 2)

    while i < 60:
        #print('s ' + str(i))
        w = 0
        while w < 10:
            #print('w '+ str(w))
            #print('= ' + str(warningcolumns[w]))
            if i == warningcolumns[w]:
                #print('a')
                #print('w ' + str(w))
                if (warningcolumns[w] % 2 == 0):
                    if warningcolumns[w] == firepoint:
                        level[i] = '\033[01;31m@'
                        break
                    else:
                        level[i] = '\033[01;33m@'
                        break
                # elif i == 0:
                #     level[i] = '\033[01;33m@'
                #     break
                else:
                    if warningcolumns[w] == firepoint:
                        level[i] = '\033[01;31m@\n'
                        break
                    else:
                        level[i] = '\033[01;33m@\n'
                        break
            else:
                #print('false')
                level[i] = '\033[01;30m#'
            w += 1
        i = i + 1

    r = 0
    #projectile.move()

    if uneditedplayerpos > 10:
        playerpos = playerpos+2
        if uneditedplayerpos > 20:
            playerpos = playerpos + 2
            if uneditedplayerpos > 30:
                playerpos = playerpos + 2
                if uneditedplayerpos > 40:
                    playerpos = playerpos + 2

    level[playerpos] = player

    while r < i:
        #print(r)
        levelcompiled = levelcompiled + str(level[r])
        r += 1
    time.sleep(0.05)
    os.system('cls')
    print(levelcompiled)
