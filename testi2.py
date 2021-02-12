# Rakenteellisia tietotyyppejä

# Lista (list)
osallistujat = ['hakala', 'viljanen', 'karilainen' ]
print('Listan toinen jäsen on', osallistujat[1])
osallistujat.append('Vainio')
osallistujat[3] = 'Öllönquist'
print(osallistujat)
print('listassa on' , len(osallistujat), 'henkilöä')

tiimin_vetaja = 'mikko karilainen'
print('nimen pituus on', len(tiimin_vetaja))
print(tiimin_vetaja.upper())

# monikko (tuple)
kouluttajat = 'hakala' , 'viljanen' , 'vainio'
# kouluttajat[3] = 'öllönquist' ei toimi koska jäsentä ei voi 
# tuplen luomisen jälkeen enää muuttaa
print(kouluttajat)

# Joukko (set)
tutkinnon_osat = {'perustehtävät', 'ohjelmistokehittäjä', 'IT-tukihenkilö'}
# Tutkitaam löytyykö joukosta jäsen (alkio) hyvinvointiteknologia-asentaja
print('Raseko järjestää', 'hyvinvointiteknologia-asentaja' in tutkinnon_osat)

# Avain- arvo parit (dictionary aka key value pair)
mini_sanakirja = {'virtahepo' : 'flodhäst', 'karhu' : 'björn', 'kettu': 'räv'}
print('karhu on ruotsiksi', mini_sanakirja['karhu'])