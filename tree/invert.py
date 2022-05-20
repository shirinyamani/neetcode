class Tree:
    def __init__(self,value=0, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

def invert(root):
    if not root:
        return None
    
    #swap the children
    tmp = root.left
    root.left = root.right
    root.right = tmp

    #recursive on each of the side children
    invert(root.left)
    invert(root.right)

    return root 
