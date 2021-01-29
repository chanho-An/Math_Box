# 기본 계산기
def abb(a, b):
	return a + b

def substract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide_new(a, b):
	return a / b

def square(a, b):
	return a ** b

def get_Percent(a, b):
	return (a / b) * 100

def remainder(a, b):
	return a // b

def get_Median(a, b):
	return (a + b) / 2

def test():
	return None

def get_Sum(n):
	return n(n + 1) / 2

def factorial(n):
	num = 1
	while n >= 1:
		num = num * n
		n = n -1
	return num
