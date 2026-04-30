class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None

    def search(self, key):
        current = self.head

        while current:
            if current.data == key:
                return current
            current = current.next

        return False
# Creating list: 1 → 2 → 3 → 4
sll = SLL()
sll.head = Node(1)
sll.head.next = Node(2)
sll.head.next.next = Node(3)
sll.head.next.next.next = Node(4)
key_to_search = 3
result = sll.search(key_to_search)

if result:
    print(f"Element {key_to_search} found in the linked list.")
    print("Node value:", result.data)
else:
    print(f"Element {key_to_search} not found in the linked list.")