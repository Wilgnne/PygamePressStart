import sys, pygame
import time
pygame.init()

size = width, height = 800, 600
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
#Futura lista de imagens
parado = []
#Contador que define a imagem atualmente visualizada
paradoAttImg = 0

#Define o tempo de espera para a prixima animação
paradoFramerate = 1/5
#Define o tempo minimo para iniciar a animção
paradoNextFramerate = 0

#Para cada imagem de 0 a 11
for index in range(12):
    #Crio o diretorio da imagem apartir do indice
    diretorio = "sheet/idle/{}.png".format(index)
    #Carrego a imagem
    img = pygame.image.load(diretorio)
    #Adiciono a imagem a lista
    parado.append(img)

deltaTime = 1/60

#Define a posicao atual do player
playerPos = [100, 50]
#Velocidade dada em Pixels/Segundo
velocity = 96

while 1:
    init = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    key=pygame.key.get_pressed()  #Checando teclas pressionadas
    if key[pygame.K_a]:           #Se o a for pressionado
        playerPos[0] = playerPos[0] - velocity * deltaTime
    if key[pygame.K_d]:           #Se o d for pressionado
        playerPos[0] = playerPos[0] + velocity * deltaTime
    if key[pygame.K_w]:           #Se o w for pressionado
        playerPos[1] = playerPos[1] - velocity * deltaTime
    if key[pygame.K_s]:           #Se o s for pressionado
        playerPos[1] = playerPos[1] + velocity * deltaTime

    screen.fill(black)
    #Desenhando a imagem atual na posicao playerPos
    screen.blit(parado[paradoAttImg], playerPos)

    if time.time() > paradoNextFramerate:
        paradoAttImg = paradoAttImg + 1
        paradoAttImg = paradoAttImg % len(parado)
        paradoNextFramerate = time.time() + paradoFramerate

    pygame.display.flip()

    deltaTime = time.time() - init