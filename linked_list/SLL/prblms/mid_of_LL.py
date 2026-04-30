class Node :
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None

    def mid(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data
# Creating list: 1 → 2 → 3 → 4 → 5
sll = SLL()
sll.head = Node(1)
sll.head.next = Node(2)
sll.head.next.next = Node(3)
sll.head.next.next.next = Node(4)
sll.head.next.next.next.next = Node(5)
sll.head.next.next.next.next.next = Node(6)
print("Middle element:", sll.mid())