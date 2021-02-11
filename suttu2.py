#suttupaperi


def bmi(paino, pituus):
    """[summary]

    Args:
        paino (float): paino kilogrammoina
        pituus (float): pituus metreinä

    returns:
        float: painoindeksi
    """    
    return paino / pituus** 2


oma_bmi = bmi(74, 1.71)

print('hoh-hoijaa taas on lihottu, painoindeksi on', oma_bmi)

try:
  print(x)
except:
  print('Something went wrong')
finally:
  print('The try except is finished')