class TreeNode:
    def __init__(self, value):
        self.info = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def is_bst_util(self, node, min_val, max_val):
        if node is None:
            return True
        
        if node.info < min_val or node.info > max_val:
            return False
        
        return (self.is_bst_util(node.left, min_val, node.info - 1) and
                self.is_bst_util(node.right, node.info + 1, max_val))

    def is_bst(self):
        return self.is_bst_util(self.root, float("-inf"), float("inf"))

tree = BinaryTree()
tree.root = TreeNode(4)
tree.root.left = TreeNode(2)
tree.root.right = TreeNode(6)
tree.root.left.left = TreeNode(1)
tree.root.left.right = TreeNode(3)
tree.root.right.right = TreeNode(7)

if tree.is_bst():
    print("Cây là một cây nhị phân tìm kiếm (BST).")
else:
    print("Cây không phải là một cây nhị phân tìm kiếm (BST).")
