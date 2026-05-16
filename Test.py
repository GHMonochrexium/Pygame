import pygame
pygame.init()
run = True

mainscreen = pygame.display.set_mode((500,500))
pygame.display.set_caption(("My First Pygame Project..."))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    mainscreen.fill("white")
    pygame.display.update()







pygame.quit()

