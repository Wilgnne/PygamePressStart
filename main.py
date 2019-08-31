import sys, pygame
pygame.init()

size = width, height = 320, 240
black = 0, 0, 0
red = 255, 0, 0

screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)

    pygame.draw.rect(screen, red, pygame.Rect(10, 10, 50, 50), 3)
    pygame.draw.circle(screen, red, [int(width/2), int(height/2)], 50, 1)

    pygame.display.flip()