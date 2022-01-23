#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 12:36:05 2022

Program: project 0 - a complex number class
Author: Hakyung Sung
Submit date: 01/12/21
Description: a simple program that creates complex numbers and runs through different operations for them.


"""

class ComplexConstructorTypeERROR(Exception):
	pass
	'''
	an exeption raised when trying to build a complex number incorrectly
	'''

class Complex():
	'''
	It creates a complex number with the form of a+bi,
	including methods to perform basic mathematical operations.
	'''

	def __init__(self, a=0, b=0):
		'''
		The constructor for the Complex number class.
		Parameters of the 'a+bi'
			1. a (real number)
			2. b (imaginary number)
			The default value is 0 since 0 has a complex representation of 0+0i.
		'''

		if((type(a) != int) and (type(a) != float)):
			raise ComplexConstructorTypeERROR("ERROR: The 'a' part of a+bi " + "complex number must be a float or an int.")
		elif ((type(b) != int) and (type(b) != float)):
			raise ComplexConstructorTypeERROR("ERROR: The 'b' part of a+bi " + "complex number must be a float or an int.")

		self.a = a
		self.b = b


	def __str__(self):
		'''
		Returns a string representation of the complex number
		Format: "(a+bi)"
		'''
		return "(" + str(self.a) + " + " + str(self.b) + "i" + ")"


	def __add__(self, other):
		'''
		Adds two complex numbers
		Usage: number3 = number1 + number2
				number3 = number1.__add__(number2)
		Return: Returns a complex number containing the summation
		'''
		returnValue = None

		if(type(other)!= Complex): #simple type check
			raise TypeError ("Cannot use '+' operand for non-Complex types.")

		else:
			a = self.a
			b = self.b
			c = other.a
			d = other.b
			aPart = a + c
			bPart = b + d
			returnValue = Complex(aPart, bPart)
		return returnValue

	def __sub__(self, other):
		'''
		Subtracts two complex numbers
		Usage: number3 = number1 - number2
				number3 = number1.__sub__(number2)
		Return: Returns a complex number containing the subtraction
		'''
		returnValue = None

		if(type(other)!= Complex):
			raise TypeError ("Cannot use '-' operand for non-Complex types.")

		else:

			a = self.a
			b = self.b
			c = other.a
			d = other.b
			aPart = a - c
			bPart = b - d
			returnValue = Complex(aPart, bPart)
		return returnValue

	def __mul__(self, other):
		'''
		Multiplies two complex numbers
		Usage: number3 = number1 * number2
				number3 = number1.__mul__(number2)
		Return: Returns a complex number containing the multiplication
		'''
		returnValue = None

		if(type(other)!= Complex):
			raise TypeError ("Cannot use 'x' operand for non-Complex types.")

		else:
			a = self.a
			b = self.b
			c = other.a
			d = other.b
			aPart = (a*c) - (b*d)
			bPart = (b*c) + (a*d)
			returnValue = Complex(aPart, bPart)
		return returnValue

	def __truediv__(self, other):
		'''
		Divides two complex numbers
		Usage: number3 = number1 / number2
				number3 = number1.__truediv__(number2)
		Return: Returns a complex number containing the division
		'''
		returnValue = None

		if(type(other)!= Complex):
			raise TypeError ("Cannot use '/' operand for non-Complex types.")

		else:
			a = self.a
			b = self.b
			c = other.a
			d = other.b
			aPart = ((a*c) + (b+d)) / ((c*c) + (d*d))
			bPart = ((b*c) - (a*d)) / ((c*c) + (d*d))
			returnValue = Complex(aPart, bPart)
		return returnValue
