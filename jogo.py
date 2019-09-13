import sys, pygame
import random
from conversor import distancia
pygame.init()

size = width, height = 800, 600
black = 0, 0, 0

screen = pygame.display.set_mode(size)

cir = pygame.image.load("ps4/cir.png")
quad = pygame.image.load("ps4/quad.png")
tri = pygame.image.load("ps4/tri.png")
xis = pygame.image.load("ps4/x.png")

l = [cir, quad, tri, xis]

toDraw = []
toDrawPos = []
toDrawShuffle = []

for i in range(3):
    aleatorio = random.choice(l)
    toDraw.append(aleatorio)
    toDrawShuffle.append(aleatorio)
    l.remove(aleatorio)

    toDrawPos.append([400 + (i * 100), 450])

random.shuffle(toDrawShuffle)


ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

controle = True
while controle == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: controle = False

    screen.fill(black)

    mouseX, mouseY = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()[0]
    print(click)

    for indice, image in enumerate(toDrawShuffle):
        pos = (400 + (indice * 100), 150)
        for posIndex, imagePos in enumerate(toDrawPos):
            if distancia((imagePos[0] + 37, imagePos[1] + 34), pos) < 50 and image == toDraw[posIndex] and click == 0:
                toDrawPos.pop(posIndex)
                toDraw.pop(posIndex)
                toDrawShuffle.pop(indice)

        screen.blit(image, pos)
    

    for indice, image in enumerate(toDraw):
        
        if distancia((toDrawPos[indice][0] + 37, toDrawPos[indice][1] + 37), [mouseX, mouseY]) < 38 and click == 1:
            toDrawPos[indice] = (mouseX - 37, mouseY - 37)
        else:
            toDrawPos[indice] = [100 + (indice * 100), 450]
            
        
        screen.blit(image, toDrawPos[indice])

    
    if len(toDraw) == 0:
        controle = False

    print("ToDraw")
    print(toDraw)
    print("ToDrawPos")
    print(toDrawPos)
    print("toDrawShuffle")
    print(toDrawShuffle)

    pygame.display.flip()