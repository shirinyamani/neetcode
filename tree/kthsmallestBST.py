#reccursive approach
def inorder(root,k):

    def helper(root):
        return inorder(root.left) + [root.val] + inorder(root.right) if root else []

    return helper(root)[k-1]


# Iteretive Approach
def inorder(root,k):
    stack = []

    while True:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        if not k:
            return root.val

        root = root.right