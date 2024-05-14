def Giao(a, b):
    set_a = set(a)
    set_b = set(b)
    intersection = set_a.intersection(set_b)
    result = sorted(intersection)
    return result

arr_a = [1, 5, 3, 7, 9, 4, 2]
arr_b = [9, 6, 2, 3, 8]
result = Giao(arr_a, arr_b)
print("Mảng c chứa các số chỉ có trong cả hai mảng a và b:", result)
