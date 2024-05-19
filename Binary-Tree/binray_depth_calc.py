class TreeNode:
    def __init__(self, key=0, left=None, right=None):
        self.key = key # This is the value stored in the node
        self.left = left # This is the left child of the node
        self.right = right # This is the right child of the node

def max_depth(root: TreeNode)-> int:
    if root is None:
        return 0
    
    else:
        left_depth = max_depth(root.left)
        right_depth = max_depth(root.right)

        return max(left_depth, right_depth) + 1
    
if __name__ == "__main__":
    # Constructing the example binary tree
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

    print("Maximum depth of the binary tree is:", max_depth(root))  # Output should be 3