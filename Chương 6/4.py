def Hop(a, b):
    set_a = set(a)
    set_b = set(b)
    union = set_a.union(set_b)
    result = sorted(union)
    return result

 
arr_a = [1, 5, 3, 7, 9, 4, 2]
arr_b = [9, 6, 2, 3, 8]
result = Hop(arr_a, arr_b)
print("Mảng c chứa các số có trong mảng a hoặc trong mảng b:", result)
