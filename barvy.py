import pygame

pygame.init()

width = 600
height = 300

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('MAX VESTAPENN')
pokracovani = True



#barvy
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
dark_blue = (0, 0, 100)
x = (255, 255, 0)

darkslategray = (121, 205, 205) #
paleturquoise = (174, 238, 238) # hra charles lecrerc
rosybrown = (255, 193, 193)     #
grey = (192, 192, 192)
screen.fill(x) #zakladni nastaveni je cerna obrazovka, tim fill znamena prebarveni obrazovky



while pokracovani:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pokracovani = False

    pygame.display.update() # tady se bude opakovane nahravat kazda zmena v obrazovce, i zmena barvy pozadi

pygame.quit()