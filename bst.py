# @tigreen

"""
 A class representing a Binary Search Tree (BST). 
"""
 
class BinaryTree():
	__slots__ = ('data', 'left', 'right')

"""
Creating a new BinaryTree object.
"""
def create_bt(data, left, right):
	bt = BinaryTree()
	bt.data = data
	bt.left = left
	bt.right = right
	return bt


"""
Insert a new node into a binary search tree.
"""
def insert(tree, data):
	if tree is None:
		tree = create_bt(data, None, None)
	elif data <= tree.data:
		tree.left = insert(tree.left, data)
	else:
		tree.right = insert(tree.right, data)
	return tree

"""
Inorder traversal.

We can also implement inorder this way if we want to
return a string as a result.
"""
def inorder(tree):
	result = ''
	if tree is None:
		return ''

	result = inorder(tree.left) + str(tree.data) +  " " + inorder(tree.right)
	return result
	

"""
Preorder traversal.
"""
def preorder(tree):
	if tree is None:
		return
	print(tree.data)
	preorder(tree.left)
	preorder(tree.right)

"""
Postorder traversal.
"""
def postorder(tree):
	if tree is None:
		return
	postorder(tree.left)
	postorder(tree.right)
	print(tree.data)
	
			
def main():
	tree = None
	tree = insert(tree, 7)
	tree = insert(tree, 5)
	tree = insert(tree, 4)
	tree = insert(tree, 6)
	tree = insert(tree, 9)
	tree = insert(tree, 8)
	tree = insert(tree, 10)
	print(inorder(tree))

if __name__ == '__main__':
	main()