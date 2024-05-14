def pascal(n):
    for i in range(n):
        coefficient = 1
        print("n={} ".format(i), end="")
        for j in range(i + 1):
            print(coefficient, end=" ")
            coefficient = coefficient * (i - j) // (j + 1)
        print()


n = int(input("Nhập số nguyên dương n: "))
pascal(n)
