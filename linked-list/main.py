# Linked List

# class Node

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

# assigning data

node1 = Node(11)
node2 = Node(22)
node3 = Node(33)

# assigning pointers

node1.next = node2
node2.next = node3

# traversal nodes

curr = node1

while curr:
  print(curr.value)
  curr = curr.next
print("None")