abeceda = 'abcdefghijklmnopqrstuvwxyz'

zadane_slovo= str(input('Zadej slovo: '))
rozhodnuti = input('Chceš dané slovo dešifrovat, nebo zašifrovat? Dešifrovat = d , zašifrovat = z: ')

if rozhodnuti == 'z':
    posun = 5
    posun = posun%len(abeceda)
    nove_slovo = ''

    for pismeno in zadane_slovo:
        stary_poradi = abeceda.index(pismeno)
        novy_poradi = stary_poradi + posun

        if novy_poradi>len(abeceda):
            novy_poradi = novy_poradi-len(abeceda)

        novy_pismeno = abeceda[novy_poradi]
        nove_slovo=nove_slovo+novy_pismeno

    print('Tvoje nove slovo je: ', nove_slovo)

elif rozhodnuti == 'd':
    posun = -5
    posun = posun%len(abeceda)
    nove_slovo = ''

    for pismeno in zadane_slovo:
        stary_poradi = abeceda.index(pismeno)
        novy_poradi = stary_poradi + posun

        if novy_poradi>len(abeceda):
            novy_poradi = novy_poradi-len(abeceda)
        novy_pismeno = abeceda[novy_poradi]
        nove_slovo=nove_slovo+novy_pismeno

    print('Tvoje nove slovo je: ', nove_slovo)


