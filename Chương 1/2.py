def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def neper(n):
    e_sum = 0
    for k in range(n+1):
        e_sum += 1 / factorial(k)
    return e_sum

n = int(input("Nhập vào số nguyên n >= 0: "))
print("Tổng của các số hạng từ a0 đến an là:", neper(n))
