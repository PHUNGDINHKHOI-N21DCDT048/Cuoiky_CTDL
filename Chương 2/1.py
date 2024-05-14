def mang_doi_xung(matrix):
    n = len(matrix)
    # Kiểm tra từng phần tử của ma trận so với phần tử đối xứng của nó
    for i in range(n):
        for j in range(i+1, n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

if mang_doi_xung(matrix):
    print("Ma trận là ma trận đối xứng.")
else:
    print("Ma trận không phải là ma trận đối xứng.")
