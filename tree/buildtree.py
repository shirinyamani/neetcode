class NodeTree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildtree(preorder,inorder):
    if not preorder or not inorder:
        return None 
    root = NodeTree(preorder[0])
    mid = inorder.index(preorder[0])

    root.left = buildtree(preorder[1:mid+1], inorder[:mid])
    root.right = buildtree(preorder[mid+1:], inorder[mid+1:])

    return root
