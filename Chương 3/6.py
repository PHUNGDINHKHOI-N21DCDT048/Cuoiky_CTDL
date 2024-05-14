class Node:
    def __init__(self, heso, somu):
        self.heso = heso
        self.somu = somu
        self.next = None

class Polynomial:
    def __init__(self):
        self.head = None

    def Them(self, heso, somu):
        new_node = Node(heso, somu)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def Chep(self):
        new_polynomial = Polynomial()  # Tạo một đa thức mới

        # Duyệt qua các số hạng của đa thức gốc và thêm vào đa thức mới
        current = self.head
        while current is not None:
            new_polynomial.Them(current.heso, current.somu)
            current = current.next

        return new_polynomial

    def InDathuc(self):
        current = self.head
        while current is not None:
            print(f"{current.heso}x^{current.somu}", end=" ")
            current = current.next
            if current is not None:
                print("+", end=" ")
        print()


dathuc = Polynomial()
dathuc.Them(3, 2)  # Thêm số hạng 3x^2
dathuc.Them(-5, 1)  # Thêm số hạng -5x^1
dathuc.Them(4, 0)  # Thêm số hạng 4x^0

dathuc_saochep = dathuc.Chep()
print("Đa thức gốc:")
dathuc.InDathuc()
print("Đa thức sao chép:")
dathuc_saochep.InDathuc()
