def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

def iterative_fibonacci(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b

n = int(input("Nhập vào số nguyên n >= 0: "))
print("Số Fibonacci thứ", n, "theo phương thức đệ qui là:", recursive_fibonacci(n))
print("Số Fibonacci thứ", n, "theo phương thức không đệ qui là:", iterative_fibonacci(n))
