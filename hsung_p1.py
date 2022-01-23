#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 13:01:11 2022

Program: project 1 - Stacks and Queues
Author: Hakyung Sung
Submit date: 01/22/21
Description: a program that creates linear data structures of stacks and queues
			using a linked list data structure as a base
"""
	

'''
prep: classes for error handling
'''

# Exceptions raised when both queue/stack are full or empty

class QueueCapacityTypeError(Exception):
	pass

class QueueCapacityBoundError(Exception):
	pass

class QueueIsFull(Exception):
	pass

class QueueIsEmpty(Exception):
	pass

class StackCapacityTypeError(Exception):
	pass

class StackCapacityBoundError(Exception):
	pass

class StackIsFull(Exception):
	pass

class StackIsEmpty(Exception):
	pass

'''
Task1: Write the  Node class
'''

class Node:

	# Function to initialize the node object	
	def __init__(self, data):
		self.data = data 		# contains the data for a given node
		self.next = None 		# contains a pointer to the next node

'''
Task2: Write the Queue class
'''

class Queue():

	'''
	creates Queue class using linked list
	including basically Enqueue and Dequeue methods
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
		self.currentsize = 0		# contains the current number of items in the queue
	
	
	def isFull(self):
		'''
		returns True/False depending of it the queue is full or not
		'''
		
		if self.currentsize == self.capacity:
			return True
		else:
			return False
		
		
	def isEmpty(self):
		'''
		returns True/False depending of it the queue is empty or not
		'''
		if self.currentsize ==0:
			return True
		else:
			return False
		
		
	def enqueue(self, item):
		'''
		adds an item to the queue.
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
			self.currentsize +=1
			return True

	
	def dequeue(self):
		'''
		removes an item from the queue.
		returns the removed item.
		'''
		returnValue = None
		
		if self.isEmpty():		# raises an QueueIsEmpty exception if empty
			raise QueueIsEmpty("The method is called when the queue is empty.")
		else:
			if self.currentsize == 1:	# dequeue when only one element exists
				returnValue = self.head.data
				self.head = None
				self.tail = None
			else:						# dequeue when more than one element
				returnValue = self.head.data
				tempv = self.head
				self.head = self.head.next
				tempv.next = None
			self.currentsize -=1
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
	including basically Push and Pop methods
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
		self.currentsize = 0		# contains the current number of items in the stack
	
	
	def isFull(self):
		'''
		returns True/False depending of it the stack is full or not
		'''
		if self.currentsize == self.capacity:
			return True
		else:
			return False
		
		
	def isEmpty(self):
		'''
		returns True/False depending of it the stack is empty or not
		'''
		if self.currentsize == 0:
			return True
		else:
			return False
		
		
	def push(self, item):
		'''
		adds an item to the stack.
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
			self.currentsize += 1
			return True

	
	def pop(self):
		'''
		removes an item from the stack.
		returns the removed item.
		'''
		returnValue = None
		
		if self.isEmpty():		# raises an StackIsEmpty exception if empty
			raise StackIsEmpty("The method is called when the stack is empty.")
		else:
			if self.currentsize == 1:	# pop when only one element exists
				returnValue = self.head.data
				
				self.head = None
			else:						# pop when more than one element
				returnValue = self.head.data
				
				self.head = self.head.next
			self.currentsize -=1
			return returnValue
	

	def peek(self):
		'''
		peaks an item from the stack without deleting it
		returns the item at the front or return False if the queue is empty
		'''		
		if self.isEmpty():		# raises an QueueIsEmpty exception if empty
			raise StackIsEmpty("The method is called when the queue is empty.")
		else:
			print(self.head.data)
				