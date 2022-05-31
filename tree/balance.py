class Tree(object):
    def __init__(self,value= 0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self,root):
        if not root:
            return True
        self.ans = True

        def dfs(root): #it returns the height of each subtree
            left_h = dfs(root.left)
            right_h = dfs(root.right)

            if abs(left_h - right_h) > 1:
                self.ans = False

            return 1+ max(left_h,right_h)  #height of the left n right subtree

        dfs(root)
        return self.ans


       

if __name__ =="__main__":
    print(Solution.isBalanced([[3,9,20,None,None,15,7]]))