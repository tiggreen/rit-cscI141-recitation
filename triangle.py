# @tiggreen

from turtle import *
import sys

def triangle(side):
	forward(side)
	left(120)
	forward(side)
	left(120)
	forward(side)
	left(120)

def main():
		
	if len(sys.argv) > 2:
		raw_input("Usage: python triangle triangleside")
		return 
		
	side = int(sys.argv[1])
	
	triangle(side)
	left(90)
	triangle(side)
	left(90)
	triangle(side)
	left(90)
	triangle(side)
	left(90)
	raw_input("Hit enter to close the window!")

main()
