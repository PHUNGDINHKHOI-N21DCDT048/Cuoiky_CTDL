def find_divisors_sum(n):
    divisors_sum = 1  # Bắt đầu với 1 vì nếu n là số nguyên dương thì 1 là ước của n và được tính vào tổng
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:  # Tránh trường hợp i và n // i giống nhau (n là số chính phương)
                divisors_sum += n // i
    return divisors_sum

def number_classification(x, y):
    for num in range(x, y+1):
        div_sum = find_divisors_sum(num)
        if div_sum < num:
            print("Số", num, "là deficient.")
        elif div_sum == num:
            print("Số", num, "là perfect.")
        else:
            print("Số", num, "là abundant.")

x = int(input("Nhập số nguyên dương x: "))
y = int(input("Nhập số nguyên dương y (y >= x): "))

if y < x:
    print("y phải lớn hơn hoặc bằng x.")
else:
    print("Phân loại các số từ", x, "đến", y, ":")
    number_classification(x, y)
