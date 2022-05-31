class Tree:
    def __init__(self,value= None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def isBalanced(self, root):

        def dfs(root):
            if not root:
                return [True]

            left_h = dfs(root.left)
            right_h = dfs(root.right)

            balanced= (left_h[0] and right_h[0] and
                            abs(left_h[1]-right_h[1] <1))

            return [balanced, 1 + max(left_h[1], right_h[1])]
        return dfs(root)[0]

if __name__ =="__main__":
    print(isinstance([[3,9,20,None,None,15,7]]))