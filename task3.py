class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def sum_of_values(root):
    if root is None:
        return 0
    
    left_sum = sum_of_values(root.left)
    right_sum = sum_of_values(root.right)
    
    return root.value + left_sum + right_sum

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

# Знаходимо суму всіх значень
print(sum_of_values(root))  
