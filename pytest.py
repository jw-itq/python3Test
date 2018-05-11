#! /usr/bin/python
row = "+-----"
def row1():
	for i in range(4):
		print(row,end="")
	print("+")
def col1():
	for i in range(4):
		for i in range(4):
			print("|    ",end=" ")
		print("|")
for i in range(4):
	row1()
	col1()
row1()
