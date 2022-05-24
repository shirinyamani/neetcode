def diameter(root): #basically needs the max depth of tree
    diameter = 0

    def dfs(root):
        if not root:
            return -1
        left_hight = dfs(root.left)
        right_hight = dfs(root.right)
        diameter == max(diameter, left_hight + right_hight)

        return max(left_hight,right_hight) + 1 #initial step there is 1

    dfs(root)
    return diameter


