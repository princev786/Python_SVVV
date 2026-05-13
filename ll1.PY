class Node:
    data = 0
    next=None

    def __init__(self,d):
        self.data = d
    
class Solution:
    def createnode(self,d):
        newnode = Node(d)
        return newnode
    def addathead(self,head,d):
        newnode = self.createnode(d)
        if head == None:
            head = newnode
            return head
        newnode.next = head
        head = newnode
        return head
    
    def addattail(self,head,d):
        newnode = self.createnode(d)
        if head == None:
            head = newnode
            return head
        temp = head
        while temp.next!=None:
            temp = temp.next
        
        temp.next = newnode
        return head
    def addatN(self,head,d,n):
        newnode = self.createnode(d)
        if head == None:
            head = newnode
            return head
        temp = head
        if n==1:
            head = self.addathead(head,d)
            return head
        for i in range(n-2):
            temp = temp.next 
        newnode.next = temp.next
        temp.next = newnode
        return head
    def printlist(self,head):
        if head == None:
            print("List is Empty.")
            return
        temp = head
        while temp!=None:
            print(temp.data ,"->",end ="")
            temp = temp.next

    def deleteatatil(self,head):
        if head == None:
            return
        if head.next==None:
            return None
        temp = head
        while temp.next.next !=None:
            temp = temp.next
        temp.next = None
        return head

    def deletewithdata(self,head,key):
        if head == None or (head.next==None and head.data ==key):
            return None
        
        if head.data == key:
            return head.next
        
        prev = None
        curr = head

        while(curr!=None):
            if curr.data == key:
               prev.next = curr.next
               return head
            prev = curr
            curr = curr.next
        return head
    
    def findmiddlenode(self,head):
        if head == None :
            return -1
        if head.next == None:
            return
        slow = head
        fast = head

        while fast.next!=None and fast.next.next!=None :
            fast = fast.next.next 
            slow = slow.next 
        if fast.next==None:
            print(slow.data)
        else:
            print(slow.data,slow.next.data )

    #None<-10 <-20 <-30 <-40 <-50
        
    def reverseLL(self,head):
        prev = None
        curr = head #10
        while(curr!=None):
            fast = curr.next #None
            curr.next = prev #40
            prev = curr #50
            curr = fast #None
        return prev
    
    def reverseKnodes(self,head,k):
        prev = None
        curr = head
        while(curr!=None and k>0):
            fast = curr.next 
            curr.next = prev
            prev = curr
            curr = fast
            k-=1
        head.next = fast
        return prev
    
    def reversekgroups(self,head,c):
        if head==None:
            return
        prev = None
        curr = head
        fast = None
        k=c
        while(curr!=None and k>0):
            fast = curr.next 
            curr.next = prev
            prev = curr
            curr = fast
            k-=1
        
        head.next = self.reversekgroups(fast,c)
        return prev
    #10 20 30 40 50
    #30 20 10 40 50


if __name__ == "__main__":
    s = Solution()
    head = s.createnode(10)
    head = s.addathead(head,5)
    head = s.addathead(head,1)
    head = s.addattail(head,20)
    head = s.addattail(head,30) #1 5 10 20 30
    head = s.addatN(head,25,5)
    head = s.addatN(head,35,6)

    s.printlist(head)
    print()
    s.findmiddlenode(head)
    print()
    head = s.reverseLL(head)
    s.printlist(head)
    print()
    head = s.reverseKnodes(head,3)
    s.printlist(head)
    print()
    head = s.reversekgroups(head,3)
    s.printlist(head)


    
        

        
