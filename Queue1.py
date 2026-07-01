class Node:
    data = 0
    next = None
    def __init__(self,val):
        self.data = val
    
class Queue:
    size = 0
    front,rear = None,None

    def enqueue(self,val):
        newnode = Node(val)
        if self.rear==None:
            self.rear = newnode
            self.front = newnode
            self.size+=1
            return
        self.rear.next = newnode
        self.rear = newnode
        self.size+=1
    
    def dequeue(self):
        if self.front==None:
            return -1
        val = self.front.data 
        self.front = self.front.next
        self.size-=1
        return val           
    
    def peek(self):
        if self.front ==None:
            return -1
        return self.front.data
    
    def contains(self,key):
        if self.front ==None:
            return False
        temp = self.front
        while temp!=None:
            if temp.data == key:
                return True
            temp = temp.next
        return False
    
    def reverse(self):
        self.rear = self.front
        prev = None
        curr = self.front
        while curr!=None:
            agla = curr.next
            curr.next = prev
            prev = curr
            curr = agla
        
        self.front = prev

    def display(self):
        if self.front == None:
            return
        temp = self.front
        while temp!=None:
            print(temp.data ,end =" ")
            temp = temp.next
        
class Stack :
    def push(self,que,ele):
        que.enqueue(ele)

    def pop(self,que):
        temp = que.front
        while temp.next.next!=None:
            temp = temp.next
        val = temp.next.data
        temp.next = None
        que.rear = temp
        return val
    
    def display(self,que):
        if que.front == None:
            return
        temp = que.front
        s=""
        while temp!=None:
            s=str(temp.data) + " " +s
            temp = temp.next
        print(s)

    
if __name__ == "__main__":
    st = Stack()
    que = Queue()
    st.push(que,10)
    st.push(que,20)
    st.push(que,30)
    st.push(que,40)
    st.push(que,60)

    print(st.pop(que))
    st.display(que)


    