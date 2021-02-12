# Luodaan painoindeksin laskentafunktio
def painoindeksi(pituus, paino):
    """painoindeksi lasketaan jakamalla paino pituuden neliöllä

    Args:
        pituus (float): henkilön pituus metreinä
        paino (float): Paino kilogrammoina
    """
    bmi = paino / (pituus**2)
    return bmi


mikan_painoindeksi = painoindeksi(1.7, 73)
print('Mikan painoindeksi on', mikan_painoindeksi)