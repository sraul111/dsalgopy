class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


#I LeRoRi  Inorder
#Pr RoLeRi PreOrder
#Po LeRiRo PostOrder    

def printInorder(root):
    if root:
        #print(f"Root val: {root.val}")
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)


def printPreorder(root):
    if root:
        print(root.val),
        printPreorder(root.left)
        printPreorder(root.right)



def printPostorder(root):

    if root:

       # print(f"Root val: {root.val}")
        # First recur on left child
        printPostorder(root.left)

        # the recur on right child
        printPostorder(root.right)

        # now print the data of node
        print(root.val),       



# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Inorder traversal of binary tree is")
printPostorder(root)