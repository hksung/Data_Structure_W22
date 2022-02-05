#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri Feb 2

Program: CIS 313 Project2 - PriorityQueue
Author: Hakyung Sung
Submit date: 02/07/22
Description: a program that implements the max-heap variety of priority queues

"""
	

'''
prep: classes for error handling
'''


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

'''
Task1: Write the  Node class
'''

class Node:

	'''
	makes a node for a given data
	'''
	
	def __init__(self, data):
		self.data = data 		# contains the data for a given node
		self.next = None 		# contains a pointer to the next node

'''
Task2: Write the Queue class
'''

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
			raise QueueCapacityTypeError("ERROR: The capacity must be an int") # error handling(1): type
		elif (capacity <=0):
			raise QueueCapacityBoundError("ERROR: The capacity must be a positive int.") # error handling(2): bound
			
		self.head = None			# contains the head of the linked list
		self.tail = None			# contains the tail of the linked list
		self.capacity = capacity	# contains the total num of items that can be fit into the queue
		self.currentSize = 0		# contains the current number of items in the queue
	
	
	def isFull(self):
		'''
		returns True/False depending of it the queue is full or not
		'''
		
		if self.currentSize == self.capacity:	# specifies the condition for full
			return True
		else:
			return False
		
		
	def isEmpty(self):
		'''
		returns True/False depending of it the queue is empty or not
		'''
		if self.currentSize ==0:	# specifies the condition for empty
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
			return False
		else:
			if self.isEmpty():			# enqueue when the queue is empty
				self.head = item_add
				self.tail = item_add
			else:						# enqueue when the queue is neither empty nor full
				self.tail.next = item_add
				self.tail = item_add
			self.currentSize +=1		# adds to the current size
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
			if self.currentSize == 1:	# dequeue when only one element exists
				returnValue = self.head.data
				self.head = None
				self.tail = None
			else:						# dequeue when more than one element
				returnValue = self.head.data
				
				tempv = self.head
				self.head = self.head.next
				tempv.next = None
			self.currentSize -=1		# subtracts from the current size
			return returnValue
	
	def front(self):
		'''
		peaks an item from the queue without deleting it
		returns the item at the front or return False if the queue is empty
		'''		
		if self.isEmpty():		# raises an QueueIsEmpty exception if empty
			raise QueueIsEmpty("The method is called when the queue is empty.")
		else:
			print(self.head.data)


'''
Task3: Write the Stack class
'''

class Stack():

	'''
	creates Stack class using linked list
	including basically push, pop, peek methods
	'''

	def __init__(self, capacity=0):
		'''
		constructor for the stack class initiation including instance variables (head, capacity, currentsize)
		'''
		
		if((type(capacity) != int)):
			raise StackCapacityTypeError("ERROR: The capacity must be an int") # error handling(1): type
		elif (capacity <=0):
			raise StackCapacityBoundError("ERROR: The capacity must be a positive int.") # error handling(2): bound
			
		self.head = None			# contains the head of the linked list
		self.capacity = capacity	# contains the total num of items that can be fit into the stack
		self.currentSize = 0		# contains the current number of items in the stack
	
	
	def isFull(self):
		'''
		returns True/False depending of it the stack is full or not
		'''
		if self.currentSize == self.capacity:	# specifies the condition for full
			return True
		else:
			return False
		
		
	def isEmpty(self):
		'''
		returns True/False depending of it the stack is empty or not
		'''
		if self.currentSize == 0:	# specifies the condition for empty
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
		
		if self.isEmpty():		# raises an StackIsEmpty exception if empty
			raise StackIsEmpty("The method is called when the stack is empty.")
		else:
			if self.currentSize == 1:	# pop when only one element exists
				returnValue = self.head.data
				
				self.head = None
			else:						# pop when more than one element
				returnValue = self.head.data
				
				self.head = self.head.next
			self.currentSize -=1		# subtracts from the current size
			return returnValue
	

	def peek(self):
		'''
		peaks an item from the stack without deleting it
		returns the item at the front or return False if the stack is empty
		'''		
		if self.isEmpty():		# raises an StackIsEmpty exception if empty
			raise StackIsEmpty("The method is called when the stack is empty.")
		else:
			print(self.head.data)

'''
Project2 Starts from here
'''


class PriorityQueue:

	'''
	creates PriorityQueue(PQ) class using heap
	including basically insert, extractMax, and peekMax methods
	'''

	def __init__(self, capacity=0):
		'''
		The PQ constructor
		Inputs: a positive integer for the size
		Usage: PQ1 = PriorityQueue(<int>)
		'''	
		if((type(capacity) != int)):
			raise QueueCapacityTypeError("ERROR: The capacity must be an int") # error handling for type
		elif (capacity <=0):
			raise QueueCapacityBoundError("ERROR: The capacity must be a positive int.") # error handling for bound
			
		self._heap = []
		self._heapIndices = {} # contains the index as a dictionary format
		self.capacity = capacity	# contains the total num of items that can be fit into the queue
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
		if self.currentSize == self.capacity:	# specifies the condition for full
			return True
		else:
			return False
		
		
	def isEmpty(self):
		'''
		Returns True/False depending of it the PQ is empty or not
		'''
		if self.currentSize == 0:	# specifies the condition for empty
			return True #len(self.heapList) == 0:
		else:
			return False
		
	def appendtoheap(self, item):
		'''
		Connects the insert method and heapindex dic
		'''		
		self._heap.append(item)
		self._heapIndices[item[1]] = len(self._heap)-1

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
			self.appendtoheap(item)
			self.maxHeapifyUp((len(self._heap)-1))
		self.currentSize += 1
		returnValue = True
		return returnValue
	
	def hasParent(self, nodeidx):
		'''
		Checks the parent nodeidx
		'''			
		if nodeidx > 0:
			return True
		
	def getParentidx(self, nodeidx):
		'''
		Gets the parent nodeidx
		'''			
		return int((nodeidx-1)/2)
	
	def getLeftChildidx(self, nodeidx):
		'''
		Gets the leftchild nodeidx
		'''			
		return nodeidx*2+1
	
	def getRightChildidx(self, nodeidx):
		'''
		Gets the rightchild nodeidx
		'''			
		return nodeidx*2+2
	
	def hasLeftChild(self, nodeidx):
		'''
		Checks the leftchild nodeidx
		'''			
		if self.getLeftChildidx(nodeidx)<len(self._heap):
			return True
		
	def hasRightChild(self, nodeidx):
		'''
		Checks the rightchild nodeidx
		'''			
		if self.getRightChildidx(nodeidx) < len(self._heap):
			return True
		
	def parentPriority(self, nodeidx):
		'''
		Returns the parent priority
		'''			
		return self._heap[self.getParentidx(nodeidx)][0]		
	
	def leftChildPriority(self, nodeidx):
		'''
		Returns the leftchild priority
		'''				
		return self._heap[self.getLeftChildidx(nodeidx)][0]			
			
	def rightChildPriority(self, nodeidx):
		'''
		Returns the rightchild priority
		'''			
		return self._heap[self.getRightChildidx(nodeidx)][0]				
	
	def maxHeapifyUp(self, nodeidx):
		'''
		Functions for items in the heap go up
		'''	
		while(self.hasParent(nodeidx)) and self.parentPriority(nodeidx) < self._heap[nodeidx][0]:
			self.swap(self.getParentidx(nodeidx), nodeidx)
			nodeidx = self.getParentidx(nodeidx)
			
	def maxHeapifDown(self, nodeidx):
		'''
		Functions for items in the heap go down
		'''		

		while self.hasLeftChild(nodeidx):
			biggerChildidx = self.getLeftChildidx(nodeidx)
			
			if self.hasRightChild(nodeidx) and self.rightChildPriority(nodeidx) > self.leftChildPriority(nodeidx):
				biggerChildidx = self.getRightChildidx(nodeidx)
				
			if self._heap[nodeidx][0] < self._heap[biggerChildidx][0]:
				self.swap(nodeidx, biggerChildidx)
				nodeidx = biggerChildidx
			else:
				return
			
	def swap(self, parentidx, childidx):
		'''
		Functions for swamp the items in the heap
		'''		
		tempVal = self._heap[parentidx]
		self._heap[parentidx] = self._heap[childidx]
		self._heap[childidx] = tempVal
		
		# after finishing swap, update the indices in the _heapIndices dic
		self._heapIndices[self._heap[parentidx][1]] = parentidx
		self._heapIndices[self._heap[childidx][1]] = childidx
		
	def extractMax(self):
		'''
		Key method2: This method removes and returns the tuple with the highest
		priority.
		'''		
		if self.isEmpty():		# raises an QueueIsEmpty exception if PQ is empty
			raise QueueIsEmpty("The method is called when the PQ is empty.")
		
		if self.hasLeftChild(0):
			self.swap(0, (len(self._heap)-1))
			popped = self._heap.pop()
			self.maxHeapifDown(0)		# reorders the heap after extraction
			self.currentSize-=1			# downsize the heap
		elif len(self._heap) == 1:		# if heap has only one item
			popped = self._heap.pop()
			self.currentSize-=1
		del self._heapIndices[popped[1]] # reorders the heap index
		return popped

	def peekMax(self):
		'''
		Key method3: This method returns the tuple with the highest priority.
		'''		
		if self.isEmpty():		# if the queue is empty, it will return False
			return False

		if self.hasLeftChild(0):
			self.swap(0, (len(self._heap)-1))
			print(self._heap[-1])
			self.maxHeapifDown(0)
		elif len(self._heap) == 1:
			print(self._heap[-1])

	def heapSort(self,lst):
		'''
		Extra method: This method sorts the given list of tuples.
		'''	
		if((type(lst) != list)):
			raise HeapSortInputError("ERROR: The lst must be a list ") # error handling for type
		else:
			for item in lst:
				list1 = self.insert(item)
				list1 = self._heap
			
			output = []
			
			for i in range(len(list1)):
				list1 = self
				popped = self.extractMax()
				output.append(popped)
			return output
