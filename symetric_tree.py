## Symemetric tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root):
    def is_mirror(left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        
        return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)
    
    if root is None:
        return True
    
    return is_mirror(root.left, root.right)

# Example usage
# Symmetric tree:
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3

symmetric_tree = TreeNode(1)
symmetric_tree.left = TreeNode(2)
symmetric_tree.right = TreeNode(2)
symmetric_tree.left.left = TreeNode(3)
symmetric_tree.left.right = TreeNode(4)
symmetric_tree.right.left = TreeNode(4)
symmetric_tree.right.right = TreeNode(3)

result = isSymmetric(symmetric_tree)  # Should return True
print(result)
