def Hieu(a, b):
    unique_a = set(a)
    unique_b = set(b)
    difference = unique_a.difference(unique_b)
    result = sorted(difference)
    return result
 
arr_a = [1, 5, 3, 7, 9, 4, 2]
arr_b = [9, 6, 2, 3, 8]
result = Hieu(arr_a, arr_b)
print("Mảng c chứa các số chỉ có trong mảng a mà không có trong mảng b:", result)
