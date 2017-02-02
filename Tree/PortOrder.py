"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def postOrder(root):
    
    if (root != None):
        data = root.data
        left = root.left
        right = root.right
        postOrder(left)
        postOrder(right)
        print(data,end=" ")
        
        
