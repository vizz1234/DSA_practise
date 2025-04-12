#User function Template for python3

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
class Solution:
    def isLeaf(self, node):
        return not node.left and not node.right
    
    def leftBoundary(self, root):
        if not root:
            return
        curr = root
        while not self.isLeaf(curr):
            self.res.append(curr.data)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
    
    def leavesBoundary(self, root):
        curr = root
        while curr:
            if not curr.left:
                if not curr.right:
                    self.res.append(curr.data)
                curr = curr.right
            else:
                inorderPredecessor = curr.left
                while inorderPredecessor.right and inorderPredecessor.right != curr:
                    inorderPredecessor = inorderPredecessor.right
                if not inorderPredecessor.right:
                    inorderPredecessor.right = curr
                    curr = curr.left
                else:
                    if not inorderPredecessor.left:
                        self.res.append(inorderPredecessor.data)
                    inorderPredecessor.right = None
                    curr = curr.right
    
    def rightBoundary(self, root):
        if not root:
            return
        temp = []
        curr = root
        while not self.isLeaf(curr):
            temp.append(curr.data)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        temp[:] = temp[::-1]
        self.res.extend(temp)
                
    def boundaryTraversal(self, root):
        # Code here
        self.res = []
        if not self.isLeaf(root):
            self.res.append(root.data)
        self.leftBoundary(root.left)
        self.leavesBoundary(root)
        self.rightBoundary(root.right)
        
        return self.res
        




#{ 
 # Driver Code Starts
#Initial Template for Python 3

# function should return a list containing the boundary view of the binary tree
#{
#  Driver Code Starts
import sys

import sys

sys.setrecursionlimit(100000)
#Contributed by Sudarshan Sharma
from collections import deque


# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    #Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):

            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):

            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    t = 1
    for _ in range(0, t):
        s = '1 2 3 4 5 6 7 N N 8 9 N N N N'
        root = buildTree(s)
        obj = Solution()
        res = obj.boundaryTraversal(root)
        for i in res:
            print(i, end=" ")
        print('')
        print("~")

# } Driver Code Ends