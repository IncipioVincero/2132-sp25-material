class AbstractPosition:
    'An abstraction representing the location of a single element'

    def element(self):
        raise NotImplemented('Must be implemented by a subclass')

    def __eq__(self, other):
        'Returns True if Position represents the same location'
        raise NotImplemented('Must be implemented by a subclass')

    def __ne__(self, other):
        return not (self == other)

class AbstractTree:

    def root(self):
        'Return the root of the tree or None'
        raise NotImplemented('Must be implemented in subclass')

    def parent(self, p):
        'Return the parent of the node at position p or none if p is root'
        raise NotImplemented('Must be implemented in subclass')

    def children(self, p):
        'Return all children of the node at position p'
        raise NotImplemented('Must be implemented in subclass')

    def num_children(self, p):
        'Return the number of children of the node at position p'
        raise NotImplemented('Must be implemented in subclass')

    def __len__(self, p):
        'Return the number of elements in the tree'
        raise NotImplemented('Must be implemented in subclass')

    # Query methods
    
    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p): 
      'Calculate the depth of a tree. Recursive version.'
      if self.is_root(p):
          return 0
      else:
        return self.depth_recursive(self.parent(p)) + 1

    def _height(self, p): # compute the height of subtree rooted in p, recursively
      if self.is_leaf(p):
        return 0
      else:
        return 1 + max([self._height(c) for c in self.children(p)])

    def height(self, p=None):
      if p is None:
        p = self.root()
      return self._height(p)


class AbstractBinaryTree(AbstractTree):
    def left(self, p):
        'Return the left child of node at position p'
        raise NotImplemented('Must be  implemented by subclass')

    def right(self, p):
        'Return the right child of node at position p'
        raise NotImplemented('Must be  implemented by subclass')

    def valid_position(self, p): 
        raise NotImplemented('Must be  implemented by subclass')

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        children = []
        if self.left(p) is not None:
            children.append(self.left(p))
            
        if self.right(p) is not None:
            children.append(self.right(p))
        return children

    def postorder(self, p):
      'retrieve a list of elements in the tree in pre-order'
      if p == None: # Base case 
          return []
     
      parent = p.element()   # "2"
     
      left = self.postorder(self.left(p)) # []

      right = self.postorder(self.right(p)) # []  
      return  left + right + [parent]   # [] + [] + [2] = [2]
      
      
    def preorder(self, p):
      'retrieve a list of elements in the tree in pre-order'
      if p == None: # Base case 
          return []
     
      parent = p.element()   # "2"
     
      left = self.preorder(self.left(p)) # []

      right = self.preorder(self.right(p)) # []  
      return [parent] + left + right
      

    def inorder(self, p):
      'retrieve a list of elements in the tree in pre-order'
      if p == None: # Base case 
          return []
     
      parent = p.element()   # "2"
     
      left = self.inorder(self.left(p)) # []

      right = self.inorder(self.right(p)) # []  
      return  left + [parent] + right  
      


class LinkedBinaryTree(AbstractBinaryTree):
    class _Node:
        def __init__(self, element, parent=None, left=None, right=None):
          self._element = element
          self._parent = parent            
          self._left = left
          self._right = right
                
    class Position(AbstractPosition):
        def __init__(self, container, node):
            self._container = container
            self._node = node
        
        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node
            
    def _make_position(self, node):
        "Converts a node to the node's position in the tree"
        if node is None:
            return None
        else:
            return self.Position(self, node)

    def _validate(self, p): # retrieve the node object in position p 
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node

    def __init__(self):
        'Create an empty linked binary tree'
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        'Return the parent of the node at position p or none if p is root'
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    # Constant time operation
    def _add_root(self, e):
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    # Constant-time operation
    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    # Constant-time operation
    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old
                
    def _delete(self, p):
        node = self._validate(p)

        # We cannot easily delete a node that has two children. If the
        # node has only one child, the child could be plugged into the
        # tree instead of the parent being removed. But there is no easy
        # way to plug the other child.
        if self.num_children(p) == 2:
            raise ValueError('Position has two children')
            
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
            
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child

        self._size -= 1
        node._parent = node
        return node._element
        
    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old
  
    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('position must be leaf')
            
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')
    
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0


def parse_postorder(postorder): 

  stack = []  # use append instead of push
  
  for s in postorder: 
    
    if s == '+' or s == '*' or s == '-' or s == '/': 
      # operator
      right = stack.pop()
      left = stack.pop()

      node = LinkedBinaryTree._Node(s, left = left, right = right )
      stack.append(node)

    else: 
      # operand = number
      node = LinkedBinaryTree._Node(s)
      stack.append(node)

  result = LinkedBinaryTree()
  result._root = stack.pop()       
  return result
    

if __name__ == "__main__":

  #tree = LinkedBinaryTree()
  #
  #root = tree._add_root("*")
  #tree._add_right(root, 1)
  #plus = tree._add_left(root, '+')
  #two = tree._add_left(plus, 2) 
  #tree._add_right(plus, 3) 

  #root_position = tree.root()

  tree = parse_postorder([2, 3, '+', 1, '*'])

  print(tree.postorder(tree.root()))
  print(tree.preorder(tree.root()))
  print(tree.inorder(tree.root()))

  

