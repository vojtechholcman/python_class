import pygame

pygame.init()

width = 600
height = 400
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Charles_helmet')

#barvy
white = (255, 255, 255)
dark = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (100, 99, 99)
yellow = (255, 222, 0)

screen.fill(grey)
pygame.draw.line(screen, red, (0, 55), (width,55), 5)
#fonts = pygame.font.get_fonts() #zjisti vsechny fonty
#print(fonts)

#nastaveni fontu

muj_font = pygame.font.Font('font/font_x.ttf', 50)
#muj_font = pygame.font.Font('font/animals_font.TTF', 50)
muj_text = muj_font.render('Chyť Charlese', True, white )
muj_text_rect = muj_text.get_rect()
muj_text_rect.center = (width//2, 30)
#system_font = pygame.font.SysFont('corel', 64)
#text
#system_text = system_font.render('Nesraž kužel!!', True, white, red)
#system_text_rect = system_text.get_rect()
#system_text_rect.center = (width//2, 50)

#obrazky
helmet_image = pygame.image.load('obrazky/helmet_f_1.png.png')
helmet_rect = helmet_image.get_rect()
helmet_rect.center = (width//2, height//2)

wall_image = pygame.image.load('obrazky/wall.png')
wall_rect = wall_image.get_rect()
wall_rect.center = (width//3, height//3)

pokracovani = True
while pokracovani:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pokracovani = False
    pygame.display.update()

    screen.blit(helmet_image, helmet_rect)
    screen.blit(wall_image, wall_rect)
    screen.blit(muj_text, muj_text_rect)
pygame.quit()