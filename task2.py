class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def find_min_value(root):
    if root is None:
        return None
    
    current_node = root
    while current_node.left is not None:
        current_node = current_node.left
    
    return current_node.value

# Створюємо дерево
#         10
#        /  \
#       5    20
#      /    /  \
#     1    15   30

root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(1)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(30)

# Знаходимо найменше значення
print(find_min_value(root))  
