import sys, pygame
import math
import conversor
from datetime import datetime

pygame.init()

size   = width, height = 800, 600
black  = 0, 0, 0
red    = 255, 0, 0
blue   = 38, 110, 246
yellow = 255, 211, 0
green  = 53, 181, 53

screen = pygame.display.set_mode(size)

center = [width // 2, height // 2]
raio = 250


arcSegundos = pygame.Rect(center[0] - raio, center[1] - raio, raio * 2, raio * 2)
auxRaio = raio + 10
arcMinutos = pygame.Rect(center[0] - auxRaio, center[1] - auxRaio, auxRaio * 2, auxRaio * 2)
auxRaio = raio + 20
arcHoras = pygame.Rect(center[0] - auxRaio, center[1] - auxRaio, auxRaio * 2, auxRaio * 2)

tamHoras = 150
tamMinutos = 200
tamSegundos = 220

angHoras = -90
angMinutos = -90
angSegundos = -90


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)

    pygame.draw.arc(screen, blue, arcSegundos, math.radians(-angSegundos), math.radians(90), 5)
    pygame.draw.arc(screen, yellow, arcMinutos, math.radians(-angMinutos), math.radians(90), 5)
    pygame.draw.arc(screen, green, arcHoras, math.radians(-angHoras), math.radians(90), 5)

    #Desenho do contorno do relogio
    #pygame.draw.circle(screen, red, center, 250, 3)

    #Desenho do ponteiro das horas
    anglulo = math.radians(angHoras)
    x = tamHoras * math.cos(anglulo) + center[0]
    y = tamHoras * math.sin(anglulo) + center[1]
    pygame.draw.line(screen, green, center, [x, y], 5)

    #Desenho do ponteiro dos minutos
    anglulo = math.radians(angMinutos)
    x = tamMinutos * math.cos(anglulo) + center[0]
    y = tamMinutos * math.sin(anglulo) + center[1]
    pygame.draw.line(screen, yellow, center, [x, y], 3)

    #Desenho do ponteiro dos segundos
    anglulo = math.radians(angSegundos)
    x = tamSegundos * math.cos(anglulo) + center[0]
    y = tamSegundos * math.sin(anglulo) + center[1]
    pygame.draw.line(screen, blue, center, [x, y], 1)

    #Obtendo a hora atual
    now = datetime.now()
    #Convertendo a hora para o angulo atual
    angHoras = conversor.HorasParaAngulo(now.hour)
    angMinutos = conversor.MinutosParaAngulo(now.minute)
    angSegundos = conversor.MinutosParaAngulo(now.second)

    print(now.hour, now.minute , now.second)
    

    pygame.display.flip()