#@tiggreen
#Some linkedlist stuff. Week 9.

class Node:
	__slots__ = ('data', 'next')

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

def count_iter(lst, elem):
	if lst is None:
		return None
	curr = lst.head
	count = 0
	while curr is not None:
		if curr.data == elem:
			count += 1 
		curr = curr.next
	return count

def count_rec(lst,elem):
	if lst is None:
		return None
	return count_rec_util(lst.head, elem)

def count_rec_util(head, elem):
	if head is None:
		return 0
	if head.data == elem:
		return 1 + count_rec_util(head.next, elem)
	else:
		return count_rec_util(head.next, elem)

def remove_rec(lst, elem):
	if lst is None:
		return None
	if lst.head.data == elem:
		lst.head = lst.head.next
		return lst
	else:
		remove_rec_util(lst.head, elem)
		return lst

def remove_rec_util(head, elem):
	if head is None:
		return None
	if head.next is None:
		return None
	if head.next.data == elem:
		head.next = head.next.next
	else:
		return remove_rec_util(head.next, elem)

def main():
	ll  = createLinkedList()
	addNode(ll, 5)
	addNode(ll, 3)
	addNode(ll, 5)
	addNode(ll, 5)
	addNode(ll, 3)
	addNode(ll, 4)
	addNode(ll, 5)
	printList(remove_rec(ll, 3))
	#printList(ll)
	
main()
	


