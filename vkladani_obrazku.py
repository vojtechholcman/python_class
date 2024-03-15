import pygame

pygame.init() #inicializace pygame
#nastaveni
width = 600
height = 400
screen = pygame.display.set_mode((width, height)) #zobrazeni obrazovky
pygame.display.set_caption('Nesraž kužel **NEMOŽNÉ, ŠÍLENÉ**')

# barva
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (100, 99, 99)

screen.fill(grey) #vyplni obrazovku

#obrazky
helmeto_image = pygame.image.load('obrazky/helmet_f_1.png.png')
helmeto_rect = helmeto_image.get_rect()
#auto_rect.bottom = 200 #da obrazek podle dolni listy
#auto_rect.top = 400 - 64 #da obrazek podle horni listy
auto_rect.center = (width//2, height//2) #da to podle stredu obrazku

kuzel_image = pygame.image.load('obrazky/kuzel.png')
kuzel_rect = kuzel_image.get_rect()
kuzel_rect.center = (400, 100)

#telo programu
pokracovani = True
while pokracovani:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pokracovani = False

    pygame.display.update()

    screen.blit(helmeto_image, helmeto_rect)
    #screen.blit(kuzel_image, kuzel_rect)
pygame.quit()