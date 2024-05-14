def Duynhat(arr):
    unique_arr = list(set(arr))  # Loại bỏ các phần tử trùng nhau và chuyển thành danh sách
    unique_arr.sort()  # Sắp xếp các phần tử theo thứ tự tăng dần
    return unique_arr

arr = [1, 5, 3, 7, 5, 9, 7]
result = Duynhat(arr)
print("Các số duy nhất và được sắp xếp trong mảng là:", result)
