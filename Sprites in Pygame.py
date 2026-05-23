import pygame
pygame.init()


mainscreen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Sprites in Pygame")
bg_image = pygame.image.load("star bg.webp").convert()
bg_image = pygame.transform.scale(bg_image, (800, 800))

img_rocket = pygame.image.load("rocket.png").convert()
img_rocket = pygame.transform.scale(img_rocket, (100, 100))

img_ufo = pygame.image.load("ufo.png").convert()
img_ufo = pygame.transform.scale(img_ufo, (100, 100))

img_meteor = pygame.image.load("meteor.png")
img_meteor = pygame.transform.scale(img_meteor, (100, 100))

rocket_sprite = img_rocket.get_rect()
rocket_sprite.center = (400, 400)

ufo_sprite = img_ufo.get_rect()
ufo_sprite.center = (600, 600)

meteor_sprite = img_meteor.get_rect()
meteor_sprite.center = (200, 200)
#KEYBINDS



run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #KEYBINDS
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        rocket_sprite.y = rocket_sprite.y - 2
    if keys[pygame.K_DOWN]:
        rocket_sprite.y = rocket_sprite.y + 2
    if keys[pygame.K_LEFT]:
        rocket_sprite.x = rocket_sprite.x - 2
    if keys[pygame.K_RIGHT]:
        rocket_sprite.x = rocket_sprite.x + 2

    #-----
    if keys[pygame.K_w]:
        ufo_sprite.y = ufo_sprite.y - 2
    if keys[pygame.K_s]:
        ufo_sprite.y = ufo_sprite.y + 2
    if keys[pygame.K_a]:
        ufo_sprite.x = ufo_sprite.x - 2
    if keys[pygame.K_d]:
        ufo_sprite.x = ufo_sprite.x + 2


    mainscreen.blit(bg_image, (0, 0))
    mainscreen.blit(img_rocket, rocket_sprite)
    mainscreen.blit(img_ufo, ufo_sprite)
    mainscreen.blit(img_meteor, meteor_sprite)

     
    pygame.display.update()


pygame.quit()