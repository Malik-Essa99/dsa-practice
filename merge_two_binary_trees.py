## Merge Two Binary Trees
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# chat gpt's logic:
def mergeTrees(root1, root2):
    if root1 is None:
        return root2
    if root2 is None:
        return root1
    
    root = TreeNode(root1.val + root2.val)
    root.left = mergeTrees(root1.left, root2.left)
    root.right = mergeTrees(root1.right, root2.right)
    return root

# my logic:

# def mergeTrees(root1, root2):
#     if root1 is None and root2 is None:
#         return None

#     if root1 and root2:
#         root = TreeNode(root1.val + root2.val)
#         root.left = mergeTrees(root1.left, root2.left)
#         root.right = mergeTrees(root1.right, root2.right)
#     elif root1:
#         root = TreeNode(root1.val)
#         root.left = mergeTrees(root1.left, None)
#         root.right = mergeTrees(root1.right, None)
#     else:  # root2 is not None
#         root = TreeNode(root2.val)
#         root.left = mergeTrees(None, root2.left)
#         root.right = mergeTrees(None, root2.right)

#     return root



# Example usage
# Tree 1:      Tree 2:
#     1             2
#    / \           / \
#   3   2         1   3
#  /               \   \
# 5                 4   7

root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)

merged_root = mergeTrees(root1, root2)
