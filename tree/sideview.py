import collections


def sideView(root):   #Level Order becauase we want the right most values of each level 
    q = collections.deque([root])  
    res = []

    for i in range(len(q)):

        while q:
            node = q.popleft()    

            if node:
                riteSide = None    #initially set to None 
                q.append(node.left)
                q.append(node.right)

            if riteSide:
                res.append(riteSide.val)   


    return res

        

            