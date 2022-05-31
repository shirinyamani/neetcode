from collections import deque


class Tree:
    def __init__(self, value=0, left=None,right=None):
        self.left = left
        self.right = right
        self.value = value


    def maxdep(self, root): #mx depth actually means the number of levels untill null point, right?
        level = 0
        q = deque([root]) #means getting out, instead of using pop 

        while q: #FIFO
            for i in range(len(q)):
                node = q.popleft() 

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            level += 1

        return level


if __name__ == "__main__":
    print(maxdep([3,9,20,None,None,15,7]))

    