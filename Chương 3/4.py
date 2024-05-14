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

    def DoiDau(self):
        current = self.head
        while current is not None:
            current.heso = -current.heso  # Đổi dấu của hệ số
            current = current.next

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
print("Đa thức trước khi đổi dấu:")
dathuc.InDathuc()
dathuc.DoiDau()
print("Đa thức sau khi đổi dấu:")
dathuc.InDathuc()
