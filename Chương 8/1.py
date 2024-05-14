class TuDien:
    def __init__(self):
        self.dictionary = {}

    def NhapTu(self, tu, dongnghia=None, trai_nghia=None):
        key = tu[0].lower()
        if key in self.dictionary:
            self.dictionary[key].append((tu, dongnghia, trai_nghia))
        else:
            self.dictionary[key] = [(tu, dongnghia, trai_nghia)]

    def TraTu(self, tu):
        key = tu[0].lower()
        if key in self.dictionary:
            for entry in self.dictionary[key]:
                if entry[0] == tu:
                    return entry[1], entry[2]
        return None, None

    def NhapTuMoi(self):
        tu = input("Nhập từ: ").strip()
        dong_nghia = input("Nhập từ đồng nghĩa (nếu có): ").strip()
        trai_nghia = input("Nhập từ trái nghĩa (nếu có): ").strip()
        self.NhapTu(tu, dong_nghia, trai_nghia)


td = TuDien()
td.NhapTu("black", "màu đen", "màu trắng")
td.NhapTu("sit", "ngồi", "đứng")
td.NhapTu("cat", "con mèo", "chó")
td.NhapTu("dog", "con chó", "mèo")

while True:
    print("\n1. Tra từ")
    print("2. Nhập từ mới")
    print("3. Thoát")
    choice = input("Chọn chức năng: ")

    if choice == "1":
        tu_can_tra = input("Nhập từ cần tra: ").strip()
        dong_nghia, trai_nghia = td.TraTu(tu_can_tra)
        if dong_nghia and trai_nghia:
            print(f"Từ đồng nghĩa của '{tu_can_tra}' là '{dong_nghia}', từ trái nghĩa là '{trai_nghia}'")
        elif dong_nghia:
            print(f"Từ đồng nghĩa của '{tu_can_tra}' là '{dong_nghia}', không có từ trái nghĩa")
        elif trai_nghia:
            print(f"Từ trái nghĩa của '{tu_can_tra}' là '{trai_nghia}', không có từ đồng nghĩa")
        else:
            print(f"Không tìm thấy từ '{tu_can_tra}' trong từ điển")
    elif choice == "2":
        td.NhapTuMoi()
    elif choice == "3":
        print("Kết thúc chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ.")
