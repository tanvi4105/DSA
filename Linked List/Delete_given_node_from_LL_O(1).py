class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def delete_node(self,Node):
        Node.data=Node.next.data
        Node.next=Node.next.next

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

ll=LinkedList()
ll.head=head
ll.delete_node(head.next.next)
ll.display()