class TreeNode:
    def __init__(self, value):
        self.info = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def count_intermediate_nodes(self, node):
        if node is None or (node.left is None and node.right is None):
            return 0
        return 1 + self.count_intermediate_nodes(node.left) + self.count_intermediate_nodes(node.right)

    def intermediate_nodes_count(self):
        if self.root is None:
            return 0
        return self.count_intermediate_nodes(self.root)


tree = BinaryTree()
tree.root = TreeNode(1)
tree.root.left = TreeNode(2)
tree.root.right = TreeNode(3)
tree.root.left.left = TreeNode(4)
tree.root.left.right = TreeNode(5)
tree.root.right.right = TreeNode(6)

print("Số nút trung gian của cây là:", tree.intermediate_nodes_count())
