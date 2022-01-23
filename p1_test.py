#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 13:26:33 2022

@author: hakyungsung
"""

from hsung_p1 import *
import pytest

class TestMain:

	#Constructor test here
	def test_initValidInt1(self):
		with pytest.raises(QueueCapacityTypeError):
			Q = Queue('a')
			Q = Queue(2.3)

	def test_initInvalidInt1(self):
		with pytest.raises(QueueCapacityBoundError):
			Q = Queue(-1)
			Q = Queue(0)

	def test_enqueueInvalidFull(self):

		with pytest.raises(QueueIsFull):
			Q = Queue(2)
			Q.enqueue(1)
			Q.enqueue(2)
			Q.enqueue(3)

	def test_enqueueValid(self):
		#try to enqueue something into the queue

		Q = Queue(10)
		Q.enqueue(1)

		assert Q.currentsize != 0
		assert Q.tail.data == 1

	def test_enqueueValidEmpty(self):

		Q1 = Queue(10)
		result = Q1.enqueue(1)

		assert result == True
		assert Q1.head.data == 1

	def test_denqueueInvalidEmpty(self):
		with pytest.raises(QueueIsEmpty):
			Q = Queue(1)
			Q.enqueue(1)
			Q.dequeue()
			Q.dequeue()
	def test_dequeueValid(self):
		Q1 = Queue(10)
		Q1.enqueue(1)
		Q1.enqueue(2)
		result = Q1.dequeue()

		assert result == 1


	def test_initValidInt2(self):
		with pytest.raises(StackCapacityTypeError):
			S = Stack('a')
			S = Stack(2.3)

	def test_initInvalidInt2(self):
		with pytest.raises(StackCapacityBoundError):
			S = Stack(-1)
			S = Stack(0)

	def test_pushInvalidFull(self):

		with pytest.raises(StackIsFull):
			S = Stack(2)
			S.push(1)
			S.push(2)
			S.push(3)

	def test_pushValid(self):
		#try to push something into the queue

		S = Stack(10)
		S.push(1)

		assert S.currentsize != 0
		assert S.head.data == 1

	def test_pushValidEmpty(self):

		s1 = Stack(10)
		result = s1.push(1)

		assert result == True
		assert s1.head.data == 1

	def test_popInvalidEmpty(self):
		with pytest.raises(StackIsEmpty):
			S = Stack(1)
			S.push(1)
			S.pop()
			S.pop()

	def test_popValid(self):
		S1 = Stack(10)
		S1.push(1)
		S1.push(2)
		result = S1.pop()

		assert result == 2
