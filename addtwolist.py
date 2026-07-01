class Node:
    data = 0
    next = None

    def __init__(self,val):
        self.data = val

class Solution:
    @staticmethod
    def hascycle(head):
        slow = head
        fast = head

        while(fast!=None and fast.next!=None):
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True
        
        return False
    
    @staticmethod
    def startofcycle(head):
        slow = head
        fast = head

        while(fast!=None and fast.next!=None):
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                slow=head
                while(slow!=fast):
                    slow = slow.next
                    fast = fast.next
                return slow.data    
        return -1
            
    @staticmethod
    def addathead(head,val):
        newnode = Node(val)
        if head==None:
            head = newnode
        else:
            newnode.next = head
            head = newnode
        return head
    @staticmethod
    def reverseLL(head):
        prev = None
        curr = head #10
        while(curr!=None):
            fast = curr.next #None
            curr.next = prev #40
            prev = curr #50
            curr = fast #None
        return prev
    @staticmethod
    def addtwolist(head1,head2):
        if head1==None:
            return head2
        if head2==None:
            return head1
        
        ans = Node(-1)
        temp1 = Solution.reverseLL(head1)
        temp2 = Solution.reverseLL(head2)
        c=0
        while(temp1!=None and temp2!=None):
            sum = temp1.data + temp2.data +c
            ans = Solution.addathead(ans,sum%10)
            c = sum//10
            temp1 = temp1.next
            temp2 = temp2.next

        while(temp1!=None):
            sum = temp1.data +c
            ans = Solution.addathead(ans,sum%10)
            temp1 = temp1.next
            c = sum//10
        while(temp2!=None):
            sum = temp2.data +c
            ans = Solution.addathead(ans,sum%10)
            temp2 = temp2.next
            c = sum//10
        while c!=0:
            ans = Solution.addathead(ans,c%10)
            c = c//10
        return ans
    @staticmethod
    def printlist(head):
        if head == None:
            print("List is Empty.")
            return
        temp = head
        while temp!=None:
            print(temp.data ,"->",end ="")
            temp = temp.next
    
if __name__ == "__main__":
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next =head.next.next

    print(Solution.hascycle(head))
    print(Solution.startofcycle(head))

    # head1 = Node(7)
    # head1.next = Node(8)
    # head1.next.next = Node(6)
    # head1.next.next.next = Node(5)
    # head2 = Node(5)
    # head2.next = Node(7)
    # head2.next.next = Node(9)
    # head2.next.next.next = Node(8)

    # Solution.printlist(head1)
    # print()
    # Solution.printlist(head2)
    # print()
    # head3 = Solution.addtwolist(head1,head2)
    
    # temp3 = head3
    # while(temp3.next!=None):
    #     print(temp3.data, end="->")
    #     temp3 = temp3.next

    # print(None)
