from binarytree import Node, build, tree
root = Node(6)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(5)

print("Binary Tree:", root)
print("List of Nodes:", list(root))
print("Inoder of node:", root.inorder)
print('Size of tree :', root.size) 
print('Height of tree :', root.height) 
  
# Get all properties at once 
print('Properties of tree : \n', root.properties) 

nodes = [5, 4, 7, 2, None, None, 8, 3 , 0]
binary_tree = build(nodes)
print("Binary Tree:", binary_tree)

print('\nList from binary tree :',  
      binary_tree.values) 

binary_tree = tree(height=4, is_perfect=True)
print("Binary Tree:", binary_tree)
print("List of Nodes:", list(binary_tree))