class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    # Count nodes
    def count_nodes(self):
        count = 0
        a = self.head   # temp pointer

        while a is not None:
            count = count + 1
            a = a.next

        return count

    # Sum of nodes
    def sum_nodes(self):
        total = 0
        a = self.head   # temp pointer

        while a is not None:
            total = total + a.data
            a = a.next

        return total


# Creating list: 2 → 5 → 7 → 9 → 10
sll = SLL()
sll.head = Node(2)
sll.head.next = Node(5)
sll.head.next.next = Node(7)
sll.head.next.next.next = Node(9)
sll.head.next.next.next.next = Node(10)

print("Count:", sll.count_nodes())
print("Sum:", sll.sum_nodes())