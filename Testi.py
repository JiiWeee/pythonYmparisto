# Esimerkkjä muuttujista

etunimi = 'Mika' #Merkkijono (string)
sukunimi = 'Hakala' # toinen tapa tehdä merkkijono (¨¨)
Kengan_koko = 44 # Kaksiosainen nimi: snake case suositeltu tapa
kenganKoko = 42.5 # Kaksiosainen nimi: dromedar case ,ei suositella
KenganKoko = 52 # Kaksiosainen nimi: camel case, ei suositella
opettaja = True

# Esimerkkejä rakenteista

# Ruudulle tulostaminen
print('opettajana on tänään', etunimi, sukunimi)

print(sukunimi, 'on iso kenkäinen, kengän koko on', Kengan_koko, '\n')

# Kysytään käyttäjältä tietoja (koko nimi)
koko_nimi = input('Kirjoita nimesi ')

# Teksti yhdistäminen (katenointi,concatenation)
tervehdys = 'Morjensta ' + koko_nimi + ', tervetuloa tampereelle'

print(tervehdys, '\n')

# Luetaan numeerista tietoa näppäimistöstä
markat = input('kuinka monta markkaa sait kakarana viikkorahaa? ')
eurot = float(markat) / 6
print('se olisi nykyään', eurot, 'euroa')

 # Funktio pythonissa, esim funktio, joka muuttaa markat euroiksi
def euroa(markkaa):
    """Funktio palauttaa markkoina annetun arvon euroina

    Args:
        markkaa (float): rahamäärä markkoina

    Returns:
        float: rahan määrä euroina
    """    
    return markkaa / 6

viikkoraha = euroa(100)

print('se on nykyisin euroina' , viikkoraha)