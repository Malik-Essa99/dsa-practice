## 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(root, val):
    def search(node):
        if node is None:
            return None

        if node.val == val:
            return node

        left_search = search(node.left)
        if left_search:
            if left_search.val == val:
                return left_search

        right_search = search(node.right)
        if right_search:
            if right_search.val == val:
                return right_search

        return None
    
    return search(root)

# Example usage
#       4
#      / \
#     2   7
#    / \
#   1   3

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

val_to_search = 2
result_node = searchBST(root, val_to_search)
if result_node:
    print("Node found with value:", result_node.val)
else:
    print("Node not found")
