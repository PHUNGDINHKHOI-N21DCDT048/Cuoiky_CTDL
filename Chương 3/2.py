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

    def RutGon(self):
        if self.head is None:
            return

        # Sắp xếp các số hạng theo số mũ giảm dần
        self.SapXep()

        prev = None
        current = self.head
        while current.next is not None:
            if current.somu == current.next.somu:
                current.heso += current.next.heso
                temp = current.next
                current.next = temp.next
                del temp
            else:
                prev = current
                current = current.next

        # Loại bỏ các số hạng có hệ số bằng 0
        current = self.head
        while current is not None and current.heso == 0:
            self.head = current.next
            current = self.head
        while current is not None:
            if current.heso == 0:
                prev.next = current.next
                current = prev.next
            else:
                prev = current
                current = current.next

    def SapXep(self):
        if self.head is None:
            return

        current = self.head
        while current.next is not None:
            temp = current.next
            while temp is not None:
                if current.somu < temp.somu:
                    current.somu, temp.somu = temp.somu, current.somu
                    current.heso, temp.heso = temp.heso, current.heso
                temp = temp.next
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
dathuc.Them(2, 2)  # Thêm số hạng 2x^2
dathuc.Them(-3, 3)  # Thêm số hạng -3x^3
dathuc.Them(1, 1)  # Thêm số hạng x^1
print("Đa thức trước khi rút gọn:")
dathuc.InDathuc()
dathuc.RutGon()
print("Đa thức sau khi rút gọn:")
dathuc.InDathuc()
