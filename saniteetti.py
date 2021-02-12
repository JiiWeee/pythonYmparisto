
# kirjasto, jossa on tietojen järkevyystarkistukseen soveltuvia funktioita
# 1. poistetaan tekstistä ylimääräiset merkit, kuten välilyönnit alusta ja lopusta
# 2. vaihdetaan vahingossa syötetty desimaalipilkku(,) desimaalipisteeksi (.)
# 3. Määritellään järkevän arvon alaraja (pienin hyväksyttävä arvo)
# 4. Määritellään järkevän arvon yläraja (suurin hyväksyttävä arvo)

def on_jarkeva(syote, alaraja, ylaraja):
    """
    Puhdistaa merkkijonosta ylimääräiset tulostumattomat merkit ja välilyönnit ja
    selvittää onko syötetty arvo annettujen  rajojen sisällä. funktio muuttaa desimaali
    pilkun desimaalipisteeksi.


    Args:
        syote (string): Näppäimistöltä syötetty arvo
        alaraja (float): pienin sallittu arvo
        ylaraja (float): suurin sallittu arvo
    """

    # poistetaan whitespace merkit merkkijono alusta
    puhdistettu_syote = syote.lstrip()

    # poistetaan whitespace merkit merkkijono alusta
    puhdistettu_syote = puhdistettu_syote.rstrip()

    # selvitetään onko  merkkijonossa pilkku (,)
    pilkunpaikka = puhdistettu_syote.find(',')

    # Jos pilkku löytyy, korvataan pisteellä
    if pilkunpaikka != -1:
        korjattu_syote = puhdistettu_syote.replace(',', '.')
    else:
        korjattu_syote = puhdistettu_syote

    # Muutetaan korjattu syöte merkkijonosta liukuluvuksi

    try:
        luku = float(korjattu_syote)
    except:
        print('Syötetyssä tiedossa on ylimääräisiä merkkejä, vain numerot sallittu')
        luku = 0
    # tarkistetaan, ettei syöte ole alarajan alapuolella
    try:
        if luku < alaraja:
            raise Exception('Syöttämäsi arvo on alle sallitun')
    except Exception as virheilmoitus:
        print(virheilmoitus)

    # Tarkistetaan, ettei syöte ole ylärajan yläpuolella
    try:
        if luku > ylaraja:
            raise Exception('Syöttämäsi arvo on yli sallitun')
    except Exception as virheilmoitus:
        print(virheilmoitus)

    # Palautetaan luku
    return luku


# Testataan toimintaa
tulos = on_jarkeva('123', 1, 500)
print(tulos)
