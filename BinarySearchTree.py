
# Binary Search Tree is a node-based binary tree data structure that has the following properties:

# The left subtree of a node contains only nodes with keys lesser than the node's key.
# The right subtree of a node 

# SEARCHING Element
# 1. Start from the root.
# 2. Compare the searching element with root, if less than root, then recurse for left,
#    else recurse for right.
# 3. if the element to search is found anywhere,return true, else return false.     

# A utility function to search a given key in BST
def search(root,key):

    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root
    
    # Key is greater than root's key
    if root.val < key:
        return search(root.right,key)
    
    # Key is smaller than root's key
    return search(root.left,key)
