class TuDien:
    def __init__(self):
        self.dictionary = {}

    def NhapTu(self, tu, dongnghia=None, trai_nghia=None):
        key = self.BamTu(tu)
        if key in self.dictionary:
            self.dictionary[key].append((tu, dongnghia, trai_nghia))
        else:
            self.dictionary[key] = [(tu, dongnghia, trai_nghia)]

    def DongNghia(self, tu):
        key = self.BamTu(tu)
        if key in self.dictionary:
            return [entry[1] for entry in self.dictionary[key] if entry[0] == tu and entry[1] is not None]
        return []

    def TraiNghia(self, tu):
        key = self.BamTu(tu)
        if key in self.dictionary:
            return [entry[2] for entry in self.dictionary[key] if entry[0] == tu and entry[2] is not None]
        return []

    def BamTu(self, tu):
        return tu[0].lower()

    def NhapTuMoi(self):
        tu = input("Nhập từ: ").strip()
        dong_nghia = input("Nhập từ đồng nghĩa (nếu có): ").strip()
        trai_nghia = input("Nhập từ trái nghĩa (nếu có): ").strip()
        self.NhapTu(tu, dong_nghia, trai_nghia)


td = TuDien()
td.NhapTu("siêng năng", "chăm chỉ", "lười biếng")
td.NhapTu("khỏe mạnh", "cường tráng", "yếu ớt")


while True:
    print("\n1. Tra từ")
    print("2. Nhập từ mới")
    print("3. Thoát")
    choice = input("Chọn chức năng: ")

    if choice == "1":
        tu_can_tra = input("Nhập từ cần tra: ").strip()
        dong_nghia = td.DongNghia(tu_can_tra)
        trai_nghia = td.TraiNghia(tu_can_tra)

        if dong_nghia:
            print(f"Từ đồng nghĩa của '{tu_can_tra}' là: {', '.join(dong_nghia)}")
        else:
            print(f"Không có từ đồng nghĩa của '{tu_can_tra}' trong từ điển")

        if trai_nghia:
            print(f"Từ trái nghĩa của '{tu_can_tra}' là: {', '.join(trai_nghia)}")
        else:
            print(f"Không có từ trái nghĩa của '{tu_can_tra}' trong từ điển")
    elif choice == "2":
        td.NhapTuMoi()
    elif choice == "3":
        print("Kết thúc chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ.")
