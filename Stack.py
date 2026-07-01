class Node:
    data = 0
    next = None

    def __init__(self,val):
        self.data = val

class Stack:
    top=None
    size =0
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self,top,val):
        newnode = Node(val)
        if self.top==None:
            self.top = newnode
        else:
            newnode.next = self.top
            self.top = newnode
        self.size +=1
        return self.top
    
    def pop(self,top):
        if self.top==None:
            print("stack is underflow")
            return self.top
        temp = self.top
        self.top = self.top.next
        return temp
    
    def peek(self,top):
        if self.top==None:
            return -1
        return self.top.data
    
    def reverse(self,top):
        turtle = None
        curr = self.top
        while curr!=None:
            hare = curr.next 
            curr.next = turtle
            turtle = curr
            curr = hare
        self.top = turtle
    
    def contains(self,top,key):
        if self.top==None:
            return False
        temp = self.top
        while temp!=None:
            if temp.data == key:
                return True
            temp = temp.next
        return False
    
    def merge(self,st1,st2):
        if st1.top==None:
            return st2
        if st2.top==None:
            return st1

        top2 = st2.reverse(st2) 
        temp = top2
        while temp!=None:
            node = temp.pop(temp)
            st1.push(st1,node.data)
            temp = temp.next
        return st1
    
    def display(self,top):
        if self.top==None:
            return
        temp = self.top
        while temp!=None:
            print(temp.data,end =" ")
            temp = temp.next
    
    def middleofstack(self,top):
        slow = self.top
        fast = self.top

        while(fast.next != None and fast.next.next != None):
            slow = slow.next 
            fast = fast.next.next
        return slow
            
if __name__=="__main__":
    s = Stack()
    s.push(s.top,10)    
    s.push(s.top,20)    
    s.push(s.top,30)    
    s.push(s.top,40)    
    s.push(s.top,50) 

    s2 = Stack()
    s2.push(s2.top,12)    
    s2.push(s2.top,24)    
    s2.push(s2.top,36)    
  
    
    s3 = Stack()
    s2.display(s2.top)

    s3 = s.merge(s,s2)
    s3.display(s3.top)
    # s.display(s.top)
    # s.pop(s.top)
    # print()
    # s.display(s.top)
    # print()
    # print(s.peek(s.top))

    # print()
    # s.reverse(s.top)
    # s.display(s.top)

    # print(s.contains(s.top,70))
    
    # print(s.middleofstack(s.top).data)

    
    # s3.display(s3.top)
    # s.display(s1)


