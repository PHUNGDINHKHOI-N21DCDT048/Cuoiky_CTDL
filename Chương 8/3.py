# Định nghĩa lớp BaiHat để biểu diễn thông tin của một bài hát
class BaiHat:
    def __init__(self, ten_bai_hat, ten_nhac_si, ten_ca_si):
        self.ten_bai_hat = ten_bai_hat
        self.ten_nhac_si = ten_nhac_si
        self.ten_ca_si = ten_ca_si

# Định nghĩa lớp Album để biểu diễn thông tin của một album
class Album:
    def __init__(self, ten_album):
        self.ten_album = ten_album
        self.danh_sach_bai_hat = []

    def ThemBaiHat(self, bai_hat):
        self.danh_sach_bai_hat.append(bai_hat)

# Định nghĩa lớp TuDien để quản lý các album ca nhạc
class TuDien:
    def __init__(self):
        self.dictionary = {}

    def NhapAlbum(self, album):
        key = self.BamAlbum(album.ten_album)
        if key in self.dictionary:
            print("Album đã tồn tại trong từ điển.")
        else:
            self.dictionary[key] = album

    def XemAlbum(self, ten_album):
        key = self.BamAlbum(ten_album)
        if key in self.dictionary:
            album = self.dictionary[key]
            print(f"Thông tin album '{album.ten_album}':")
            for bai_hat in album.danh_sach_bai_hat:
                print(f"- Bài hát: {bai_hat.ten_bai_hat}, Nhạc sĩ: {bai_hat.ten_nhac_si}, Ca sĩ: {bai_hat.ten_ca_si}")
        else:
            print("Không tìm thấy album trong từ điển.")

    def BamAlbum(self, ten_album):
        return ten_album.lower()

# Tạo một đối tượng của lớp Album và nhập thông tin cho album
album_vpop = Album("V-Pop Hits")
album_vpop.ThemBaiHat(BaiHat("Em Gì Ơi", "Khắc Hưng", "Jack"))
album_vpop.ThemBaiHat(BaiHat("Có Chắc Yêu Là Đây", "Nguyễn Đình Vũ", "Sơn Tùng M-TP"))
album_vpop.ThemBaiHat(BaiHat("Anh Ơi Ở Lại", "Phan Mạnh Quỳnh", "Hương Giang"))

# Tạo một đối tượng của lớp TuDien và nhập album vào từ điển
td = TuDien()
td.NhapAlbum(album_vpop)

# Xem thông tin của album vừa nhập
td.XemAlbum("V-Pop Hits")
