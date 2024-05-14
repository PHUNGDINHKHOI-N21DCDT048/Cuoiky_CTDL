class TreeNode:
    def __init__(self, value):
        self.info = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def is_avl_util(self, node):
        if node is None:
            return True
        
        balance = self.balance_factor(node)
        if balance > 1 or balance < -1:
            return False
        
        return (self.is_avl_util(node.left) and self.is_avl_util(node.right))

    def is_avl(self):
        return self.is_avl_util(self.root)


avl_tree = AVLTree()
avl_tree.root = TreeNode(1)
avl_tree.root.left = TreeNode(2)
avl_tree.root.right = TreeNode(3)
avl_tree.root.left.left = TreeNode(4)
avl_tree.root.left.right = TreeNode(5)
avl_tree.root.right.right = TreeNode(6)

if avl_tree.is_avl():
    print("Cây là một cây cân bằng AVL.")
else:
    print("Cây không phải là một cây cân bằng AVL.")
