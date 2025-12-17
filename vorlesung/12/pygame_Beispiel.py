import pygame

pygame.init()
breite = 800
hoehe = 600
screen = pygame.display.set_mode((breite, hoehe))
screen.fill((0,0,0))
pygame.display.set_caption("Mein erstes Pygame Programm")

# warte bis jemand das Fenster schliesst
weitermachen = True
r,b,g = 0,0,0
while weitermachen:
    farbe = (r,g,b)
    r = (r + 1) % 255
    g = (g + 2) % 255
    b = (b + 3) % 255
    pygame.draw.rect(screen, farbe, (300, 200, 200, 200),0)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            weitermachen = False
            pygame.quit()
