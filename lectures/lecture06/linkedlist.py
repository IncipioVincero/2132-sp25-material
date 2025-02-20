class List:
  """
  abstract data type for a list.
  """

  def get(k):  #retrieve element at index k
    pass

  def insert(k,x): #insert element x at index k 
    pass

  def remove(k):  #remove element at index k
    pass

  def append(x): # add x at the end of the list
    pass


class Node: 
  def __init__(self, element, next = None): 
    self.element = element
    self.next = next


class SingleLinkedList(List): 

  def __init__(self): 
    self._head = None
    self.len = 0

  def get_node(self, k): 
    current = self._head
    for i in range(k):
      current = current.next
    return current

  def get(self, k):  #retrieve element at index k
    return self.get_node(k).element
   
  def insert(self, k,x): #insert element x at index k 
    if k > self.len: 
      raise IndexError("invalid list index") 

    if self.len == 0: 
      node = Node(x)
      self._head = node
    elif k == 0: 
      node = Node(x, self._head)
      self._head = node
    else:
      current = self.get_node(k-1)
      node = Node(x, current.next)
      current.next = node
    self.len += 1

  def remove(self, k):  #remove element at index k
      if k >= self.len:
        raise IndexError("invalid list index")
      elif k == 0:
        oldhead = self._head
        self._head = self._head.next
        oldhead.next = None
      else: 
        current = self.get_node(k-1)
        oldnext = current.next 
        current.next = current.next.next
        oldnext.next = None
    
      self.len -= 1

  def remove_first(self): #aka pop
    self.remove(0)

  def remove_last(self): 
    self.remove(self.len - 1)

  def prepend(self, x): # insert at the beginning of list 
    self.insert(0, x)    

  def append(self,x): # add x at the end of the list, aka push
    self.insert(self.len, x)

  def __repr__(self): 

    if self.len == 0:
      return "[ ]"

    current = self._head
    result = "["
    while current.next != None: #for i in range(self.len):
      result = result + str(current.element) + " "
      current = current.next
    result = result + str(current.element) + "]"
    return result 


class DoubleNode:
  
  def __init__(self, element, prev, next):
    self.element = element
    self.prev = prev
    self.next = next
    

class LinkedListIterator: 

  def __init__(self, current):
    self.current = current

  def next(self):
    if self.current.next == None: 
      raise StopIteration
    element = self.current.element
    self.current = current.next
    return element    


class DoubleLinkedList(List): 

  def __init__(self): 
    self._head = DoubleNode(None, None, None)
    self._tail = DoubleNode(None, self._head, None) 
    self._head.next = self._tail
    self.len = 0

  def iterator(self): 
    return LinkedListIterator(self._head.next)


  def get_node(self, k):
   
    if k == -1: 
      return self._head    

    if k <= self.len // 2:   # k in first half
      current = self._head.next
      for i in range(k):
        current = current.next
    else:                   # k in second half    
      current = self._tail.prev
      for i in range(self.len - k -1):
        current = current.prev
      

    return current

  def get(self, k):  #retrieve element at index k
    return self.get_node(k).element
   
  def insert(self, k,x): #insert element x at index k 
    if k > self.len: 
      raise IndexError("invalid list index") 

    pred = self.get_node(k-1)
    node = DoubleNode(x, None, None) 
    node.next = pred.next 
    pred.next = node
    node.next.prev = node
    node.prev = pred 
    self.len += 1

  def remove(self, k):  #remove element at index k
      if k >= self.len:
        raise IndexError("invalid list index")

      node = self.get_node(k)
      pred = node.prev
      succ = node.next

      pred.next = succ
      succ.prev = pred
      node.next = None
      node.prev = None
      self.len -= 1

  def remove_first(self): #aka pop
    self.remove(0)

  def remove_last(self): 
    self.remove(self.len - 1)

  def prepend(self, x): # insert at the beginning of list 
    self.insert(0, x)    

  def append(self,x): # add x at the end of the list, aka push
    self.insert(self.len, x)

  def __repr__(self): 

    # TODO needs to be updated
    if self.len == 0:
      return "[ ]"

    current = self._head.next
    result = "["
    while current.next != self._tail: #for i in range(self.len):
      result = result + str(current.element) + " "
      current = current.next
    result = result + str(current.element) + "]"
    return result 
   
class Deque:

    def __init__(self): 
        self._list = DoubleLinkedList()

    def add_first(self, e):
        'Add element e to the front of the double-ended queue'
         self._list.insert(0, e)

    def add_last(self, e):
        'Add element e to the end of the double-ended queue'
        self._list.append(e)

    # Renamed deque operation
    def remove_first(self):
        'Remove the first element from the double-ended queue'
        element = self.get(0) 
        self._list.remove(0)
        return element

    def remove_last(self):
        'Remove the last element from the double-ended queue'
        element = self.get(self._list.len-1)
        self._list.remove(self._list.len-1)
        return element

    # Auxiliary operations
    
    def first(self):
        'Return a reference to the first element in the double-ended queue'
        return self.get(0)

    def last(self):
        'Return a reference to the last element in the double-ended queue'
        return self.get(self._list.len-1)

    def is_empty(self):
        return self._list.len == 0

    def __len__(self):
        return self._list.len 



li = DoubleLinkedList()
li.append(1)
li.append(2)
li.append(3)




# Runtime? O(N^2) with a linked list,  O(N) with array list
for i in range(li.len): 
  print(li.get(i))

# With LinkedListIterator: O(N) on a linked list
for x in li: 
  print(x)

iter = li.iterator()
try:
  while True: 
    x = iter.next()
except StopIteration: 
   pass





