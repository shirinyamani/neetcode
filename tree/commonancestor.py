def LCA(root,p,q): #use the BST concept
    node = root.val
    #3 scenarios: 1) both nodes are less than the given node ---> search in left 2) both nodes are bigger ---> search in rigght 3) nodes are in defferent sides then return root itself!
    if p.val < node and q.val<node:
        return LCA(root.left, p, q)

    elif q.val > node and p.val > node:
        return LCA(root.right, p, q)

    else:
        return root 

    