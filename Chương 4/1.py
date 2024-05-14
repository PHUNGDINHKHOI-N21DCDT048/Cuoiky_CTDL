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

    def InNguoc_DeQui(self, node):
        if node is None:
            return
        self.InNguoc_DeQui(node.next)
        print(node.data, end=" ")

    def InNguoc_KhongDeQui(self):
        stack = []
        current = self.head
        while current:
            stack.append(current.data)
            current = current.next
        while stack:
            print(stack.pop(), end=" ")


dslk = LinkedList()
dslk.Them(1)
dslk.Them(2)
dslk.Them(3)
dslk.Them(4)

print("Danh sách liên kết:")
current = dslk.head
while current:
    print(current.data, end=" ")
    current = current.next
print()

print("In ngược sử dụng đệ qui:")
dslk.InNguoc_DeQui(dslk.head)
print()

print("In ngược không sử dụng đệ qui:")
dslk.InNguoc_KhongDeQui()
