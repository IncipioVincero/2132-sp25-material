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
    
class DoubleLinkedList(List): 

  def __init__(self): 
    self._head = DoubleNode(None, None, None)
    self._tail = DoubleNode(None, self._head, None) 
    self._head.next = self._tail
    self.len = 0

  def get_node(self, k):
    
    if k == -1: 
      return self.head    
 
    current = self._head.next
    for i in range(k):
      current = current.next
    return current

  def get(self, k):  #retrieve element at index k
    return self.get_node(k).element
   
  def insert(self, k,x): #insert element x at index k 
    if k > self.len: 
      raise IndexError("invalid list index") 

    current = self.get_node(k-1)
    node = None(x, None, None) 
    node.next = current.next 
    current.next = node
    node.next.prev = node
    node.prev = curr
    self.len += 1

  def remove(self, k):  #remove element at index k
      if k >= self.len:
        raise IndexError("invalid list index")

      #pass TODO

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

    current = self._head
    result = "["
    while current.next != None: #for i in range(self.len):
      result = result + str(current.element) + " "
      current = current.next
    result = result + str(current.element) + "]"
    return result 

    

