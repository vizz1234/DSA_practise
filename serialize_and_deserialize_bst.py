#User function Template for python3

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    #Function to serialize a tree and return a list containing nodes of tree.
    def serialize(self, root):
        #code here
        self.btArr = []
        def recurPreOrder(root):
            if not root:
                self.btArr.append(-1)
                return None
            
            self.btArr.append(root.data)
            root.left = recurPreOrder(root.left)
            root.right = recurPreOrder(root.right)
        
        recurPreOrder(root)
        return self.btArr
    
    #Function to deserialize a list and construct the tree.   
    def deSerialize(self, arr):
        #code here
        self.btArr[:] = arr[:]
        self.idx = 0
        def recurPreOrder():
            if self.btArr[self.idx] == -1:
                self.idx += 1
                return None
            
            root = Node(self.btArr[self.idx])
            self.idx += 1
            root.left = recurPreOrder()
            root.right = recurPreOrder()
            
            return root
        
        return recurPreOrder()