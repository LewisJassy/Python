class TreeNode:
    def __init__(self, key=0, left=None, right=None):
        self.key = key # This is the value stored in the node
        self.left = left # This is the left child of the node
        self.right = right # This is the right child of the node

def max_depth(root: TreeNode)-> int:
    if root is None: # check if root is empty or not
        return 0 # return 0 if root is empty
    
    else:
        left_depth = max_depth(root.left) # recursively call the function to get the left depth
        right_depth = max_depth(root.right) # recursively call the function to get the right depth

        return max(left_depth, right_depth) + 1 # return the maximum depth of the tree
    
if __name__ == "__main__":
    # Constructing the example binary tree
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

    print("Maximum depth of the binary tree is:", max_depth(root))  # Output should be 3