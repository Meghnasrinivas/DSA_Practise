class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None

    def reverse(self):
        prev = None
        curr = self.head

        while curr is not None:
            next_node = curr.next   # Step 1: store next
            curr.next = prev        # Step 2: reverse link
            prev = curr             # Step 3: move prev
            curr = next_node        # Step 4: move curr

        self.head = prev


# Creating list: 1 → 2 → 3 → 4
sll = SLL()
sll.head = Node(1)
sll.head.next = Node(2)
sll.head.next.next = Node(3)
sll.head.next.next.next = Node(4)

print("Before reverse:")
a = sll.head
while a:
    print(a.data, end=' ')
    a = a.next

sll.reverse()

print("\nAfter reverse:")
a = sll.head
while a:
    print(a.data, end=' ')
    a = a.next