#@tiggreen
# Draws a polygon.

from turtle import *

def draw(n,s, current):
	if current == 0:
		return
		
	draw(n,s, current - 1)
	forward(s)
	left(360/n)

def draw_iter(n,s, current):

	while current != 0:
		forward(s)
		left(360/n)
		current = current - 1

	
def main():
	n = int(input("n:"))
	s = int(input("s:"))
	if n < 3:
		print("no")
		return
		
	draw_iter(n,s,n)
	input("Please hit enter to close the window.")

main()