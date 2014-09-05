# @tiggreen
# CSCI141 Week2 Recitation

from turtle import *

def draw_crosses_1(S):
    forward(S)
    back(S)
    
def draw_crosses_2(S):
    forward(S)
    left(90)
    draw_crosses_1(S/2)
    right(90)
    draw_crosses_1(S/2)
    right(90)
    draw_crosses_1(S/2)
    left(90)
    back(S)
    
def draw_crosses_3(S):
    forward(S)
    left(90)
    draw_crosses_2(S/2)
    right(90)
    draw_crosses_2(S/2)
    right(90)
    draw_crosses_2(S/2)
    left(90)
    back(S)


# Let's put everything together
# as one recursive function. 
def draw_crosses(s,n):
	if(n <= 0):
		return 
	forward(s)
	left(90)
	draw_crosses(s/2,n-1)
	right(90)
	draw_crosses(s/2,n-1)
	right(90)
	draw_crosses(s/2,n-1)
	left(90)
	back(s)

def main():
	S = int(input("S: "))
	N = int(input("N: "))
	draw_crosses(S,N)
	input("Hit enter to close the window!")
	
main()
