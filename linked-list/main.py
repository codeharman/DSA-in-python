# Node class

class Node:
  def __init__(self, value, next = None):
    self.value = value
    self.next = next

#Linked List

class LinkedList:
  def __init__(self):
    self.head = None
  
  def insert(self, value):
    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node

  def print_list(self):
    current = self.head
    while current:
      print(current.value)
      current = current.next

ll = LinkedList()

ll.insert(5)
ll.insert(10)
ll.insert(21)



ll.print_list()