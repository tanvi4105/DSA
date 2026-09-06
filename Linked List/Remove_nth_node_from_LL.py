class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def Remove_nth_node(self,n):
        if self.head is None:
            return
        if n==1:
            self.head=self.head.next
            return
        
        cnt=1
        prev=None
        curr=self.head
        while curr!=None:
            if cnt==n:
                prev.next=curr.next
                return
            prev=curr    
            curr=curr.next
            cnt+=1
        
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end=" -> ")       
            temp=temp.next
        print("None")   
    
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

ll=LinkedList()
ll.head=head
ll.Remove_nth_node(1)
ll.display()