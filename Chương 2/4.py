def mang_nhom_hang(matrix):
    n = len(matrix)
    visited = set()  # Dùng tập hợp để lưu trữ các hàng đã được duyệt qua
    for i in range(n):
        if i not in visited:  # Kiểm tra xem hàng đã được duyệt qua chưa
            group = [i+1]  # Bắt đầu một nhóm mới với chỉ mục hàng i
            visited.add(i)
            # Duyệt qua các hàng còn lại để tìm các hàng giống hàng thứ i
            for j in range(i + 1, n):
                if matrix[i] == matrix[j]:
                    group.append(j+1)
                    visited.add(j)
            # In ra nhóm chỉ mục hàng nếu nhóm có nhiều hơn một hàng
            if len(group) > 1:
                print("Nhóm chỉ mục hàng:", *group)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3],
    [7, 8, 9],
    [4, 5, 6],
    [10, 11, 12]
]

print("Các nhóm chỉ mục hàng của các hàng giống nhau:")
mang_nhom_hang(matrix)
