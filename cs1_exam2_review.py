#@tiggreen
"""
Coded up during CS1 TA exam review. 11/1/2014.
"""
class Node:
	__slots__ = ('data', 'next')

# top is a node object
def pop(node):
	if emptyStack(node):
		raise IndexError("Stack is empty!")
	node = node.next

def push(node, elem):
	node = Node(elem, node)

def dequeue(qu):
	if emptyQueue(qu):
		raise IndexError("Queue is empty!")
	qu.front = qu.front.next
	if emptyQueue(qu):
		qu.back  = None
	qu.size -= 1 


class Pet:
	__slots__ = ('name', 'age', 'species')
	_types = (str, int, str)


def createPet(name, species):
	p = Pet()
	p.age  = 0
	p.name = name
	p.species = species
	return p


def wordSumCount(filename):
	d = {}
	for line in open(filename):
		line = line.strip()
		key_value = line.split(",")
		key = key_value[0]
		count = int(key_value[1])
		if key not in d:
			d[key] = count
		else:
			prev_count = d[key]
			curr_count = prev_count + count
			d[key] = curr_count
	
	for key in d.keys():
		print(key + " : " + str(d[key]))

wordSumCount("file.txt")		

def bsearch(lst, elem):
	if not lst:
		return False
		
	middle_index = len(lst) // 2
	print(lst[middle_index])
	if lst[middle_index] == elem:
		return True
	elif lst[middle_index] > elem:
		return bsearch(lst[:middle_index], elem)
	else:
		return bsearch(lst[middle_index+1:], elem)

class LinkedList:
	__slots__ = ('head', 'size')

#print the linkedlist
def printList(lst):
	if lst is None:
		return None
	curr = lst.head
	while curr is not None:
		print(curr.data)
		curr = curr.next
	

def createNode(d, n):
	nd = Node()
	nd.data = d
	nd.next = n
	return nd

def printReverse(head):
	if head is None:
		return None
	printReverse(head.next)
	print(head.data)
		
	
def getLast(lst):
	if lst is None:
		return None
	curr = lst.head
	while curr.next is not None:
		curr = curr.next
	
	return curr.data
	
def createLinkedList():
	ll = LinkedList()
	ll.head = None
	ll.size = 0
	return ll

def addNode(lst, nodeData):
	if lst.head is None:
		lst.head = createNode(nodeData,None)
		return lst
	hd = lst.head
	while hd.next is not None:
		hd = hd.next
	hd.next = createNode(nodeData, None)
	return hd

# returns the number of occurances of elem in ll.
def countUtil(head, elem):
	if head is None:
		return 0
	if 	head.data == elem:
		return 1 + countUtil(head.next, elem)
	else:
		return countUtil(head.next, elem)

def count(ll, elem):
	if not ll:
		return None
	return countUtil(ll.head,elem)

def countIter(ll, elem):
	if not ll:
		return None
		
	head = ll.head
	count = 0
	while head is not None:
		if head.data == elem:
			count += 1
		head = head.next
	return count
	
# return the nth to last element of a linked list.
# findNthelement(ll, 3) ==> 3
# findNthelement(ll, 1) ==> 5
def findNthelement(ll, n):
	if not ll:
		return None
	head1 = ll.head
	head2 = ll.head
	counter = 0
	while head1 is not None:
		if counter >= n:
			head2 = head2.next
		head1 = head1.next
		counter += 1
	return head2.data

def main():
	ll  = createLinkedList()
	addNode(ll, 5)
	addNode(ll, 3)
	addNode(ll, 5)
	addNode(ll, 5)
	addNode(ll, 3)
	addNode(ll, 4)
	addNode(ll, 5)
	print(findNthelement(ll,4))
main()
	


