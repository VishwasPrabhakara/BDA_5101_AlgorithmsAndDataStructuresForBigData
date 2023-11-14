class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create_binary_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    return root

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.data, end=' ')
        inorder_traversal(node.right)

def preorder_traversal(node):
    if node:
        print(node.data, end=' ')
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.data, end=' ')

if __name__ == '__main__':
    root = create_binary_tree()

    print("Inorder Traversal:")
    inorder_traversal(root)

    print("\n\nPreorder Traversal:")
    preorder_traversal(root)

    print("\n\nPostorder Traversal:")
    postorder_traversal(root)
