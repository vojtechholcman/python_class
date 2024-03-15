import pygame

pygame.init()  # inicializace pygame

width = 600  # sirka plochy
height = 300  # vyska plochy
screen = pygame.display.set_mode((width, height))  # nastavy jaky ma byt display (sirka, vyska)
pygame.display.set_caption('*tvuj pocitac kdyz zapnes teamsi*')

# hlavni herni cyklus
pokracovani = True
while pokracovani:
    for event in pygame.event.get():  # pro vsechny prikazy kdy ten jeden  bude krizek tak True zmen na False
        if event.type == pygame.QUIT: # zmacknuti krizku
            pokracovani = False

pygame.quit() #ukonceni pygame