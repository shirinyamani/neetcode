#counting the number of nodes, then initiate with a value rcount = 0 then got for comparing n getting the max/min
def goodpoints(root):
    if not root:
        return None
    
    def dfs(node, mxval):
        count = 0

        if node.val >= mxval:
            count += 1

        else: 0

        mxval = max(node.val, mxval)

        count += dfs(node.right)
        count += dfs(node.left)
        return count

    return dfs(root, root.val)