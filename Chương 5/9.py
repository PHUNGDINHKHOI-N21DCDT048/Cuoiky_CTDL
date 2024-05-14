class TreeNode:
    def __init__(self, value):
        self.info = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def is_subtree_util(self, s, t):
        if s is None:
            return False
        if self.is_identical_trees(s, t):
            return True
        return self.is_subtree_util(s.left, t) or self.is_subtree_util(s.right, t)

    def is_identical_trees(self, s, t):
        if s is None and t is None:
            return True
        if s is not None and t is not None:
            return (s.info == t.info and
                    self.is_identical_trees(s.left, t.left) and
                    self.is_identical_trees(s.right, t.right))
        return False

    def is_subtree(self, other_tree):
        return self.is_subtree_util(self.root, other_tree.root)

tree1 = BinaryTree()
tree1.root = TreeNode(3)
tree1.root.left = TreeNode(4)
tree1.root.right = TreeNode(5)
tree1.root.left.left = TreeNode(1)
tree1.root.left.right = TreeNode(2)

tree2 = BinaryTree()
tree2.root = TreeNode(4)
tree2.root.left = TreeNode(1)
tree2.root.right = TreeNode(2)

tree3 = BinaryTree()
tree3.root = TreeNode(4)
tree3.root.left = TreeNode(1)
tree3.root.right = TreeNode(2)
tree3.root.left.left = TreeNode(0)

if tree1.is_subtree(tree2):
    print("Cây 2 là cây con của cây 1.")
else:
    print("Cây 2 không phải là cây con của cây 1.")

if tree1.is_subtree(tree3):
    print("Cây 3 là cây con của cây 1.")
else:
    print("Cây 3 không phải là cây con của cây 1.")
