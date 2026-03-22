# Node class

class Node:
  def __init__(self, value, next = None):
    self.value = value
    self.next = next

# Linked list

class LinkedList:
  def __init__(self, head = None):
    self.head = head

  def insert(self, value):
    node_head = Node(value)
    node_head.next = self.head
    self.head = node_head

  def remove(self, value):
    current = self.head

    if current.value is None:
      return
    
    while current.next:
      if current.next.value == value:
        current.next = current.next.next
        return
      current = current.next
  
  def swap_nodes(self, val1, val2):

    # if both values are same there is nothing to worry about

    if val1 == val2:
      return
    
    # find val1

    prev1 = None
    curr1 = self.head

    while curr1:
      if curr1.value == val1:
        prev1 = curr1
        curr1 = curr1.next
    
    # find val2

    prev2 = None
    curr2 = self.head

    while curr2:
      if curr2.value == val2:
        prev2 = curr2
        curr2 = curr2.next
    
    if curr1 is None or curr2 is None:
      print('One or two values are missing')
      return

    # change the previous nodes

    if prev1 is None:
      self.head = curr2
    else:
      prev1.next = curr2

    if prev2 is None:
      self.head = curr1
      prev2.next = curr1

    # swap next pointers

    temp = curr1.next
    curr1.next = curr2.next
    curr2.next = temp


  def print(self):
    current = self.head

    while current:
      print(current.value)
      current = current.next



ll = LinkedList()

ll.insert(23)
ll.insert(65)
ll.insert(245)
ll.insert(52)

ll.swap_nodes(65, 34)

ll.print()
