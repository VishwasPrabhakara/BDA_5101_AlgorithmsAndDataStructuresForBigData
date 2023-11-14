class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def count_leaf_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)

def count_total_nodes(root):
    if root is None:
        return 0
    return 1 + count_total_nodes(root.left) + count_total_nodes(root.right)

def display_all_values(root):
    if root is not None:
        print(root.data, end=' ')
        display_all_values(root.left)
        display_all_values(root.right)

if __name__ == '__main__':
    # Example binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print("Number of leaf nodes:", count_leaf_nodes(root))
    print("Total number of nodes in the tree:", count_total_nodes(root))

    print("Values of all nodes:")
    display_all_values(root)
