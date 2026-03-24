# Node class

class Node:
  def __init__(self, value, next = None ):
    self.value = value
    self.next = next

# Linked List

class Linked_list:
  def __init__(self, head = None):
    self.head = head

  def insert(self, value):
    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node

  def remove(self, value):
    
    # values are 5,4,2 and lets say we want to remove value 4
    # 1. 4 node pointer points to the 2 node
    # 2. we need to make 5 pointer points to the 2 node instead of the 4 node or kind of make it skip

    curr = self.head

    if curr.value is None:
      return
    
    if curr.value == value:
      self.head = curr.next
      return
      
    
    while curr.next:
      if curr.next.value == value:
        curr.next = curr.next.next
        return 
      curr = curr.next

  def print(self):
    curr = self.head
    while curr:
      print(curr.value)
      curr = curr.next

ll = Linked_list()

ll.insert(2)
ll.insert(5)
ll.insert(8)
ll.remove(8)
ll.print()
