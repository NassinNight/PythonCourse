from duze_cyfry import daj_cyfre, pytajnik


def drukuj_dlc(liczba):
  cyfry = [daj_cyfre(int(c)) for c in str(liczba)]

  for i in range(5):
    for cyfra in cyfry:
      print(cyfra[i] + "  ", end="")
    print()

drukuj_dlc(12345)