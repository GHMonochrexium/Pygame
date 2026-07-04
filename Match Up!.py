import pygame
pygame.init()


mainscreen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Match Up")
font1 = pygame.font.SysFont("Arial", 30)

ninja_img = pygame.image.load("ninja.png")
ninja_img = pygame.transform.scale(ninja_img, (100, 100))

wizard_img = pygame.image.load("wizard.png")
wizard_img = pygame.transform.scale(wizard_img, (100, 100))

wand_img = pygame.image.load("wand.png")
wand_img = pygame.transform.scale(wand_img, (100, 100))

bow_img = pygame.image.load("bow.png")
bow_img = pygame.transform.scale(bow_img, (100, 100))

archer_img = pygame.image.load("archer.png")
archer_img = pygame.transform.scale(archer_img, (100, 100))

sword_img = pygame.image.load("sword.png")
sword_img = pygame.transform.scale(sword_img, (100, 100))

wizard = wizard_img.get_rect()
wizard.center = (100, 700)

wand = wand_img.get_rect()
wand.center = (700, 100)

ninja = ninja_img.get_rect()
ninja.center = (100, 100)


sword = sword_img.get_rect()
sword.center = (700, 400)

archer = archer_img.get_rect()
archer.center = (100, 400)

bow = bow_img.get_rect()
bow.center = (700, 700)
score = 0
font2 = pygame.font.SysFont("Arial", 30)
text2 = font2.render(f"Score: {score}", True, (0, 0, 0))
font3 = pygame.font.SysFont("Arial", 30)
line1 = False
line2 = False
line3 = False
ns = False
nb = False
nw = False
aS = False
ab = False
aw = False
ww = False
ws = False
wb = False

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ninja.collidepoint(event.pos) and line1 == False:
                ns = True
                nw = True 
                nb = True
                print("Ninja Clicked!")
            if wizard.collidepoint(event.pos) and line3 == False:
                ww = True
                ws = True
                wb = True
                print("Wizard Clicked!")
            if archer.collidepoint(event.pos) and line2 == False:
                aS = True
                aw = True
                ab = True
                print("Archer Clicked!")
        if event.type == pygame.MOUSEBUTTONUP:
            if sword.collidepoint(event.pos) and ns:
                nw = False
                nb = False
                ws = False
                aS = False
                line1 = True
                score += 1
                print("Ninja and Sword Matched!")
                
            if sword.collidepoint(event.pos) and aS:
                ws = False
                ns = False
                aw = False
                ab = False
                line2 = True
                print("Archer and Sword Matched!")
            if sword.collidepoint(event.pos)  and ws:
                wb = False
                ww = False
                aS = False
                ns = False
                line3 = True
                print("Wizard and Sword Matched!")
            if bow.collidepoint(event.pos) and nb:
                wb = False
                ns = False
                nw = False
                line1 = True
                ab = False
                print("Ninja and Bow Matched!")
            if bow.collidepoint(event.pos) and ab:
                aS = False
                aw = False
                wb = False
                sb = False
                line2 = True
                score += 1
                print("Archer and Bow Matched!")
            if bow.collidepoint(event.pos) and wb:
                ab = False
                ws = False
                nb = False
                ww = False
                line3 = True
                print("Wizard and Bow Matched!")
            if wand.collidepoint(event.pos) and nw:
                aw = False
                nb = False
                ns = False
                wb = False
                line1 = True
                print("Ninja and Wand Matched!")
            if wand.collidepoint(event.pos) and aw:
                sw = False
                ab = False
                aS = False
                nw = False
                line2 = True
                print("Archer and Wand Matched!")
            if wand.collidepoint(event.pos) and ww:
                ws = False
                aw = False
                wb = False
                nw = False
                line3 = True
                score += 1
                print("Wizard and Wand Matched!")

    mainscreen.fill((0,255,0))
    mainscreen.blit(ninja_img, ninja)
    mainscreen.blit(wand_img, wand)
    mainscreen.blit(bow_img, bow)
    mainscreen.blit(archer_img, archer)
    mainscreen.blit(sword_img, sword)
    mainscreen.blit(wizard_img, wizard)

    if score == 3:
        text3 = font3.render("You Win!", True, (0, 0, 0))
        mainscreen.blit(text3, (300, 100))
        
    if line1 == True:
        if ns == True:
            pygame.draw.line(mainscreen, (0, 0, 255), ninja.center, sword.center, 5)
            
        if nb == True:
            pygame.draw.line(mainscreen, (255, 0, 0), ninja.center, bow.center, 5)
        if nw == True:
            pygame.draw.line(mainscreen, (255,0, 0), ninja.center, wand.center, 5)
    if line2 == True:
        if ab == True:
            pygame.draw.line(mainscreen, (0, 0, 255), archer.center, bow.center, 5)
            
        if aw == True:
            pygame.draw.line(mainscreen, (255, 0, 0), archer.center, wand.center, 5)
        if aS == True:
            pygame.draw.line(mainscreen, (255, 0, 0), archer.center, sword.center, 5)
    if line3 == True:
        if ws == True:
            pygame.draw.line(mainscreen, (255, 0, 0), wizard.center, sword.center, 5)
        if wb == True:
            pygame.draw.line(mainscreen, (255, 0, 0), wizard.center, bow.center, 5)
        if ww == True:
            pygame.draw.line(mainscreen, (0, 0, 255), wizard.center, wand.center, 5)
            
    
    text1 = font1.render("Match the character with their main weapon!", True, (255, 255, 255))
    mainscreen.blit(text1, (100, 20))
    text2 = font2.render(f"Score: {score}", True, (0, 0, 0))
    mainscreen.blit(text2, (300, 60))
# hw make the changes for the wand conditions in mousebutton up again so that the wizard works also add a score feasture
    
    pygame.display.update()
pygame.quit()