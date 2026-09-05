class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def find_middle_of_LL(self,head):
        slow=head
        fast=head
        while fast and fast.next and slow:
            slow=slow.next
            fast=fast.next.next

        return slow    

    
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

ll=LinkedList()
middle=ll.find_middle_of_LL(head)
print("Middle of linked list:",middle.data)    