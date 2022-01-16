#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 21:30:36 2022

@author: hakyungsung
"""

from project0 import *
import pytest

class TestMain:
	
	def test_addValid(self):
		
		number1 = Complex(2, 3)
		number2 = Complex(4, 7)
		number3 = number1+number2
		
	def test_addNone(self):
		number1= Complex(2,3)
		number2 = None
		
		with pytest.raises(TypeError):
			number3 = number1+number2
			
	def test_addInvalid(self):
		""" Tests if correct exception raised for invalid add call """
		number1 = Complex(2,3)
		number2 = "hi"
		
		with pytest.raises(TypeError):
			number3 = number1+number2
			
			
	def test_subValid(self):
		
		number1 = Complex(2, 3)
		number2 = Complex(4, 7)
		number3 = number1-number2
		
	def test_subNone(self):
		number1= Complex(2,3)
		number2 = None
		
		with pytest.raises(TypeError):
			number3 = number1-number2
			
	def test_subInvalid(self):
		""" Tests if correct exception raised for invalid add call """
		number1 = Complex(2,3)
		number2 = "hi"
		
		with pytest.raises(TypeError):
			number3 = number1-number2

	def test_mulValid(self):
		
		number1 = Complex(2, 3)
		number2 = Complex(4, 7)
		number3 = number1*number2
		
	def test_mulNone(self):
		number1= Complex(2,3)
		number2 = None
		
		with pytest.raises(TypeError):
			number3 = number1*number2
			
	def test_mulInvalid(self):
		""" Tests if correct exception raised for invalid add call """
		number1 = Complex(2,3)
		number2 = "hi"
		
		with pytest.raises(TypeError):
			number3 = number1*number2


	def test_divValid(self):
		
		number1 = Complex(2, 3)
		number2 = Complex(4, 7)
		number3 = number1/number2
		
	def test_divNone(self):
		number1= Complex(2,3)
		number2 = None
		
		with pytest.raises(TypeError):
			number3 = number1/number2
			
	def test_divInvalid(self):
		""" Tests if correct exception raised for invalid add call """
		number1 = Complex(2,3)
		number2 = "hi"
		
		with pytest.raises(TypeError):
			number3 = number1/number2