# Node Class

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None 

# Doubly LinkdedList

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  
  def add_to_head(self, value):
    new_node = Node (value)
    
    if self.head:
      new_node.next = self.head
      self.head.prev = new_node
    else:
      self.tail = new_node
    
    self.head = new_node
  
  def print(self):
    curr = self.head

    while curr:
      print(curr.value)
      curr = curr.next
    

dll = DoublyLinkedList()

dll.add_to_head(2)
dll.add_to_head(59)
dll.print()