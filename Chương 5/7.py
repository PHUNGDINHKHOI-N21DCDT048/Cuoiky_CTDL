class TreeNode:
    def __init__(self, value):
        self.info = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def copy_tree(self, node):
        if node is None:
            return None
        new_node = TreeNode(node.info)
        new_node.left = self.copy_tree(node.left)
        new_node.right = self.copy_tree(node.right)
        return new_node

    def copy(self):
        new_tree = BinaryTree()
        new_tree.root = self.copy_tree(self.root)
        return new_tree

 
tree = BinaryTree()
tree.root = TreeNode(1)
tree.root.left = TreeNode(2)
tree.root.right = TreeNode(3)
tree.root.left.left = TreeNode(4)
tree.root.left.right = TreeNode(5)

copied_tree = tree.copy()

print("Cây ban đầu:")
# In cây ban đầu
def print_tree(node):
    if node is None:
        return
    print_tree(node.left)
    print(node.info, end=" ")
    print_tree(node.right)

print_tree(tree.root)
print("\nCây đã sao chép:")
# In cây đã sao chép
print_tree(copied_tree.root)
