import pygame
from pygame import mixer
import random

pygame.init()
pygame.display.set_caption("Flappy Rana")
mixer.music.load('./sounds/music.wav')
mixer.music.play(-1)
jumpSound = mixer.Sound("./sounds/jump.wav")     
screen = pygame.display.set_mode((800,480))
ground = pygame.image.load('./graphics/environment/ground.png')
obstacle0 = pygame.image.load('./graphics/obstacles/0.png')
obstacle1 = pygame.image.load('./graphics/obstacles/1.png')
obstacle2 = pygame.image.load('./graphics/obstacles/2.png')
plane = pygame.image.load('./graphics/plane/red2.png')
pygame.display.set_icon(plane)
obstaclexvalue1 = 850
obstaclexvalue2 = 1350
obstacleyvalue1 = 0
obstacleyvalue2 = 0
playerYvalue = 200
running = False
openingScreen = True
gameOver = False
font = pygame.font.Font('./graphics/font/BD_Cartoon_Shout.ttf', 20)
titleFont = pygame.font.Font('./graphics/font/BD_Cartoon_Shout.ttf', 80)
background = pygame.image.load('./graphics/environment/background.png')
obstacles = [obstacle0, obstacle1, obstacle2]
chosenobstacle1 = random.choice(obstacles)
chosenobstacle2 = random.choice(obstacles)
spacePressed = False
score = 0

def decreaseValue(xvalue):
    xvalue = xvalue - 5
    return xvalue

def decreaseYvalue(yvalue):
    yvalue = yvalue + 3
    return yvalue

def increaseYvalue(yvalue):
    yvalue = yvalue - 100
    return yvalue

def chooseObstacle(obstacle, yvalue):
    if(obstacle == obstacle1 or obstacle == obstacle0): #seedha
        yvalue = 241
    elif(obstacle == obstacle2): #ulta
        yvalue = 0
    return yvalue

def detectBottomCollision(yvalue):
    if(yvalue > 409):
        return True
    else:
        return False

def detectPillarCollision(obstacle, obstacleXvalue, playerYvalue):
    if(obstacle == obstacle1 or obstacle == obstacle0): #seedha
        if(obstacleXvalue <= 458 and obstacleXvalue >= 300 and playerYvalue >= 180):
            return True
    elif(obstacle == obstacle2): #ulta
        if(obstacleXvalue <= 458 and obstacleXvalue >= 300 and playerYvalue <= 239):
            return  True
    return False

def showScore():
    printScore = font.render("SCORE: " + str(score), True, (196,154,132))
    screen.blit(printScore, (5,10))

#opening screen    
play = font.render("Press space to play" , True, (196,154,132))
flappyPlane = titleFont.render("Flappy Rana" , True, (196,154,132))
while(openingScreen == True and running == False):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            openingScreen = False
        elif(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_SPACE):
                spacePressed = True                
    if(spacePressed == True):
        spacePressed = False
        running = True
        openingScreen = False  
    screen.blit(background,(0,0))
    screen.blit(chosenobstacle1,(obstaclexvalue1,obstacleyvalue1))
    screen.blit(chosenobstacle2,(obstaclexvalue2,obstacleyvalue2))
    screen.blit(plane,(355,playerYvalue))
    screen.blit(ground,(0,409))
    screen.blit(flappyPlane, (50, 50))
    screen.blit(play, (260, 360))
    pygame.display.flip()

#game loop
while(running == True):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
        elif(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_SPACE):
                spacePressed = True            
    obstacleyvalue1 = chooseObstacle(chosenobstacle1, obstacleyvalue1)
    obstacleyvalue2 = chooseObstacle(chosenobstacle2, obstacleyvalue2)
    if(obstaclexvalue1 <= -105):
        obstaclexvalue1 = 790
        chosenobstacle1 = random.choice(obstacles)
        score = score + 1
    if(obstaclexvalue2 <= -105):
        obstaclexvalue2 = 1050
        chosenobstacle2 = random.choice(obstacles)
        score = score + 1
    if(spacePressed == True):
        playerYvalue = increaseYvalue(playerYvalue)
        jumpSound.play()
        if(detectPillarCollision(chosenobstacle1,obstaclexvalue1,playerYvalue) == True
           or detectPillarCollision(chosenobstacle2,obstaclexvalue2,playerYvalue) == True):
            running = False
            gameOver = True
        spacePressed = False
    else:
        playerYvalue = decreaseYvalue(playerYvalue)
        if(detectBottomCollision(playerYvalue) == True):
            running = False
            gameOver = True
    obstaclexvalue2 = decreaseValue(obstaclexvalue2)
    screen.blit(background,(0,0))
    screen.blit(chosenobstacle1,(obstaclexvalue1,obstacleyvalue1))
    screen.blit(chosenobstacle2,(obstaclexvalue2,obstacleyvalue2))
    screen.blit(plane,(355,playerYvalue))
    screen.blit(ground,(0,409))
    showScore()
    pygame.display.update()

printGameOver = titleFont.render("Game Over", True, (196,154,132))
printScore = font.render("SCORE: " + str(score), True, (196,154,132))
while(gameOver == True):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            gameOver = False
        elif(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_SPACE):
                spacePressed = True            
    screen.blit(background,(0,0))
    screen.blit(chosenobstacle1,(obstaclexvalue1,obstacleyvalue1))
    screen.blit(chosenobstacle2,(obstaclexvalue2,obstacleyvalue2))
    screen.blit(plane,(355,playerYvalue))
    screen.blit(ground,(0,409))
    screen.blit(printGameOver, (117,150))
    screen.blit(printScore, (345,240))
    pygame.display.update()
