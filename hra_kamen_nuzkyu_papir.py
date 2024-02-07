from obrazky_nuzky_papir_kamen import obrazky
import random

green = '\033[32m'
red = '\033[31m'
blue = '\033[34m'
yellow = '\033[93m' 
end = '\033[0m'

skore1 = 0

skore2 = 0

vyhra = ''

pocitac = 'Radim'
remiza = 'remiza'

pravda = True

print('Hrajes proti ', pocitac)
jmeno= str(input('Zadej svoje jmeno: ')) 



for i in range (10):

    hrac1 = random.randint(0,2)
    print('********************************************************************************')
    print((red + "                 KAMEN" + end), obrazky[0]) 
    print((red + "            ZADEJ: 0" + end))                          
    print('================================================================================')
    print((green + "                 NUZKY"  + end), obrazky[1]) 
    print((green + "            ZADEJ: 1" + end))                                                                         
    print('================================================================================')
    print((blue + "                 PAPIR" + end), obrazky[0]) 
    print((blue + "            ZADEJ: 2" + end))                                                     
    print('********************************************************************************')

    print(red + "KAMEN: 0" + end)
    print(green + "NUZKY: 1" + end)
    print(blue + "PAPIR: 2" + end)

    hrac2 = int(input(': '))

    hrac2novy = hrac2 + 1

    while(hrac2!= 0 and hrac2!= 1 and hrac2!=2):
        print('Zadal jsi neco spatne, zadej to znovu.')
        hrac2 = int(input('Co chces zvolit, kamen = 0, nuzky = 1, papir = 2: '))

    if hrac1 == 0 and hrac2 == 1:
        vyhra = pocitac 
        skore1 = skore1 + 1
    elif hrac1 == 0 and hrac2 == 2:
        vyhra= jmeno
        skore2 = skore2 + 1
    elif hrac1 == 1 and hrac2 == 0:
        vyhra = jmeno
        skore1 = skore1 + 1
    elif hrac1 == 1 and hrac2 == 2:
        vyhra = pocitac
        skore2 = skore2 + 1
    elif hrac1 == 2 and hrac2 == 0:
        vyhra= pocitac
        skore1 = skore1 + 1
    elif hrac1 == 2 and hrac2 == 1:
        vyhra = jmeno
        skore2 = skore2 + 1
    elif hrac2 == hrac1: 
        vyhra= remiza

    skore1 = skore1

    skore2 = skore2

    if hrac1 == 0:
        hrac1 = obrazky[0]
    elif hrac1 == 1:
        hrac1 = obrazky[1]
    elif hrac1 == 2:
         hrac1 = obrazky[2]

    if hrac2 == 0:
        hrac2 = obrazky[0]
    elif hrac2 == 1:
        hrac2 = obrazky[1]
    elif hrac2 == 2:
        hrac2 = obrazky[2]

    print('********************************************')
    print('Ty zvolil jsi: ')
    print(hrac2)
    print('********************************************')

    print('********************************************')
    print('Radim zvolil: ')
    print(hrac1)
    print('********************************************')

    print('Vyhral : ',vyhra )
    print('*******************************************')

if skore1 > skore2:
    fullvyhra = pocitac
elif skore1 < skore2:
    fullvyhra = jmeno
elif skore1 == skore2:
    fullvyhra = "remíza"

print('Celkovym vyhercem je: ', fullvyhra)
