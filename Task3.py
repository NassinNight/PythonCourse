def krzyzyk(n):
  for _ in range(n):
    print(n*" " + "*" * n)
  for _ in range(n):
    print("*" * (3 * n))
  for _ in range(n):
    print(n*" " + "*" * n)
krzyzyk(4)