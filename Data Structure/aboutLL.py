class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def add(self, data):
        node = head
        while node.next:
            node = node.next
        node.next = Node(data)


node = Node(1)
head = node
for index in range(2, 10):
    node.add(index)

while node.next:
    print(node.data)
    node = node.next
print(node.data)