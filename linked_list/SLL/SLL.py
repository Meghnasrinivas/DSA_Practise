class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__ (self):
        self.head = None

    def traversal(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            a=self.head
            while a is not None:
                print(a.data,end=' ')
                a=a.next
        #Insertion

    def insertion_at_beg(self,data):
        print()
        nb=Node(data)
        nb.next=self.head
        self.head=nb

    def insertion_at_end(self,data):
        print()
        ne=Node(data)
        a=self.head
        while a.next is not None:
            a=a.next
        a.next=ne

    def insertin_at_specific(self,position,data):
        print()
        npn=Node(data)
        a=self.head
        for i in range(1,position-1):
            a=a.next
        npn.next=a.next
        a.next=npn

    #Deletion
    def del_at_begi(self):
        print()
        a=self.head
        self.head=a.next
        a.next=None

    def del_at_end(self):
        print()
        prev=self.head
        a=self.head.next
        while a.next is not None:
            a=a.next
            prev=prev.next
        prev.next=None
        
    def del_at_specific(self,position):
        print()
        prev=self.head
        a=self.head.next
        for i in range(1,position-1):
            a=a.next
            prev=prev.next
        prev.next=a.next
        a.next=None


n1=Node(2)
sll=SLL()
sll.head=n1
n2=Node(5)
n1.next=n2
n3=Node(7)
n2.next=n3
n4=Node(9)
n3.next=n4
n5=Node(10)
n4.next=n5
n6=Node(15)
n5.next=n6
sll.traversal()   
sll.insertion_at_beg(1)
sll.traversal() 
sll.insertion_at_end(15)
sll.traversal()
sll.insertin_at_specific(3,17)
sll.traversal()
sll.del_at_begi()
sll.traversal()
sll.del_at_end()
sll.traversal()
sll.del_at_specific(4)
sll.traversal()