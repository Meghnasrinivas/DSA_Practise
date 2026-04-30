class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None

    def is_palindrome(self):
        # Step 1: Find the middle of the linked list
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

        # Step 2: Reverse the second half of the linked list
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Step 3: Compare the first half and the reversed second half
        left = self.head
        right = prev  # prev is now the head of the reversed second half

        while right:  # Only need to compare until the end of the shorter half
            if left.data != right.data:
                return False
            left = left.next
            right = right.next

        return True
# Creating list: 1 → 2 → 3 → 2 → 1
sll = SLL()
sll.head = Node(1)
sll.head.next = Node(2)
sll.head.next.next = Node(3)
sll.head.next.next.next = Node(2)
sll.head.next.next.next.next = Node(1)
print("Is the linked list a palindrome?", sll.is_palindrome())
# Creating list: 1 → 2 → 3 → 4
sll2 = SLL()
sll2.head = Node(1)
sll2.head.next = Node(2)
sll2.head.next.next = Node(3)
sll2.head.next.next.next = Node(4)
print("Is the linked list a palindrome?", sll2.is_palindrome())