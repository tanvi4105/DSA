class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def merge(self,list1,list2):
        dummy_node = Node(-1)
        temp = dummy_node

        while list1 is not None and list2 is not None:
            if list1.data<=list2.data:
                temp.next=list1
                list1=list1.next
            else:
                temp.next=list2
                list2=list2.next
            temp=temp.next

        if list1 is not None:
            temp.next=list1
        else:
            temp.next=list2
           
        return dummy_node.next

    def display(self,head):
        temp=head
        while temp!=None:
            print(temp.data,end=" -> ")       
            temp=temp.next
        print("None")                   

        
list1 = Node(1)
list1.next = Node(3)
list1.next.next = Node(5)

list2 = Node(2)
list2.next = Node(4)
list2.next.next = Node(6)

ll=LinkedList()
print("First sorted linked list: ",end="")
ll.display(list1)

print("Second sorted linked list: ", end="")
ll.display(list2)

merged_list = ll.merge(list1, list2)

print("Merged sorted linked list: ", end="")
ll.display(merged_list)

