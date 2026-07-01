class Node:
    data =0
    left= None
    right= None

    def __init__(self,val):
        self.data = val

class Tree:

    def BuildTree(self,lst):
        root = Node(lst[0])
        que = [] 
        que.append(root)
        j=1
        while(len(que)!=0 and j<len(lst)):
            curr = que[0]
            del que[0]
            if lst[j]!=None:
                newnode = Node(lst[j])
                curr.left = newnode
                que.append(newnode)
            if lst[j+1]!=None:
                newnode = Node(lst[j+1])
                curr.right = newnode
                que.append(newnode)
            j = j+2
        return root

    def preOrder(self,root):
        if root == None:
            return
        print(root.data ,end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self,root):
        if root==None:
            return
        self.inOrder(root.left)
        print(root.data ,end =" ")
        self.inOrder(root.right)
        
    def postOrder(self,root):
        if root == None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data ,end =" ")

    def levelorder(self,root):
        if root == None:
            return
        que =[]
        que.append(root)
        while len(que)!=0:
            curr = que[0]
            print(curr.data ,end =" ")
            del que[0]
            if curr.left!=None:
                que.append(curr.left)
            if curr.right!=None:
                que.append(curr.right)

    def height(self,root):
        if root == None:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)

        return 1+max(left,right)
    m=0
    def diameter(self,root):
        if root==None:
            return 0
        left  = self.diameter(root.left)
        right = self.diameter(root.right)

        self.m= max(self.m,left+right)

        return 1+max(left,right)
    
    c = 0
    def countnodes(self,root):
        if root == None:
            return 
        self.c+=1
        self.countnodes(root.left)
        self.countnodes(root.right)

    def isEqual(self,root1,root2):
        if root1==None and root2==None:
            return True
        if root1==None or root2==None:
            return False
        if root1.data != root2.data:
            return False

        return root1.data==root2.data and self.isEqual(root1.left,root2.left) and root1.data==root2.data and self.isEqual(root1.right, root2.right)
    
    def isMirror(self,root1,root2):
        if root1==None and root2==None:
            return True
        if root1==None or root2==None:
            return False
        if root1.data != root2.data:
            return False
        
        return root1.data == root2.data and self.isMirror(root1.left,root2.right) and self.isMirror(root1.right, root2.left)
    
    def dlt(self,root,key):
        if root==None:
            return root
        que=[]
        que.append(root)
        keyNode=None
        temp=None
        while len(que)!=0:
            curr = que[0]
            temp = curr
            del que[0]
            if curr.data == key:
                keyNode = curr
            if curr.left!=None:
                que.append(curr.left)
            if curr.right!=None:
                que.append(curr.right)

        if keyNode != None:
            keyNode.data = temp.data
            return self.dltLastNode(root,temp)
        return root  

    def dltLastNode(self,root,temp):
        que = []
        que.append(root)
        while len(que)!=0:
            curr = que[0]
            del que[0]
            if curr.left == temp:
                curr.left = None
            else:
                if curr.left!=None:
                    que.append(curr.left)
            if curr.right == temp:
                curr.right = None
            else:
                if curr.right!=None:
                    que.append(curr.right)
        return root
            


if __name__ == "__main__":
    mango = Tree()

    tree = mango.BuildTree([10,20,30,40,None,60,70])

    tree2 = Node(10)
    tree2.left = Node(20)
    tree2.left.left = Node(40)
    tree2.right = Node(30)
    tree2.right.left = Node(60)
    tree2.right.right = Node(70)

    mango.levelorder(tree)
    print()
    mango.dlt(tree,20)
    mango.levelorder(tree)
    # mango.countnodes(tree)
    # print(mango.c)

    # mango.diameter(tree)
    # print(mango.m+1)
    # print(mango.height(tree))

    # mango.preOrder(tree)
    # mango.postOrder(tree)
    # mango.levelorder(tree)

