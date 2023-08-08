## Find a Corresponding Node of a Binary Tree in a Clone of That Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getTargetCopy(original, cloned, target):
    def _walk(node, val):
        if node is None:
            return None

        if node.val == val:
            return node

        left_result = _walk(node.left, val)
        if left_result:
            return left_result

        right_result = _walk(node.right, val)
        if right_result:
            return right_result

        return None

    result = _walk(cloned, target.val)
    return result

# Create an example tree
# Original tree:
#       1
#      / \
#     2   3
#        / \
#       4   5

original_root = TreeNode(1)
original_root.left = TreeNode(2)
original_root.right = TreeNode(3)
original_root.right.left = TreeNode(4)
original_root.right.right = TreeNode(5)

# Clone the original tree
cloned_root = TreeNode(1)
cloned_root.left = TreeNode(2)
cloned_root.right = TreeNode(3)
cloned_root.right.left = TreeNode(4)
cloned_root.right.right = TreeNode(5)

# Set the target node (e.g., target node is the node with value 3 in the original tree)
target_node = original_root.right

# Find the corresponding node in the cloned tree
cloned_target = getTargetCopy(original_root, cloned_root, target_node)

# Print the value of the cloned target node
print(cloned_target.val)
