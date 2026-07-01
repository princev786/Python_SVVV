
class Queue:
    st1 = []
    st2 = []
    top1=-1
    top2=-1

    def push(self,st,val):
        st.append(val)
    
    def pop(self,st):
        return st.pop()


    def enqueue(self,val):
        if len(self.st1)==0 and len(self.st2)!=0:
            for i in range(len(self.st2)-1,-1,-1):
                self.st1.append(self.st2.pop())
        self.st1.append(val)

    def dequeue(self):
        for i in range(len(self.st1)-1,-1,-1):
            self.st2.append(self.st1.pop())
        self.st2.pop()

