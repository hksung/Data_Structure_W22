#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program: CIS 313 Project4 - Red Black Tree
Author: Hakyung Sung
Submit date: 03/09/22
Description: a program that implements Redblacktree with various functions
    related to red black tree, binary search tree, etc.
"""


# ========================== Exceptions Classes ================================

class QueueCapacityTypeError(Exception):
    '''
    This exception gets raised when the queue is given the wrong type
    '''
    pass


class QueueCapacityBoundError(Exception):
    '''
    This exception gets raised when the queue is given the wrong bound
    '''
    pass


class QueueIsFull(Exception):
    '''
    This exception gets raised when the queue is full
    '''
    pass


class QueueIsEmpty(Exception):
    '''
    This exception gets raised when the queue is empty
    '''
    pass


class StackCapacityTypeError(Exception):
    '''
    This exception gets raised when the stack is given the wrong type
    '''
    pass


class StackCapacityBoundError(Exception):
    '''
    This exception gets raised when the stack is given the wrong bound
    '''
    pass


class StackIsFull(Exception):
    '''
    This exception gets raised when the stack is full
    '''
    pass


class StackIsEmpty(Exception):
    '''
    This exception gets raised when the stack is empty
    '''
    pass


class HeapSortInputError(Exception):
    '''
    This exception gets raised when the heapsort input is given the wrong type
    '''
    pass


class QueueInputTypeError(Exception):
    '''
    This exception gets raised when the input is given the wrong type
    '''
    pass


class TreeIsEmpty(Exception):
    '''
    This exception gets raised when the tree is empty
    '''
    pass

# ============================ Helper Methods ===================================

# ============================== Node Class =====================================


class Node:
    '''
    makes a node for a given data
    '''

    def __init__(self, data):
        self.data = data 		# contains the data for a given node
        self.next = None 		# contains a pointer to the next node

# ============================== BSTNode Class ==================================


class BSTNode():
    """ This class implements a node for the BST"""

    def __init__(self, item):
        """
        Description: The constructor for the Node class
        Usage: node = BSTNode(item)
                        item == (<int>, <value>)
        """
        self._parent = None
        self._rChild = None
        self._lChild = None
        self._value = item
        self._key = item[0]

    def __str__(self):
        """
        Returns a string rep of the node for debugging
        """
        returnValue = "Node: {}\n".format(self._key)
        returnValue += "Parent: {}\n".format(self._parent._key)
        returnValue += "Left Child: {}\n".format(self._lChild._key)
        returnValue += "Right Child: {}\n".format(self._rChild._key)
        return returnValue

    def getParent(self):
        """
        Description: Accessor method for the Node. Returns parent.
        Usage: <node>.getParent()
        """
        return self._parent

    def getRChild(self):
        """
        Description: Accessor method for the Node. Returns pright child.
        Usage: <node>.getRChild()
        """
        return self._rChild

    def getLChild(self):
        """
        Description: Accessor method for the Node. Returns left child.
        Usage: <node>.getLChild()
        """
        return self._lChild

    def getValue(self):
        """
        Description: Accessor method for the Node. Returns the item.
        Usage: <node>.getValue()
        """
        return self._value

    # Mutator methods
    def setParent(self, node):
        """
        Description: Mutator method. Sets the parent reference.
        Usage: <node>.setParent(<BSTNode>)
        """
        self._parent = node

    def setRChild(self, node):
        """
        Description: Mutator method. Sets the rchild reference.
        Usage: <node>.setRChild(<BSTNode>)
        """
        self._rChild = node

    def setLChild(self, node):
        """
        Description: Mutator method. Sets the lchild reference.
        Usage: <node>setLChild(<BSTNode>)
        """
        self._lChild = node

    # Comparison operators
    def __gt__(self, other):
        """
        Description: Overloads the > operator to allow direct comparison of
                                nodes.
        Usage: node1 > node2
        """
        returnValue = False
        if (other != None):
            returnValue = self._key > other._key
        return returnValue

    def __lt__(self, other):
        """
        Description: Overloads the < operator to allow direct comparison of
                                nodes.
        Usage: node1 < node2
        """
        returnValue = False
        if (other != None):
            returnValue = self._key > other._key
        return returnValue

    def __eq__(self, other):
        """
        Description: Overloads the == operator to allow direct comparison of
                                nodes.
        Usage: node1 == node2
        """
        returnValue = False
        if (other != None):
            returnValue = self._key == other._key
        return returnValue

    def __ne__(self, other):
        """
        Description: Overloads the != operator to allow direct comparison of
                                nodes.
        Usage: node1 != node2
        """
        returnValue = False
        if (other != None):
            returnValue = self._key != other._key
        if (other == None):
            returnValue = True
        return returnValue

    def __ge__(self, other):
        """
        Description: Overloads the >= operator to allow direct comparison of
                                nodes.
        Usage: node1 >= node2
        """
        returnValue = False
        if (other != None):
            returnValue = self._key >= other._key
        return returnValue

    def __le__(self, other):
        """
        Description: Overloads the <= operator to allow direct comparison of
                                nodes.
        Usage: node1 <= node2
        """
        returnValue = False
        if (other != None):
            returnValue = self._key >= other._key
        return returnValue

    # Some helper methods to make things easy in the BST
    def hasLeftChild(self):
        """
        Description: This methods returns true if the current node
                                has a left child.
        Usage: <node>.hasLeftChild()
        """
        returnValue = False
        if(type(self._lChild) == BSTNode and self._lChild._parent is self):
            returnValue = True
        return returnValue

    def hasRightChild(self):
        """
        Description: This methods returns true if the current node
                                has a right child.
        Usage: <node>.hasRightChild()
        """
        returnValue = False
        if(type(self._rChild) == BSTNode and self._rChild._parent is self):
            returnValue = True
        return returnValue

    def hasOnlyOneChild(self):
        """
        Description: This method returns true if the current node has
                                only one child.
        Usage: <node>.hasOnlyOneChild()
        """
        returnValue = False
        LC = self.hasLeftChild()
        RC = self.hasRightChild()
        if (LC and not RC) or (not LC and RC):
            returnValue = True
        return returnValue

    def hasBothChildren(self):
        """
        Description: This method returns true if the current node has
                                both children
        Usage: <node>.hasBothChildren()
        """
        returnValue = False
        LC = self.hasLeftChild()
        RC = self.hasRightChild()
        if (LC and RC):
            returnValue = True
        return returnValue

    def isLeaf(self):
        """
        Description: This method returns true if the current node is
                                a leaf node.
        Usage: <node>.ifLeaf()
        """
        returnValue = False
        if(self._rChild == None and self._lChild == None):
            returnValue = True
        return returnValue

    def isRoot(self):
        return not self._parent

    def isLeftChild(self):
        """
        Description: This method returns true if the current node is
                                a left child.
        Usage: <node>.isLeftChild()
        """
        returnValue = False
        if(self._parent != None):
            if(self._parent._lChild is self):
                if(self._parent._rChild is not self):
                    returnValue = True
        return returnValue

    def isRightChild(self):
        """
        Description: This method returns true if the current node is
                                a right child.
        Usage: <node>.isRightChild()
        """
        returnValue = False
        if(self._parent != None):
            if(self._parent._rChild is not self):
                if(self._parent._lChild is not self):
                    returnValue = True
        return returnValue

# ============================== RBNode Class ===================================


class RBNode():
    '''
    This class implements a node for the RBT
    '''

    def __init__(self, item):
        '''
        Description: The constructor for the RBNode class.
        Default color is red.

        Usage: node = RBNode(item) / item == (<init>, <value>)
        '''
        self._parent = None
        self._lChild = None
        self._rChild = None
        self.color = True
        self._value = item
        self._key = item[0]

    def __str__(self):
        '''
        Returns a string rep of the node (for debugging)
        '''
        color = "red" if(self.color) else "black"
        returnValue = f"Node: ({self._key}, {color})\n"
        returnValue += f"Parent: {self._parent._key if(self._parent != None) else self._parent}\n"
        returnValue += f"Left Child: {self._lChild._key if( self._lChild != None) else self._lChild}\n"
        returnValue += f"Right Child: {self._rChild._key if(self._rChild != None) else self._rChild}\n"
        return returnValue

    # Accessor Methods
    def getParent(self):
        """
        Description: Accessor method for the Node. Returns parent.
        Usage: <node>.getParent()
        """
        return self._parent

    def getRChild(self):
        """
        Description: Accessor method for the Node. Returns right child.
        Usage: <node>.getRChild()
        """
        return self._rChild

    def getLChild(self):
        """
        Description: Accessor method for the Node. Returns left child.
        Usage: <node>.getLChild()
        """
        return self._lChild

    def getValue(self):
        """
        Description: Accessor method for the Node. Returns the item.
        Usage: <node>.getValue()
        """
        return self._value

    def getKey(self):
        """
        Description: Accessor method for the Node. Returns the key.
        Usage: <node>.getKey()
        """
        return self._key

    def getColor(self):
        """
        Description: Accessor method for the Node. Returns the color.
        Usage: <node>.getColor()
        """
        return self.color

    # Mutator methods
    def setParent(self, node):
        """
        Description: Mutator method. Sets the parent reference.
        Usage: <node>.setParent(<RBNode>)
        """
        self._parent = node

    def setLChild(self, node):
        """
        Description: Mutator method. Sets the lchild reference.
        Usage: <node>.setLChild(<RBNode>)
        """
        self._lChild = node

    def setRChild(self, node):
        """
        Description: Mutator method. Sets the rchild reference.
        Usage: <node>.setRChild(<RBNode>)
        """
        self._rChild = node

    def setValue(self, value):
        """
        Description: Mutator method. Sets the value reference.
        Usage: <node>.setValue(<tuple>)
        """
        self._value = value

    def setKey(self, key):
        """
        Description: Mutator method. Sets the key reference.
        Usage: <node>.setKey(<int>)
        """
        self._key = key

    def setRed(self):
        """
        Description: Sets the color of the node to red.
        Usage: <node>.setRed()
        """
        self.color = True

    def setBlack(self):
        """
        Description: Sets the color of the node to black.
        Usage: <node>.setBlack()
        """
        self.color = False

    # comparison operators
    def __gt__(self, other):
        """
        Description: Overloads the > operator to allow direct comparison of
                                nodes.
        Usage: node1 > node2
        """
        returnValue = False
        if(other != None):
            returnValue = self._key > other._key
            return returnValue

    def __lt__(self, other):
        """
        Description: Overloads the < operator to allow direct comparison of
                                nodes.
        Usage: node1 < node2
        """
        returnValue = False
        if(other != None):
            returnValue = self._key < other._key
        return returnValue

    def __eq__(self, other):
        """
        Description: Overloads the == operator to allow direct comparison of
                                nodes.
        Usage: node1 == node2
        """
        returnValue = False
        if(other != None):
            returnValue = self._key == other._key
        return returnValue

    def __ne__(self, other):
        """
        Description: Overloads the != operator to allow direct comparison of
                                nodes.
        Usage: node1 != node2
        """
        returnValue = False
        if(other != None):
            returnValue = self._key != other._key
        if(other == None):
            returnValue = True
        return returnValue

    def __le__(self, other):
        """
        Description: Overloads the <= operator to allow direct comparison of
                                nodes.
        Usage: node1 <= node2
        """
        returnValue = False
        if(other != None):
            returnValue = self._key <= other._key
        return returnValue

    def __ge__(self, other):
        """
        Description: Overloads the >= operator to allow direct comparison of
                                nodes.
        Usage:  node1 >= node2
        Input: Another instance of the node class.
        """
        returnValue = False
        if(other != None):
            returnValue = self._key >= other._key
        return returnValue

    # Some helper methods to make things easy in the BST
    def hasLeftChild(self):
        """
        Description: This method returns true if the current node
                                has a left child.
        Usage: <node>.hasLeftChild()
        """
        returnValue = False
        if(type(self._lChild) == RBNode and self._lChild._parent is self):
            returnValue = True
        return returnValue

    def hasRightChild(self):
        """
        Description: This method returns true|false depending on if the current
                                node has a right child or not.
        Usage: <node>.hasRightChild()
        """
        returnValue = False
        if(type(self._rChild) == RBNode and self._rChild._parent is self):
            returnValue = True
        return returnValue

    def hasOnlyOneChild(self):
        """
        Description: Returns True if the current node has only one child.
        Usage: <node>.hasOnlyOneChild()
        """
        LC = self.hasLeftChild()
        RC = self.hasRightChild()
        return (LC and not RC) or (not LC and RC)

    def hasBothChildren(self):
        """
        Description: Returns True if the current node has both children
        Usage: <node>.hasBothChildren()
        """
        return self.hasLeftChild() and self.hasRightChild()

    def isLeaf(self):
        """
        Description: Returns true if the current node is a leaf node.
        Usage: <node>.isLeaf()
        """
        returnValue = False
        if(self._rChild == None and self._lChild == None):
            returnValue = True
        return returnValue

    def isLeftChild(self):
        """
        Description: Returns true if the current node is a left child
        Usage: <node>.isLeftChild()
        """
        returnValue = False
        if(self._parent != None):
            if(self._parent._lChild is self):
                if(self._parent._rChild is not self):
                    returnValue = True
        return returnValue

    def isRightChild(self):
        """
        Description: Returns true if the current node is a right child
        Usage: <node>.isRightChild()
        """
        returnValue = False
        if(self._parent != None):
            if(self._parent._rChild is self):
                if(self._parent._lChild is not self):
                    returnValue = True
        return returnValue

    def isRed(self):
        """
        Description: Returns True if this node is red.
        Usage: <node>.isRed()
        """
        return self.color == True

    def isBlack(self):
        """
        Description: Returns True if this node is black.
        Usage: <node>.isBlack()
        """
        return self.color == False

# ============================== Stack Class ====================================


class Stack():

    '''
    creates Stack class using linked list
    including basically push, pop, peek methods
    '''

    def __init__(self, capacity=0):
        '''
        constructor for the stack class initiation including instance variables (head, capacity, currentSize)
        '''

        if((type(capacity) != int)):
            raise StackCapacityTypeError(
                "ERROR: The capacity must be an int")  # error handling(1): type
        elif (capacity <= 0):
            raise StackCapacityBoundError(
                "ERROR: The capacity must be a positive int.")  # error handling(2): bound

        self.head = None			# contains the head of the linked list
        # contains the total num of items that can be fit into the stack
        self.capacity = capacity
        self.currentSize = 0		# contains the current number of items in the stack

    def isFull(self):
        '''
        returns True/False depending of it the stack is full or not
        '''
        if self.currentSize == self.capacity:  # specifies the condition for full
            return True
        else:
            return False

    def isEmpty(self):
        '''
        returns True/False depending of it the stack is empty or not
        '''
        if self.currentSize == 0:  # specifies the condition for empty
            return True
        else:
            return False

    def push(self, item):
        '''
        adds an item to the stack
        returns True/False depending on if the push was successful
        '''
        item_add = Node(item)

        if self.isFull():		# raises a StackIsFull exception if full
            raise StackIsFull("The method is called when the stack is full.")
            return False
        else:
            new_node = item_add
            new_node.next = self.head
            self.head = new_node
            self.currentSize += 1		# adds to the current size
            return True

    def pop(self):
        '''
        removes an item from the stack
        returns the removed item
        '''
        returnValue = None

        if self.isEmpty():		# raises an QueueIsEmpty exception if empty
            raise StackIsEmpty("The method is called when the stack is empty.")
        else:
            if self.currentSize == 1:  # dequeue when only one element exists
                returnValue = self.head.data
                self.head = None
            else:						# dequeue when more than one element
                returnValue = self.head.data

                tempv = self.head
                self.head = self.head.next
                tempv.next = None
            self.currentSize -= 1		# subtracts from the current size
            return returnValue

    def peek(self):
        '''
        peaks an item from the stack without deleting it
        returns the item at the front or return False if the stack is empty
        '''
        if self.isEmpty():		# raises an StackIsEmpty exception if empty
            return False
        else:
            return self.head.data

# ============================== Queue Class ====================================

class Queue():

    '''
    creates Queue class using linked list
    including basically enqueue, dequeue, front methods
    '''

    def __init__(self, capacity=0):
        '''
        constructor for the queue class initiation including instance variables (head, tail, capacity, currentsize)
        '''

        if((type(capacity) != int)):
            raise QueueCapacityTypeError(
                "ERROR: The capacity must be an int")  # error handling(1): type
        elif (capacity <= 0):
            raise QueueCapacityBoundError(
                "ERROR: The capacity must be a positive int.")  # error handling(2): bound

        self.head = None			# contains the head of the linked list
        self.tail = None			# contains the tail of the linked list
        # contains the total num of items that can be fit into the queue
        self.capacity = capacity
        self.currentSize = 0		# contains the current number of items in the queue

    def isFull(self):
        '''
        returns True/False depending of it the queue is full or not
        '''

        if self.currentSize == self.capacity:  # specifies the condition for full
            return True
        else:
            return False

    def isEmpty(self):
        '''
        returns True/False depending of it the queue is empty or not
        '''
        if self.currentSize == 0:  # specifies the condition for empty
            return True
        else:
            return False

    def enqueue(self, item):
        '''
        adds an item to the queue
        returns True/False depending on if the enqueue was successful
        '''
        item_add = Node(item)

        if self.isFull():		# raises a QueueIsFull exception if full
            raise QueueIsFull("The method is called when the queue is full.")
        else:
            if self.isEmpty():			# enqueue when the queue is empty
                self.head = item_add
                self.tail = item_add
            else:						# enqueue when the queue is neither empty nor full
                self.tail.next = item_add
                self.tail = item_add
            self.currentSize += 1		# adds to the current size
            return True

    def dequeue(self):
        '''
        removes an item from the queue
        returns the removed item
        '''
        returnValue = None

        if self.isEmpty():		# raises an QueueIsEmpty exception if empty
            raise QueueIsEmpty("The method is called when the queue is empty.")
        else:
            if self.currentSize == 1:  # dequeue when only one element exists
                returnValue = self.head.data
                self.head = None
                self.tail = None
            else:						# dequeue when more than one element
                returnValue = self.head.data

                tempv = self.head
                self.head = self.head.next
                tempv.next = None
            self.currentSize -= 1		# subtracts from the current size
            return returnValue

    def front(self):
        '''
        peaks an item from the queue without deleting it
        returns the item at the front or return False if the queue is empty
        '''
        if self.isEmpty():		# raises an QueueIsEmpty exception if empty
            return False
        else:
            return self.head.data
# ================================ PQ Class =====================================

class PriorityQueue:

    '''
    creates PriorityQueue(PQ) class using heap
    including basically insert, extractMax, and peekMax methods
    '''

    def __init__(self, capacity):
        '''
        The PQ constructor
        Inputs: a positive integer for the size
        Usage: PQ1 = PriorityQueue(<int>)
        '''
        if((type(capacity) != int)):
            raise QueueCapacityTypeError(
                "ERROR: The capacity must be an int")  # error handling for type
        elif (capacity <= 0):
            raise QueueCapacityBoundError(
                "ERROR: The capacity must be a positive int.")  # error handling for bound

        self._heap = []
        # contains the total num of items that can be fit into the queue
        self.capacity = capacity
        self.currentSize = 0		# contains the current number of items in the queue

    def __str__(self):
        '''
        Returns a string representation of the heap
        Format: "[(<prio1>, <item>),(prio2, item), ...]" or "[]" if the PQ is empty
        '''
        return str(self._heap)

    def isFull(self):
        '''
        Returns True/False depending of it the PQ is full or not
        '''
        if self.currentSize == self.capacity:  # specifies the condition for full
            return True
        else:
            return False

    def isEmpty(self):
        '''
        Returns True/False depending of it the PQ is empty or not
        '''
        if self.currentSize == 0:  # specifies the condition for empty
            return True
        else:
            return False

    def parent(index):
        return index/2

    def insert(self, item):
        '''
        Key method1: This method adds a tupble to the PQ based on its priority,
        then return True upon successfully adding it to the heap

        Intput: tuple item(s)
        Usage: returnValue = <insert>.PriorityQueue(<item>)
        '''
        returnValue = False

        if self.isFull():		# raises a QueueIsFull exception if PQ is full
            raise QueueIsFull("The method is called when the PQ is full.")
        elif type(item) != tuple:		# raises a QueueInputTypeError exception if input is not a tuple
            raise QueueInputTypeError("The input must be a tuple")
        else:
            self._heap.append(item)
            index = len(self._heap)-1

            while index != 1:
                numOfParentNode = index//2

                if self._heap[numOfParentNode][0] < self._heap[index][0]:
                    self._heap[numOfParentNode], self._heap[index] = self._heap[index], self._heap[numOfParentNode]
                    index = numOfParentNode
                else:
                    break

        returnValue = True
        self.currentSize += 1
        return returnValue

    def extractMax(self):
        '''
        Key method2: This method removes and returns the tuple with the highest
        priority.
        '''
        if self.isEmpty():		# raises an QueueIsEmpty exception if PQ is empty
            raise QueueIsEmpty("The method is called when the PQ is empty.")
        elif len(self._heap) == 1:
            popped = self._heap.pop()
            self.currentSize -= 1
        else:
            self._heap[1], self._heap[-1] = self._heap[-1], self._heap[1]
            popped = self._heap.pop(-1)
            self.maxHeapify(1)
            self.currentSize -= 1
        return popped

    def maxHeapify(self, i):
        left = i*2
        right = i*2 + 1
        greatest = i

        if left < len(self._heap) and self._heap[left][0] > self._heap[greatest][0]:
            greatest = left
        if right < len(self._heap) and self._heap[right][0] > self._heap[greatest][0]:
            greatest = right
        if greatest != i:
            self._heap[i], self._heap[greatest] = self._heap[greatest], self._heap[i]
            self.maxHeapify(greatest)

    def peekMax(self):
        '''
        Key method3: This method returns the tuple with the highest priority.
        '''
        if self.isEmpty():		# if the queue is empty, it will return False
            return False
        else:
            popped = self._heap[0]
        return popped

    def heapSort(self, lst):
        '''
        Extra method: This method sorts the given list of tuples.
        '''
        if((type(lst) != list)):
            # error handling for type
            raise HeapSortInputError("ERROR: The lst must be a list ")
        else:
            for item in lst:
                self.insert(item)

            output = []

            for i in range(len(lst)):
                popped = self.extractMax()
                output.append(popped)
            return output
# ================================ BST Class ====================================


class BinarySearchTree:
    """
    Description: A Binary Search Tree (BST)
    Let x be a node in a binary search tree.
    If y is a node in the left subtree of x, then y:key <= x:key.
    If y is a node in the right subtree of x, then y:key >= x:key.
    """

    def __init__(self):
        """The constructor for our BST
        Inputs: a tuple
        Usage: BST = BinarySearchTree()
        """
        self._root = None

    def _isValid(self, item):
        """
        Description: Checks to see if a tuple is valid
        Usage: (outside) BST.isValid(item) (inside) self.isValid(item)
        """
        returnValue = True
        if(type(item) != tuple):
            returnValue = False
        elif(type(item[0]) != int):
            returnValue = False
        elif(len(item) != 2):
            returnValue = False
        return returnValue

    def _transplantR(self, cNode):
        """
        Description: This transplant attaches the currentNodes right child
                                to the current nodes parant.
        Notes:
                        1. Do not call this method when CNode is the root.
                        2. Don't forget to handle the cNode references in your func.
        """
        parent = cNode.getParent()
        child = cNode.getRChild()
        if(cNode.isRightChild()):
            parent.setLChild(child)
            child.setParent(parent)
        else:
            parent.setRChild(child)
            child.setParent(parent)

    def _transplantL(self, cNode):
        """
        Description: This transplant attaches the currentNodes left child
                                to the current nodes parant.
        Notes:
                        1. Do not call this method when CNode is the root.
                        2. Don't forget to handle the cNode references in your func.
        """
        parent = cNode.getParent()
        child = cNode.getLChild()
        if(cNode.isLeftChild()):
            parent.setLChild(child)
            child.setParent(parent)
        else:
            parent.setRChild(child)
            child.setParent(parent)

    def traverse(self, mode):
        """
        Description: The traverse method returns a string rep
                                of the tree according to the specified mode.
        """
        self.output = ""
        if(type(mode) == str):
            if(mode == "in-order"):
                self.inorder(self._root)
            elif(mode == "pre-order"):
                self.preorder(self._root)
            elif(mode == "post-order"):
                self.postorder(self._root)
        else:
            self.output = "ERROR: Unrecognized mode..."
        return self.output[:-2]

    def inorder(self, node):
        """ computes the inorder traversal"""
        if (node != None):
            self.inorder(node.getLChild())
            self.output += str(node._key) + ", "
            self.inorder(node.getRChild())

    def preorder(self, node):
        """ computes the pre-order traversal"""
        if (node != None):
            self.output += str(node._key) + ", "
            self.preorder(node.getLChild())
            self.preorder(node.getRChild())

    def postorder(self, node):
        """ computes the postorder traversal"""
        if (node != None):
            self.postorder(node.getLChild())
            self.postorder(node.getRChild())
            self.output += str(node._key) + ", "

    def insert(self, item):
        """
        Description: This inserts a new item into the tree.
        Item: <tuple>
        Usage: BST.insert(int, "data")
        """
        returnValue = False

        if self._isValid(item) is False or item is None:
            return returnValue

        if self._isValid(item):
            node = BSTNode(item)

            if self._root == None:
                self._root = node
                returnValue = True
                return returnValue

            else:
                p = self._root
                while True:
                    if item[0] < p._key:

                        if p.getLChild() is not None:
                            p = p.getLChild()
                        else:
                            p._lChild = node
                            break
                    else:
                        if p.getRChild() is not None:
                            p = p.getRChild()
                        else:
                            p._rChild = node
                            break
                    returnValue = True
                    return returnValue

    def find(self, id):
        """
        Description: This takes an int id and returns the tuple in the tree
                whose ID matches that value. If no such tuple exists in the tree,
                return False
        Usage: BST.find(int)
        """
        p = self._root

        if p is None:  # when the tree is empty
            raise TreeIsEmpty()
        while p is not None:
            if p._key == id:
                return p._value
            elif id < p._key:
                p = p._lChild
            else:
                p = p._rChild
        return False

    def delete(self, id):
        """
        Description: This removes a node from the tree and return True,
                else it will return False
        Usage: BST.delete(int)
        """

        p = self._root
        prev = None

        if p is None:  # when the tree is empty raise the error
            raise TreeIsEmpty()

        while p is not None:
            if p._key == id:  # start delete key

                if p.isLeaf():
                    p = None
                    if prev == None:
                        self._root = None

                else:  # check if right child exist and
                    if p._rChild is None:
                        if prev == None:  # No right child, assign prev child to p.left
                            self._root = p._lChild  # Root is being deleted, update root

                        else:
                            if id < prev._key:
                                prev._lChild = p._lChild
                                p = None
                            else:
                                prev._rChild = p._lChild
                                p = None

                    else:
                        temp = p._rChild
                        temp_prev = p

                        while temp._lChild is not None:
                            temp_prev = temp
                            temp = temp._lChild

                        if(p._rChild == temp):
                            temp._lChild = p._lChild
                            p._rChild = None

                            del p

                            if prev == None:  # check if root is being deleted
                                self._root = temp

                        else:
                            p._key = temp._key
                            p._value = temp._value

                            if(temp._key < temp_prev._key):
                                temp_prev._lChild = None
                            else:
                                temp_prev._rChild = None

                            del temp
                return True

            elif id < p._key:
                prev = p

                p = p._lChild

            else:
                prev = p
                p = p._rChild

        return False
# ================================ RBT Class ====================================

class RedBlackTree:
    """
    Description: A Red-Black Tree (RBT).
    Each node stores an informatino of color, used to ensure that the tree
    remains balanced during insertions and deletions.
    """

    def __init__(self):
        """ The constructor for our RBT """
        self._root = None
        # Add any other instance variables you need.

    def _isValid(self, item):
        """
        Description: Checks to see if a tuple is valid
        Usage: (outside) <RBT>._isValid(item) (inside) self._isValid(item)
        """
        returnValue = True
        if(type(item) != tuple):
            returnValue = False
        elif(type(item[0]) != int):
            returnValue = False
        elif(len(item) != 2):
            returnValue = False
        return returnValue

    def _isRoot(self, node):
        """
        Description: This function returns true if the given node is the root.
        Usage: self._isRoot(node)
        """
        return node is self._root

    def _isEmpty(self):
        """
        Description: This method returns true if the tree is empty, else False.
        """
        return self._root == None

    def _rbTransplant(self, u, v):
        """
        Description: A pretty straightforward implementation of RB-Transplant from ch. 12 pg. 323 of the book.
        """
        if(u._parent == None):
            self._root = v
        elif(u.isLeftChild()):
            u.getParent().setLChild(v)
        else:
            u.getParent().setRChild(v)
        if(v != None):
            v.setParent(u.getParent())

    def traverse(self, mode):
        """
        Description: The traverse method returns a string rep
        of the tree according to the specified mode
        """
        self.output = ""
        if(type(mode) == str):
            if(mode == "in-order"):
                self.inorder(self._root)
            elif(mode == "pre-order"):
                self.preorder(self._root)
            elif(mode == "post-order"):
                self.postorder(self._root)
        else:
            self.output = "ERROR: Unrecognized mode..."
        return self.output[:-2]

    def inorder(self, node):
        """ computes the inorder traversal """
        if(node != None):
            self.inorder(node.getLChild())
            color = "red" if(node.color) else "black"
            self.output += f"({node.getKey()}, {color}), "
            self.inorder(node.getRChild())

    def preorder(self, node):
        """computes the pre-order traversal"""
        if(node != None):
            color = "red" if(node.color) else "black"
            self.output += f"({node.getKey()}, {color}), "
            self.preorder(node.getLChild())
            self.preorder(node.getRChild())

    def postorder(self, node):
        """ compute postorder traversal"""
        if(node != None):
            self.postorder(node.getLChild())
            self.postorder(node.getRChild())
            color = "red" if(node.color) else "black"
            self.output += f"({node.getKey()}, {color}), "

    def _findMinimum(self, node):
        """
        Description: Finds the successor of the current node and returns it.
        Usage: self._findMinimum(<RBNode>)
        """
        min = node
        while(min.hasLeftChild()):
            min = min.getLChild()
        return min

    def _findNode(self, id):
        """
        Description: Finds node in tree with given id,
        returns corresponding ticket. Returns False if unsuccessful.
        """
        if(type(id) == int):
            currentNode = self._root
            while(currentNode != None and currentNode.getKey() != id):
                if(id < currentNode._key):
                    currentNode = currentNode.getLChild()
                else:
                    currentNode = currentNode.getRChild()
        return currentNode if(currentNode != None) else False

    def insert(self, item):
        """
        Description: Inserts given tuple into the tree while
        preserving binary tree property.
        Returns True if successful, False otherwise
        See ch. 12 pg. 315 of the book
        """
        ret = False
        if(self._isValid(item)):
            z = RBNode(item)
            ret = True
            y = None
            x = self._root
            while(x != None):
                y = x
                if(z < x):
                    x = x.getLChild()
                else:
                    x = x.getRChild()
            z.setParent(y)
            if(y == None):
                self._root = z
                ret = True
            elif(z < y):
                y.setLChild(z)
                ret = True
            else:
                y.setRChild(z)
                ret = True
            z.setLChild(None)
            z.setRChild(None)
            z.setRed()
            self._insertFixup(z)
            ret = True
        return ret

    def delete(self, id):
        """
        Description: Deletes node from tree with given ticketID;
        restructures binary tree. Returns True if successful,
        False otherwise. See CH. 12 page 324 of the book.
        """
        ret = False
        if(self._isEmpty()):
            raise TreeIsEmpty("ERROR: Cannot delete from an empty tree.\n")
        elif(type(id) == int):
            z = self._findNode(id)
            if(type(z) == RBNode):
                ret = True
                y = z
                y_original_color = y.getColor()
                if(not z.hasLeftChild()):
                    x = z.getRChild()
                    self._rbTransplant(z, z.getRChild())
                elif(not z.hasRightChild()):
                    x = z.getLChild()
                    self._rbTransplant(z, z.getLChild())
                else:
                    y = self._findMinimum(z.getRChild())
                    y_original_color = y.getColor()
                    x = y.getRChild()
                    if(y.getParent() is z):
                        if (x != None):
                            x.setParent(y)
                    else:
                        self._rbTransplant(y, y.getRChild())
                        y.setRChild(z.getRChild())
                        y.getRChild().setParent(y)
                    self._rbTransplant(z, y)
                    y.setLChild(z.getLChild())
                    y.getLChild().setParent(y)
                    y.color = z.color
                if(y_original_color == False):
                    self._deleteFixup(x)
                z.setParent(None)
                z.setRChild(None)
                z.setLChild(None)

        return ret

    def find(self, id):
        """
        Description: Finds node in tree with given id,
        returns corresponding ticket. Returns False if unsuccessful.
        """
        ret = False
        if(self._root == None):
            raise TreeIsEmpty(
                "ERROR: Cannot find any nodes in an empty tree.\n")
        if(type(id) == int):
            result = self._findNode(id)
            if(type(result) == RBNode):
                ret = result.getValue()
        return ret
# ====================== IMPLEMENT THE METHODS BELOW ============================

    def _insertFixup(self, currentNode):
        """
        Description: Fixes the tree after inserting
        """

        if currentNode._parent is None:
            self._root.setBlack()
        else:
            if currentNode._parent.color is True:
                if currentNode._parent == currentNode._parent._parent._lChild:
                    y = currentNode._parent._parent._rChild
                    if y.isRed():
                        currentNode._parent.setBlack()
                        y.setBlack()
                        currentNode._parent._parent.setRed()
                        currentNode = currentNode._parent._parent
                    else:
                        if currentNode == currentNode._parent._rChild:
                            currentNode = currentNode._parent
                            self._leftRotate(currentNode)

                        currentNode._parent.setBlack()
                        currentNode._parent._parent.setRed()
                        self._rightRotate(currentNode._parent._parent)
                else:
                    y = currentNode._parent._parent._lChild

                    if y.isRed():
                        currentNode._parent.setBlack()
                        y._setBlack()
                        currentNode._parent._parent.setRed()
                        currentNode = currentNode._parent._parent

                    else:
                        if currentNode == currentNode._parent._lChild:
                            currentNode = currentNode._parent
                            self._rightRotate(currentNode)
                        currentNode._parent.setBlack()
                        currentNode._parent._parent.setRed()
                        self._leftRotate(currentNode._parent._parent)


    def _deleteFixup(self, currentNode):
        """
        Description: Restores the properties of the RB tree upon node deletion
        """
        while currentNode != self._root and currentNode.isBlack():
            if currentNode == currentNode._parent._lChild:
                x = currentNode._parent._rChild
                if x.isRed():
                    x.setBlack()
                    currentNode._parent.setRed()
                    self._leftRotate(currentNode._parent)
                    x = currentNode._parent._rChild
                if x._lChild.isBlack() and x._rChild.isBlack():
                    x.setRed()
                    currentNode = currentNode._parent
                else:
                    if x._rChild.isBlack():
                        x._lChild.setBlack()
                        x.setRed()
                        self._rightRotate(x)
                        x = currentNode._parent._rChild
                    x.color == currentNode._parent.color
                    currentNode._paret.setBlack()
                    x._rChild.setBlack()
                    self._leftRotate(currentNode._parent)
                    currentNode = self._root
            else:
                x = currentNode._parent._lChild
                if x.isRed():
                    x.setBlack()
                    currentNode._parent.setRed()
                    self._rightRotate(currentNode._parent)
                if x._rChild.isBlack() and x._lChild.isBlack():
                    x.setRed()
                    currentNode = currentNode._parent
                else:
                    if x._lChild.isBlack():
                        x._rChild.setBlack()
                        x.setRed()
                        self._leftRotate(x)
                        x = currentNode._parent._lChild
                    x.color == currentNode._parent.color
                    currentNode._parent.setBlack()
                    x._lChild.setBlack()
                    self._rightRotate(currentNode._parent)
                    currentNode = self._root
        currentNode.setBlack()

    def _leftRotate(self, currentNode):
        """
        Description: Performs a left rotation from a given node
        """
        cr = currentNode._rChild
        currentNode._rChild = cr._lChild

        if cr._lChild != self._root:
            cr._lChild._parent = currentNode

        cr._parent = currentNode._parent

        if currentNode._parent == self._root and currentNode._parent._isBlack():
            self._root = cr
        elif currentNode == currentNode._parent._lChild:
            currentNode._parent._lChild = cr
        else:
            currentNode._parent._rChild = cr
        cr._lChild = currentNode
        currentNode._parent = cr

    def _rightRotate(self, currentNode):
        """
        Description: Performs a right rotation from a given node
        """
        cl = currentNode._lChild
        currentNode._lChild = cl._rChild

        if cl._rChild != self._root:
            cl._rChild._parent = currentNode
        cl._parent = currentNode._parent

        if currentNode._parent == self._root and currentNode._parent._isBlack():
            self._root = cl
        elif currentNode == currentNode._parent._rChild:
            currentNode._parent._rChild = cl
        else:
            currentNode._parent._lChild = cl

        cl._rChild = currentNode
        currentNode._parent = cl
