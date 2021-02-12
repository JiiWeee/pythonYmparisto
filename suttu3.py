# Otetaan käyttöön modulin saniteetti.py toiminnot
import saniteetti

# funktio painoindeksin (body mass index) laskemiseksi
def bmi(paino, pituus):
    painoindeksi = paino / pituus ** 2
    return painoindeksi

#funktio kehon rasvaprosentin laskemiseksi
def rasvaprosentti(bmi, ika, sukupuoli):
    rprosentti = 1.2 * bmi + 0.23 * ika - 10.8 * sukupuoli - 5.4
    return rprosentti 


# Kysytään käyttäjältä tarvittavat tiedot, huom näppäimistöstä saadaan aina merkkijono (string)
paino_str = input('Anna painosi kilogrammoina: ')
paino = saniteetti.on_jarkeva(paino_str, 20, 200)
pituus_str = input('anna pituutesi metreinä: ')
ika_str = input('kuinka vanha olet: ')
sukupuoli_str = input('paina 1, jos olet mies, 0 jos olet nainen: ')

# Muutetaan merkkijonot luvuiksi
#muuttuja, johon tallentuu tieto virheen tapahtumisesta alustus :false
tapahtui_virhe = False

try:
    #tutkitaan onko merkkijonossa aakkosia ja annetaan tyyppivirhe jos on
    if paino_str.isalpha():
        raise TypeError('vain numerot (0...9) ja desimaalipiste(.) on sallittu')

    #jos ei ole virhettä, muutetaan liukuluvuksi
    paino = float(paino_str)
    
#jos tapahtui virhe, tulostetaan virheilmoitusteksti ja asetetaan virhemuuttujan arvoksi true
except Exception as virhe:
    print(virhe)
    tapahtui_virhe = True

try:
    paino = float(paino_str)

except:
    print('Paino virheellinen')
    tapahtui_virhe = True


#TODO: Tee tyyppitarkistusrutiinit kaikille muuttujilles
try:
    pituus = float(pituus_str)

except:
    print('pituus virheellinen')
    tapahtui_virhe = True

try:
    ika = float(ika_str)

except:
    print('ikätieto virheellinen')
    tapahtui_virhe = True

try:
    sukupuoli = float(sukupuoli_str)

except:
    print('sukupuoli virheellinen syötä vain 1 tai 0')
    tapahtui_virhe = True

if tapahtui_virhe == False:
    painoindeksi = bmi(paino, pituus)
    print('painoindeksisi on:', painoindeksi)
    rprosentti = rasvaprosentti(painoindeksi, ika, sukupuoli)
    print('kehosi rasvaprosentti on:', rprosentti)

else:
    print('tuloksia ei voitu laskea, koska syöttötiedoissa oli virhe')
