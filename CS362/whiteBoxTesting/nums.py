def calcNums(min, max):
    for n in range(min, max+1):
        if (n**n) % 5 == 0:
            print(n)
            print("  ")

calcNums(48,100)