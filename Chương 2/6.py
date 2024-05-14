def Tru(a, b):
    # Chuyển mảng a và b thành chuỗi số nguyên
    num_a = int(''.join(map(str, a)))
    num_b = int(''.join(map(str, b)))
    
    # Thực hiện phép trừ
    result = num_a - num_b
    
    return result  # Trả về kết quả phép trừ

a = [9, 8, 7]
b = [1, 2, 3]
print("Kết quả của a - b là:", Tru(a, b))
