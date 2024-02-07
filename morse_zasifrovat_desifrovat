morseovka = { 'a' : '.-', 'b' : '-...', 'c' : '-.-.', 'd' : '-..', 'e' : '.', 'f' : '..-.', 'g' : '--.', 'h' : '....', 'i' : '..', 'j' : '.---', 'k' : '-.-', 'l' : '.-..', 'm' : '--', 'n' : '-.', 'o' : '---', 'p' : '.--.', 'q' : '--.-', 'r' : '.-.', 's' : '...', 't' : '-', 'u' : '..-', 'v' : '...-', 'w' : '.--', 'x' : '-..-', 'y' : '-.--', 'z' : '--..', '/' : '/' }
morseovka_obracene = { '.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g', '....' : 'h', '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q', '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-': 'x', '-.--' : 'y', '--..' : 'z', '/' :'/' }

print('Prekladac Morseovy abecedy')
funkce = input('Chces slovo zasifrovat, nebo desifrovat?, Pokud chces zasifrovat = z, nebo desifrovat = d: ')

while funkce != 'z' and funkce !='d':
    print('Zadaj si neco spatne, zkus to znovu.')
    funkce = input('Chces neco zasifrovat, nebo desifrovat?, Pokud chces zasifrovat = z, nebo desifrovat = d: ')

#zasifrovani
if funkce == 'z':
    slovo_zasifrovat = input('Napis sem slovo ktere chces zasifrovat, jednotliva pismena slova se pak budou oddelovat /: ')

    skladani_slova_zasifrovat = ''

    for znak in slovo_zasifrovat:
        if znak in morseovka:
            morseovka_znak = morseovka[znak]
            skladani_slova_zasifrovat = skladani_slova_zasifrovat + morseovka_znak +'/'
    print('Tve slovo je: ',skladani_slova_zasifrovat)
            
#desifrovani
elif funkce == 'd':
    slovo_desifrovat = input('Napis sem jake slovo chces desifrovat, jednotliva pismena oddeluj /, jednotliva slova oddeluj //, priklad: pes bezi - .--././...//-..././--../../ : ')

    slovo_desifrovat_in_morse = ''
    skladani_slova_desifrovat = ''

    slova_z = slovo_desifrovat.split('//')
    for slovo_z in slova_z:
        pismena_z = slovo_z.split('/')
        for pismeno_z in pismena_z:
            pismeno_d = morseovka_obracene[pismeno_z]
            print (pismeno_d, end='')
        print (' ')
