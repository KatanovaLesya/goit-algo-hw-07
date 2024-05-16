class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def find_max_value(root):
    if root is None:
        return None
    
    current_node = root
    while current_node.right is not None:
        current_node = current_node.right
    
    return current_node.value

# Створюємо дерево
#         10
#        /  \
#       5    20
#           /  \
#          15   30

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(30)

# Знаходимо найбільше значення
print(find_max_value(root))  
