def szachownica(n, k):
    for i in range(n * k * 2):
        for j in range(n):
            if (i // k) % 2 == 0:
                print("#" * k + " " * k, end="")
            else:
                print(" " * k + "#" * k, end="")
        print()
szachownica(4, 3)