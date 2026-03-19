# Node Class

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next
  
# Node LinkedList

class LinkedList:
  def __init__(self, head=None):
    self.head = head
  
  def insert(self, value):
    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node
  
  def print(self):
    current = self.head
    while current:
      print(current.value)
      current = current.next
  
  def remove(self, value):
    current = self.head

    if current is None:
      return
    
    if current.value == value:
      self.head = current.next
      return
    
    while current.next:
      if current.next.value == value:
        current.next = current.next.next
        return
      current = current.next

ll = LinkedList()

ll.insert(5)
ll.insert(10)
ll.insert(100)
ll.remove(10)
ll.print()