from collections import deque
from logging import root


def subTree(s,t):

    def is_same(r1,r2):
        if r1 is None and r2 is None: 
            return True

        if r1 is None or r2 is None:
            return False

        else:
            if r1.val == r2.val: #if the roots are the same then go n check whether the children are EXACTLY the same!
                return is_same(r1.left, r2.left) and is_same(r1.right, r2.right)
        return False

    #to traverse thro the tree n check all nodes
    q = deque([s]) 
    while q:
        node = q.popleft()
        if is_same(node, t):
            return True
        else:
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

        return False
