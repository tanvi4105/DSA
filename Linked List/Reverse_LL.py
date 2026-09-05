class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return 
        
        temp=self.head
        while temp.next!=None:
            temp=temp.next

        temp.next=newnode    

    def display(self):
        if self.head is None:
            return
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end=" -> ")
                temp=temp.next
            print("None")

    def Reverse(self):
        if self.head is None:
            return
        prev=None
        curr=self.head   
        while curr:
            nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=nextnode
        self.head=prev
        
ll=LinkedList()
ll.insert(10) 
ll.insert(20) 
ll.insert(30) 
ll.insert(40)              
ll.display()
ll.Reverse()
ll.display()
