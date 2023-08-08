## Range Sum of BST

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rangeSumBST(root, low, high):
    def sum_of_range(node):
        if node is None:
            return 0
        
        if low <= node.val <= high:
            return node.val + sum_of_range(node.left) + sum_of_range(node.right)
        elif node.val < low:
            return sum_of_range(node.right)
        else:
            return sum_of_range(node.left)

    return sum_of_range(root)

# Create an example BST
#      10
#     /  \
#    5   15
#   / \    \
#  3   7    18

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

low = 7
high = 15
result = rangeSumBST(root, low, high)
print("Range sum:", result)  # This should output 32
