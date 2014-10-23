#@tiggreen
#Some linkedlist stuff. Week 9.

class Node:
	__slots__ = ('data', 'next')

class LinkedList:
	__slots__ = ('head', 'size')

#print the linkedlist
def printList(lst):
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

def count_iter(lst, elem):
	if lst is None:
		return None 
	cnt = 0 
	curr = lst.head
	while curr is not None:
		if curr.data == elem:
			cnt+=1
		curr = curr.next
	return cnt

def count_rec(head, elem):
	if head is None:
		return 0
	if head.data == elem:
		return 1 + count_rec(head.next, elem)
	else:
		return count_rec(head.next, elem)

def main():
	ll  = createLinkedList()
	addNode(ll, 5)
	addNode(ll, 3)
	addNode(ll, 5)
	addNode(ll, 4)

main()
	


