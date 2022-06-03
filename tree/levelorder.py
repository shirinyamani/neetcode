from collections import deque


#Solution 1

def levelorder(root): #idea is to have the node values and just add them to the list
    q = deque()
    res = []

    if root: q.append(root)

    while q:
        val = []

        for i in range(len(q)):

            node = q.popleft()

            val.append(node.val)

            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

        res.append(val)

    return res

#Solution 2

def levelorder1(root):
    res, q = [], deque([(root,0)])

    while q:

        node, level = q.popleft()
        if node:
            if len(res) < level +1:
                res.append([])
                res[level].append(node.val)
                q.append(node.left, level+1)
                q.append(node.right, level+1)

    return res





