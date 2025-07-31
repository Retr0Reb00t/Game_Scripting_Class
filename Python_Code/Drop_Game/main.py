#three standard imports for pygame games
import sys
import pygame
import random

##########################
#-------------------------
# This is a game where you click sprites before they reach the bottom of the screen
# Game ends when sprite ends bottom of screen
#--------------------------
##########################

########
#LOAD
########
pygame.init() #starts the game/initialized everything

#scenes
# 0 = title, 1 = game, 2 = gameover/replay
scene = 0

#load bug images
bug = pygame.image.load("bee_a.png")
bug2 = pygame.image.load("fly_a.png")
bug3 = pygame.image.load("ladybug_walk_a.png")

bugs = [bug, bug2, bug3]

#flipped bug (for aesthetics)
rSlime = pygame.transform.flip(bug, True, False) #slime, horizontal flip, vertical flip

#Setup the Screen
width = 600
height = 400
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Don't Let the Slime Splat!")
pygame.display.set_icon(bug)

#define colors
green = (74, 93, 35)
orange = (243, 121, 78)
black = (0, 0, 0)

#------------------------------
#Title and Gameover Page Stuff
titleY = 100
titleFont = pygame.font.SysFont("Arial", 65)
bugTitle = titleFont.render("It's Raining Bugs", False, green)
gameOverTitle = titleFont.render("Bug Went Splat", False, green)

playY = 300
btnMargin = 10
btnFont = pygame.font.SysFont("Arial", 30)
playWord = btnFont.render("PLAY", False, green)
quitWord = btnFont.render("QUIT", False, green)
restartWord = btnFont.render("RESTART", False, orange)

playButton = pygame.draw.rect(screen, black, ((width/2)-(playWord.get_width()/2) - btnMargin, playY-btnMargin, playWord.get_width() + (btnMargin*2), playWord.get_height() + (btnMargin*2)), 0)
quitButton = pygame.draw.rect(screen, orange, ((width/4)-(quitWord.get_width()/2) - btnMargin, playY-btnMargin, quitWord.get_width() + (btnMargin*2), quitWord.get_height() + (btnMargin*2)), 0)
restartButton = pygame.draw.rect(screen, green, ((width * .75)-(restartWord.get_width()/2) - btnMargin, playY-btnMargin, restartWord.get_width() + (btnMargin*2), restartWord.get_height() + (btnMargin*2)), 0)

counter = 0
numThings = 7
bugImage = []
bugX = []
bugY = []
bugSpeed = []
baseSpeed = 0.1
speedMult = 1.2

# power-up stuff
powerUp = pygame.image.load("gem_blue.png")
powerX = random.randint(0, width - powerUp.get_width())
powerY = 400 + random.randint(powerUp.get_height(), powerUp.get_height() *2)
powerSpeed = baseSpeed + random.random()/100
powerTimer = 25000

while counter < numThings:
    bugImage.append(random.choice(bugs))
    bugX.append(random.randint(0, width - bug.get_width()))
    bugY.append(0 - random.randint(bug.get_height(), bug.get_height() *2))
    bugSpeed.append((baseSpeed + random.random())/100)
    counter += 1
########
#GAME LOOP
########
gameOver = False
while gameOver == False:
    #quit event: the Pygame special
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    ########
    #MOUSE CLICKS
    ########
    if pygame.mouse.get_pressed()[0]:
        coords = pygame.mouse.get_pos()
        if scene == 0:
            if pygame.Rect.collidepoint(playButton, coords):
                scene = 1
        elif scene == 1:
            counter = 0
            while counter < numThings:
                if coords[0] >= bugX[counter] and coords[0] <= bugX[counter] + bug.get_width() and coords[1] >= bugY[counter] and coords[1] <= bugY[counter] + bug.get_height():
                    bugImage[counter] = random.choice(bugs)
                    bugX[counter] = random.randint(0, width - bug.get_width())
                    bugY[counter] = 0 - random.randint(bug.get_height(), bug.get_height() *2)
                    bugSpeed[counter] *= speedMult
                counter += 1
            if coords[0] >= powerX and coords[0] <= powerX + powerUp.get_width() and coords[1] >= powerY and coords[1] <= powerY + powerUp.get_height():
                powerX = random.randint(0, width - powerUp.get_width())
                powerY = 400 + random.randint(powerUp.get_height(), powerUp.get_height() *2)
                powerSpeed = baseSpeed + random.random()/100
                powerTimer = 25000
                counter = 0
                while counter < numThings:
                    bugSpeed[counter] /= 4
                    counter += 1
        else:
            if pygame.Rect.collidepoint(quitButton, coords):
                gameOver = True
            if pygame.Rect.collidepoint(restartButton, coords):
                counter = 0
                while counter < numThings:
                    bugImage[counter] = random.choice(bugs)
                    bugX[counter] = random.randint(0, width - bug.get_width())
                    bugY[counter] = 0 - random.randint(bug.get_height(), bug.get_height() *2)
                    bugSpeed[counter] = (baseSpeed + random.random())/100
                    counter += 1
                powerX = random.randint(0, width - powerUp.get_width())
                powerY = 400 + random.randint(powerUp.get_height(), powerUp.get_height() *2)
                powerSpeed = baseSpeed + random.random()/100
                powerTimer = 25000
                scene = 0

    ########
    #UPDATE
    ########
    if scene == 1:
        counter = 0
        while counter < numThings:
            if bugY[counter] + bug.get_height() > height:
                scene = 2
            bugY[counter] += bugSpeed[counter]
            counter += 1
        if powerTimer <= 0:
            if powerY - powerUp.get_height() < 0:
                    powerX = random.randint(0, width - powerUp.get_width())
                    powerY = 400 + random.randint(powerUp.get_height(), powerUp.get_height() *2)
                    powerSpeed = baseSpeed + random.random()/100
                    powerTimer = 25000
            else:
                powerY -= powerSpeed
        else:
            powerTimer -= 1
    ########
    #DRAW
    ########
    if scene == 0:
        screen.fill(orange)
        #centered title
        screen.blit(bugTitle, ((width/2)-(bugTitle.get_width()/2), titleY))
        #slime left
        screen.blit(bug, ((width/2)-(bugTitle.get_width()/2)-bug.get_width(), titleY+ (bugTitle.get_height()-bug.get_height())))       
        screen.blit(rSlime, ((width/2) + (bugTitle.get_width()/2), titleY+ (bugTitle.get_height()-bug.get_height())))

        coords = pygame.mouse.get_pos()
        if pygame.Rect.collidepoint(playButton, coords):
            playButton = pygame.draw.rect(screen, green, ((width/2)-(playWord.get_width()/2) - btnMargin, playY-btnMargin, playWord.get_width() + (btnMargin*2), playWord.get_height() + (btnMargin*2)), 0)
        else:
            playButton = pygame.draw.rect(screen, black, ((width/2)-(playWord.get_width()/2) - btnMargin, playY-btnMargin, playWord.get_width() + (btnMargin*2), playWord.get_height() + (btnMargin*2)), 0)
            screen.blit(playWord, ((width/2)-(playWord.get_width()/2), playY))
    elif scene == 1:
        screen.fill(green)
        counter = 0
        while counter < numThings:
            screen.blit(bugImage[counter], (bugX[counter], bugY[counter]))
            counter += 1
        screen.blit(powerUp, (powerX, powerY))
    else:
        screen.fill(black)

        screen.blit(gameOverTitle,(width/2 - gameOverTitle.get_width()/2, titleY))
        screen.blit(bug, ((width/2)-(gameOverTitle.get_width()/2)-bug.get_width(), titleY+ (gameOverTitle.get_height()-bug.get_height())))       
        screen.blit(rSlime, ((width/2) + (gameOverTitle.get_width()/2), titleY+ (gameOverTitle.get_height()-bug.get_height())))

        coords = pygame.mouse.get_pos()
        if pygame.Rect.collidepoint(quitButton, coords):
            quitButton = pygame.draw.rect(screen, green, ((width/4)-(quitWord.get_width()/2) - btnMargin, playY-btnMargin, quitWord.get_width() + (btnMargin*2), quitWord.get_height() + (btnMargin*2)), 0)
        else:
            quitButton = pygame.draw.rect(screen, orange, ((width/4)-(quitWord.get_width()/2) - btnMargin, playY-btnMargin, quitWord.get_width() + (btnMargin*2), quitWord.get_height() + (btnMargin*2)), 0)
            screen.blit(quitWord, ((width/4) - (quitWord.get_width()/2), playY))
        
        if pygame.Rect.collidepoint(restartButton, coords):
            restartButton = pygame.draw.rect(screen, orange, ((width * .75)-(restartWord.get_width()/2) - btnMargin, playY-btnMargin, restartWord.get_width() + (btnMargin*2), restartWord.get_height() + (btnMargin*2)), 0)
        else:
            restartButton = pygame.draw.rect(screen, green, ((width * .75)-(restartWord.get_width()/2) - btnMargin, playY-btnMargin, restartWord.get_width() + (btnMargin*2), restartWord.get_height() + (btnMargin*2)), 0)
            screen.blit(restartWord, ((width * .75)-(restartWord.get_width()/2), playY))
    #flip the page/render the display
    pygame.display.flip()

########
#QUIT
########
pygame.display.quit()