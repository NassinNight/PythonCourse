def koperta(n):
  for i in range(2 * n + 1):
    for j in range(2 * n + 1):
      if i == 0 or i == 2 * n or j == 0 or j == 2 * n or i == j or i == 2 * n - j:
        print("*", end="")
      else:
        print(" ", end="")
    print()

koperta(4)