from turtle import *

def drawSquare(s):
	forward(s)
	left(90)
	forward(s)
	left(90)
	forward(s)
	left(90)
	forward(s)
	left(90)
	
def drawSquares(depth, length):
	if depth < 0:
		pass
	else:
		forward(length)
		left(90)
		drawSquares(depth-1, length/3)
		forward(length)
		left(90)
		forward(length)
		left(90)
		drawSquares(depth-1, length/3)
		forward(length)
		left(90)
		
def drawSquaresModified(depth, length):
	if depth < 0:
		pass
	else:
		forward(length)
		left(90)
		drawSquaresModified(depth-1, length/3)
		forward(length)
		left(90)
		forward(length)
		left(90)
		drawSquaresModified(depth-1, length/3)
		forward(length)
		left(90)


def isPolindrome(st1):
	if len(st1) < 1:
		return True	
	elif st1[0] == st1[-1]:
		return isPolindrome(st1[1:-1])
	else:
		return False

def isPolindromeIter(st1):
	ln = len(st1)
	for ind in range(ln):
		if st1[ind] != st1[ln - ind - 1]:
			return False
	return True
	
def w():
	i =0
	s = "hello"
	for ch in s:
		print("i=", i, "ch=", ch)
		i = i + 1

def words(filename):
	nlines = 0
	nchars = 0
	for line in open(filename):
		nchars += len(line.strip())
		nlines = nlines + 1
		 
	return (nlines, nchars)
	
		 		
def m():
	sum =1 
	i = 0 
	while i < 10:
		sum = sum + i 
		i = i + 1
	print("sum=", sum, "i=", i)
	
def draw3(s, n):
	forward(s)
	left(360/n)
	forward(s)
	left(360/n)
	forward(s)
	left(360/n)

def drawP(s, n, current):
	if current < 1:
		return
	else:
		drawP(s,n, current - 1)
		forward(s)
		left(360/n)
	
def draw(s):
	forward(math.sqrt(2000))
	

def main():

	maxsize= 200
	d = int(input("Depth: "))
	pensize(2)
	drawSquaresModified(d, maxsize)
	input("hit enter to close the window!")
	#filename = input("Enter a filename now: ")
	#print(isPolindromeIter("noon"))
	#drawP(100, 5, 5)
	#w()
	#input("hit to close")
	
main()