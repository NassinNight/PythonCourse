from losowanie_fragmentow import losuj_fragment

def losuj_haslo(n):
  haslo = ""
  while len(haslo) < n:
    fragment = losuj_fragment()
    if len(haslo) == n - 2 and (len(fragment) == 3 or len(fragment) == 4):
        fragment = losuj_fragment()
    elif len(haslo) == n - 3 and (len(fragment) == 2 or len(fragment) == 4):
        fragment = losuj_fragment()
    elif len(haslo) == n - 4 and (len(fragment) == 2 or len(fragment) == 3):
        fragment = losuj_fragment()
    elif len(haslo) == n - 5 and len(fragment) == 4:
        fragment = losuj_fragment()
    elif len(haslo) + len(fragment) <= n:
      haslo += fragment
  return haslo

print("Hasla o dlugosci 8 znakow:")
for _ in range(10):
  print(losuj_haslo(8))

print("\nHasla o dlugosci 12 znakow:")
for _ in range(10):
  print(losuj_haslo(12))

