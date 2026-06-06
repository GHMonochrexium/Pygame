import pygame
import random
import time
pygame.init()
pygame.mixer.init()

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
font1 = pygame.font.SysFont("Arial", 30)
boom = pygame.mixer.music.load("vine_boom.mp3")

run = True
start_time = time.time()
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
    
    if rocket_sprite.colliderect(ufo_sprite):
        text1 = font1.render("Mission Complete!", True, "white")
        pygame.mixer.music.play(1)   #since there is only one sound in this game atm, you dont have to specify.
        rocket_sprite.center = (1100, 1000)
        ufo_sprite.center = (1100, 1000)
        meteor_sprite.center = (1000, 1000)
        mainscreen.blit(text1, (300, 50))
    current_time = time.time()
    if current_time - start_time >= 5:
       meteor_sprite.center = (random.randint(100, 700), random.randint(100, 700))
       start_time = current_time
    elif rocket_sprite.colliderect(meteor_sprite):
        text1 = font1.render("Mission Failed!", True, "white")
        pygame.mixer.music.play(1)   #since there is only one sound in this game atm, you dont have to specify.
        rocket_sprite.center = (1100, 1000)
        ufo_sprite.center = (1500, 1000)
        meteor_sprite.center = (1100, 1000)
        mainscreen.blit(text1, (300, 50))
    pygame.display.update() 

pygame.quit()