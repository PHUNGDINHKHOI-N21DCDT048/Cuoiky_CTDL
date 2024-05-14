class TreeNode:
    def __init__(self, value):
        self.info = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def is_identical_trees(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is not None and node2 is not None:
            return (node1.info == node2.info and
                    self.is_identical_trees(node1.left, node2.left) and
                    self.is_identical_trees(node1.right, node2.right))
        return False

    def compare_trees(self, other_tree):
        return self.is_identical_trees(self.root, other_tree.root)

tree1 = BinaryTree()
tree1.root = TreeNode(1)
tree1.root.left = TreeNode(2)
tree1.root.right = TreeNode(3)

tree2 = BinaryTree()
tree2.root = TreeNode(1)
tree2.root.left = TreeNode(2)
tree2.root.right = TreeNode(3)

tree3 = BinaryTree()
tree3.root = TreeNode(1)
tree3.root.left = TreeNode(2)
tree3.root.right = TreeNode(4)

if tree1.compare_trees(tree2):
    print("Cây 1 và cây 2 là giống nhau.")
else:
    print("Cây 1 và cây 2 không giống nhau.")

if tree1.compare_trees(tree3):
    print("Cây 1 và cây 3 là giống nhau.")
else:
    print("Cây 1 và cây 3 không giống nhau.")
