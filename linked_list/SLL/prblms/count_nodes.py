class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None

    def count_nodes(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count
# Creating list: 1 → 2 → 3 → 4
sll = SLL()
sll.head = Node(1)
sll.head.next = Node(2)
sll.head.next.next = Node(3)
sll.head.next.next.next = Node(4)
print("Number of nodes in the linked list:", sll.count_nodes())