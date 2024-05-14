def recursive_gcd(m, n):
    if n == 0:
        return m
    else:
        return recursive_gcd(n, m % n)

def iterative_gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m

m = int(input("Nhập số nguyên dương thứ nhất m: "))
n = int(input("Nhập số nguyên dương thứ hai n: "))

print("Ước số chung lớn nhất của", m, "và", n, "theo phương thức đệ qui là:", recursive_gcd(m, n))
print("Ước số chung lớn nhất của", m, "và", n, "theo phương thức không đệ qui là:", iterative_gcd(m, n))
