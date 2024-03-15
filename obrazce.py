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

screen.fill(black) #zakladni nastaveni je cerna obrazovka, tim fill znamena prebarveni obrazovky
pygame.draw.line(screen, white,(0,50), (width,50),) # cara
pygame.draw.rect(screen, white,(100,111, 400,211)) # obdelnik
pygame.draw.circle(screen, red, (300,200), 60, width=2) #kruh, kruznice podle width, kdyz nula tak khur


while pokracovani:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pokracovani = False

    pygame.display.update() # tady se bude opakovane nahravat kazda zmena v obrazovce, i zmena barvy pozadi

pygame.quit()
