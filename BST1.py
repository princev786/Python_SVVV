class Node:
    data = 0
    left = None
    right= None
    def __init__(self,data):
        self.data = data
class BST:
    def buildTree(self,lst):
        root = Node(lst[0])
        que=[]
        que.append(root)
        j=1
        while len(que)!=0 and j<len(lst):
            curr = que[0]
            del que[0]
            if lst[j]!=None:
                curr.left = Node(lst[j])
                que.append(curr.left)
            if lst[j+1]!=None:
                curr.right = Node(lst[j+1])
                que.append(curr.right)
            j+=2
        return root

    def insert(self,root,key):
        que = []
        que.append(root)
        while len(que)!=0:
            curr = que[0]
            del que[0]
            if curr.data <= key:
                if curr.right !=None:
                    que.append(curr.right)
                else:
                    curr.right = Node(key)
                    return root

            if curr.data > key:
                if curr.left !=None:
                    que.append(curr.left)
                else:
                    curr.left = Node(key)
                    return root
        return root   


    def inOrder(self,root):
        if root == None:
            return
        self.inOrder(root.left)
        print(root.data,end = " ")
        self.inOrder(root.right)
    def preOrder(self,root):
        if root==None:
            return
        print(root.data,end=" ")

        self.preOrder(root.left)
        self.preOrder(root.right)
    def postOrder(self,root):
        if root==None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data,end=" ")
    
    def levelOrder(self,root):
        if root==None:
            return
        que=[]
        que.append(root)
        while len(que)!=0:
            curr=que[0]
            print(curr.data,end=" ")
            del que[0]
            if curr.left!=None:
                que.append(curr.left)
            if curr.right!=None:
                que.append(curr.right)

    def rightNode(self,node):
        if node == None:
            return node
        root = node
        while root.right !=None:
            root= root.right
        return root
   
    def dlt(self,root,key):
        temp = self.rightNode(root.left)
        que=[]
        que.append(root)
        keyNode = None
        while len(que)!=0:
            curr = que[0]
            del que[0]
            if curr.data == key:
                keyNode = curr
                break
            if curr.left!=None:
                que.append(curr.left)
            if curr.right!=None:
                que.append(curr.right)

        if keyNode !=None:
            keyNode.data = temp.data
            return self.dltleaf(root,temp)
    
    def dltleaf(self,root,temp):
        que = []
        que.append(root)
        while len(que)!=0:
            curr = que[0]
            del que[0]
            if curr.left ==temp:
                curr.left=None
            else:
                if curr.left!=None:
                    que.append(curr.left)
            if curr.right ==temp:
                curr.right=None
            else:
                if curr.right!=None:
                    que.append(curr.right)
            
        return root

    def lca(self,root,p,q):
        if root == None:
            return None
        if root.data == p or root.data == q:
            return root
        left = self.lca(root.left,p,q)
        right = self.lca(root.right,p,q)
        if left and right :
            return root
        if left :
            return left
        else:
            return right
        



oak = BST()
root = oak.buildTree([50,40,60,20,45,55,70])     
oak.levelOrder(root)
root = oak.dlt(root,50)
print()
oak.levelOrder(root)
        