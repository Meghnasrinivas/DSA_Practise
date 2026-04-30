class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None

    def merge_sorted(self, head1, head2):
        dummy = Node(0)  # Dummy node to simplify edge cases
        tail = dummy

        while head1 and head2:
            if head1.data < head2.data:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next

        # Attach the remaining nodes, if any
        if head1:
            tail.next = head1
        elif head2:
            tail.next = head2

        return dummy.next  # The merged list starts from dummy.next
# Creating first sorted linked list: 1 → 3 → 5
sll = SLL()
sll.head = Node(1)
sll.head.next = Node(3)
sll.head.next.next = Node(5)
# Creating second sorted linked list: 2 → 4 → 6
sll2 = SLL()
sll2.head = Node(2)
sll2.head.next = Node(4)
sll2.head.next.next = Node(6)
# Merging the two sorted linked lists
merged_head = sll.merge_sorted(sll.head, sll2.head)
# Printing the merged linked list
print("Merged sorted linked list:")
current = merged_head
while current:
    print(current.data, end=' ')
    current = current.next

    