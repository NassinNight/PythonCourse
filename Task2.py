from math import log10

def silnia(n):
  wynik = 1
  for i in range(1, n + 1):
    wynik *= i
  return wynik

for i in range(4, 101):
  a = int(log10(silnia(i))) + 1
  if a == 1:
    print(f"{i}! ma {a} cyfrę")
  elif a % 10 in [2, 3, 4] and a not in [12, 13, 14]:
    print(f"{i}! ma {a} cyfry")
  else:
    print(f"{i}! ma {a} cyfr")
