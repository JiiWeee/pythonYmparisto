# toistorakentent
# FOR-silmukka
lista = ['Mika', 'Mikko', 'Harttu', 'Markku']
for opettaja in lista:
    print('Hyvää huomenta', opettaja, '\n')
    if opettaja == 'Harttu':
        break
print('Tervetuloa töihin')

# Kertoma
kertoma = 1
for luku in range(1, 5):
    kertoma = kertoma * luku
print('kertoma on', kertoma)

#While-silmukka
kierroslaskuri = 0
while kierroslaskuri < 5:
    print('tänään kaikki menee pieleen!')
    kierroslaskuri = kierroslaskuri + 1
print('silmukka päättynyt')