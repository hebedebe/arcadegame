#import modules for future use
import os
import pygame
import time
import keyboard
import random

#define variables
player = '\033[01;35m*'
Projectile = '\033[01;34m!'
uneditedplayerpos = 25
difficulty = 1
fire = False
firepoint = 0
levelcompiled = ''
newloc = 0
warningcolumns = [0, 11, 12, 23, 24, 35, 36, 47, 48, 59]
level = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
        "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ]


class projectile(): #create projectile class
    def move(): #create a move function within the class to manage projectile movement
        newloc = firepoint + 1
        if newloc != warningcolumns[0]:
                if newloc != warningcolumns[1]:
                        if newloc != warningcolumns[2]:
                                if newloc != warningcolumns[3]:
                                        if newloc != warningcolumns[4]:
                                                if newloc != warningcolumns[5]:
                                                        if newloc != warningcolumns[6]:
                                                                if newloc != warningcolumns[7]:
                                                                        if newloc != warningcolumns[8]:
                                                                                if newloc != warningcolumns[9]:
                                                                                        level[newloc] = Projectile
while True: #main loop, runs repated code
    fire = True #sets fire to true, for testing purposes
    firepoint += 1
    firechance = random.randint(difficulty,1200)
    if firechance <= difficulty:
        fire = True

    try: #attempt to check if the keys are being pressed. "try:" is used to avoid crashing the program if an exception occurs
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
        pass #if an error occurs in the key detection, do nothing and continue with the code
    playerpos = uneditedplayerpos
    moveup = False
    moveupright = False
    moveright = False
    movedownright = False
    movedown = False
    movedownleft = False
    moveleft = False
    moveupleft = False


    levelcompiled = ""

    if fire:
        #firepoint = warningcolumns[random.randint(0,9)]
        pass

    i = 0
    w = 0

    #print(0 % 2)
    #print(12 % 2)
    #print(13 % 2)

    while i < 60: #loop generates the level based on previously modified variables
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
    projectile.move()

    if uneditedplayerpos > 10:
        playerpos = playerpos+2
        if uneditedplayerpos > 20:
            playerpos = playerpos + 2
            if uneditedplayerpos > 30:
                playerpos = playerpos + 2
                if uneditedplayerpos > 40:
                    playerpos = playerpos + 2

    level[playerpos] = player

    while r < i: #compiles level into a single string to be printed by the system
        #print(r)
        levelcompiled = levelcompiled + str(level[r])
        r += 1
    time.sleep(0.05) #pauses to prevent speeds that are too high for the player
    os.system('cls') #clears the output for the level to be printed onto
    print(levelcompiled) #prints the compiled level into the output
