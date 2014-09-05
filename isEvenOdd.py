#@tiggreen
import sys

# Returns True if the number is even.
def isEven(n):
	return n%2 == 0

def main():
	if len(sys.argv) != 2:
		print "Usage: python isEvenOdd.py number"
		return
	
	user_input = int(sys.argv[1])
	if isEven(user_input):
		print "The input number is even."
	else:
		print "The input number is odd."	
main()


