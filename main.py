import pygame
import random
pygame.init() #inicializuje ze chci pouzit knihovnu pygame

width = 600 #zde si nastavim jak velka ma byt herni plocha (delka)
height = 400 #zde si nastavim jak ma byt velka herni plocha (vyska)

screen = pygame.display.set_mode((width, height)) #tapple - nemeni se, take si zde inicializuji ze chci zobrazit herni plochu

pygame.display.set_caption('Chyť Charlese') #zde si muzu nastavit jmeno toho herniho okna

# zpomaleni cyklu
fps = 120
clock = pygame.time.Clock()

score_hra = 0

#barvy
white = (255, 255, 255)
dark = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)        #zde mam barvy nastavene pomoci RGB
blue = (0, 0, 255)
grey = (100, 99, 99)
yellow = (255, 222, 0)

screen.fill(grey) #vyplni mi obrazovku barvou, kterou tam napisu

#cara
#pygame.draw.line(screen, red, (0, 55), (width,55), 5) #zde si nakreslim caru do herni plochy

#nastaveni_fontu_textu

#fonts = pygame.font.get_fonts() #zjisti vsechny fonty
#print(fonts)                    # vypise mi vsechny fonty

muj_font = pygame.font.Font('font/font_x.ttf', 50) #zde si inicializuji do promnene muj_font, ze chci pouzit dany font
muj_text = muj_font.render('Chyť Charlese', True, white ) #zde mu reknu co chci napsat tim fontem
muj_text_rect = muj_text.get_rect() #zde mu dam tvar obdelniku
muj_text_rect.center = (width//2, 30) #zde nastavim kde ma ten text byt

#obrazky

#obrazky_helmy
helmet_image = pygame.image.load('obrazky/helmet.png') #nahraje mi do tohoto programu obrazek, ktery chci
helmet_image_rect = helmet_image.get_rect()                  #udelam z obrazku obdelnik, aby se mi s nim lepe pracovalo
helmet_image_rect.center = (width//2, height//2)             #reknu si kam ho chci umistit

#obrazek_zdi
wall_image = pygame.image.load('obrazky/wall.png') #nahraje mi do tohoto programu obrazek, ktery chci
wall_image_rect = wall_image.get_rect()                  #udelam z obrazku obdelnik, aby se mi s nim lepe pracovalo
wall_image_rect.center = (width//3, height//3)           #reknu si kam ho chci umistit

#hudba_na_pozadi
#pozadi
pygame.mixer.music.load('sounds/f1_theme_sound.mp3')
pygame.mixer.music.play(-1, 0, 0)
pygame.mixer.music.set_volume(0.3)

#hit
sound_crash = pygame.mixer.Sound('sounds/car_hit_sound_vettel.mp3')
sound_crash.set_volume(0.8)

#score

'''
score_text = pygame.font.Font('font/font_x.ttf', 20) #zde si inicializuji do promnene muj_font, ze chci pouzit dany font
score_zobraz = score_text.render(f'Score: {score_hra}', True, white ) #zde mu reknu co chci napsat tim fontem
score_zobraz_rect = score_zobraz.get_rect() #zde mu dam tvar obdelniku
score_zobraz_rect.center = (width//2-50, 80) #zde nastavim kde ma ten text byt
'''

#hlavni_herni_cyklus

i = 0

pokracovani = True

while pokracovani:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pokracovani = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if wall_image_rect.y > 60:
            wall_image_rect.y -=5
    if keys[pygame.K_s]:
        if wall_image_rect.y < 340:
            wall_image_rect.y +=5
    if keys[pygame.K_a]:
        if wall_image_rect.x > 0:
            wall_image_rect.x -=5
    if keys[pygame.K_d]:
        if wall_image_rect.x < 540:
            wall_image_rect.x +=5



    #kolize
    if wall_image_rect.colliderect(helmet_image_rect):
        helmet_image_rect.centerx = random.randint(32, height-32)
        helmet_image_rect.centery = random.randint(70, height-32)
        sound_crash.play()
        score_hra = score_hra+1
    #score
    score_text = pygame.font.Font('font/font_x.ttf',20)  # zde si inicializuji do promnene muj_font, ze chci pouzit dany font
    score_zobraz = score_text.render(f'Score: {score_hra}', True, white)  # zde mu reknu co chci napsat tim fontem
    score_zobraz_rect = score_zobraz.get_rect()  # zde mu dam tvar obdelniku
    score_zobraz_rect.center = (width // 2 - 255, 30)  # zde nastavim kde ma ten text byt

    screen.blit(score_zobraz, score_zobraz_rect)
    screen.blit(helmet_image, helmet_image_rect) #do obrazovky obtiskni nejdrive obrazek a pak na nej dej ctverec
    screen.blit(wall_image, wall_image_rect)     #do obrazovky obtiskni nejdrive obrazek a pak na nej dej ctverec
    screen.blit(muj_text, muj_text_rect)   #do obrazovky obtiskni nejdrive obrazek a pak na nej dej ctverec
    #screen.blit(score_zobraz, score_zobraz_rect)

    pygame.display.update()

    screen.fill(grey)

    pygame.draw.line(screen, red, (0, 55), (width, 55), 5)  # zde si nakreslim caru do herni plochy
    clock.tick(fps)
pygame.quit()