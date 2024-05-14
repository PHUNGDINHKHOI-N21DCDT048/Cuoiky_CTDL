class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def Them(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def DaoNguoc(self):
        if self.head is None:
            return

        stack = []
        current = self.head
        while current:
            stack.append(current)
            current = current.next

        self.head = stack.pop()
        current = self.head
        while stack:
            current.next = stack.pop()
            current = current.next
        current.next = None

    def InDanhSach(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

dslk = LinkedList()
dslk.Them(1)
dslk.Them(2)
dslk.Them(3)
dslk.Them(4)

print("Danh sách liên kết trước khi đảo ngược:")
dslk.InDanhSach()

dslk.DaoNguoc()

print("Danh sách liên kết sau khi đảo ngược:")
dslk.InDanhSach()
