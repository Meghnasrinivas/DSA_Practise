class Node:
    def __init__ (self,data):
        self.data = data
        self.prev=None
        self.next = None

class DLL:
    def __init__ (self):
        self.head = None

    def forward_traversal(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            a=self.head
            while a is not None:
                print(a.data,end=' ')
                a=a.next
    
    def backward_traversal(self):
        print()
        if self.head is None:
            print('Linked list is empty')
        else:
            a=self.head
            while a.next is not None:
                a=a.next
            while a is not None:
                print(a.data,end=' ')
                a=a.prev
             
            #Insertion
    def insertion_at_begin(self,data):
        print()
        nb=Node(data)
        a=self.head
        a.prev=nb
        nb.next=a
        self.head=nb
    
    def insertion_at_end(self,data):
        print()
        ne=Node(data)
        a=self.head
        while a.next is not None:
            a=a.next
        a.next=ne
        ne.prev=a
    
    def insertion_at_specific(self,position,data):
        print()
        npn=Node(data)
        a=self.head
        for i in range(1,position-1):
            a=a.next
        npn.prev=a
        npn.next=a.next
        a.next.prev=npn
        a.next=npn

       #Deletion
    def delete_at_begin(self):
        print()
        a=self.head
        self.head=a.next
        a.next=None
        self.head.prev=None

    def delete_at_end(self):
        print()
        a=self.head.next
        before=self.head
        while a.next is not None:
            a=a.next
            before=before.next
        a.prev=None
        before.next=None
    
    def delete_at_specific(self,position):
        print()
        a=self.head.next
        before=self.head
        for i in range(1,position-1):
            a=a.next
            before=before.next
        before.next=a.next
        a.next.prev=before
        a.next=None
        a.prev=None


n1=Node(2)
dll=DLL()
dll.head=n1
n2=Node(3)
n2.prev=n1
n1.next=n2
n3=Node(4)
n3.prev=n2
n2.next=n3
n4=Node(5)
n4.prev=n3
n3.next=n4
n5=Node(6)
n5.prev=n4
n4.next=n5
n6=Node(7)
n6.prev=n5
n5.next=n6
dll.forward_traversal()
dll.backward_traversal()
dll.insertion_at_begin(8)
dll.forward_traversal()
dll.backward_traversal()
dll.insertion_at_end(9)
dll.forward_traversal()
dll.insertion_at_specific(4,10)
dll.forward_traversal()
dll.delete_at_begin()
dll.forward_traversal()
dll.delete_at_end()
dll.forward_traversal()
dll.delete_at_specific(4)
dll.forward_traversal()