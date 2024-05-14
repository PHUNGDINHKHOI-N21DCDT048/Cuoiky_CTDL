def mang_trung_hang(matrix):
    n = len(matrix)
    # Duyệt qua từng cặp hàng trong ma trận
    for i in range(n):
        for j in range(i + 1, n):
            # So sánh từng phần tử của hai hàng
            if matrix[i] == matrix[j]:
                return True
    return False

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3]
]

if mang_trung_hang(matrix):
    print("Ma trận có ít nhất hai hàng giống nhau.")
else:
    print("Ma trận không có ít nhất hai hàng giống nhau.")
