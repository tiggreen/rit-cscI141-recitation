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
"""
def inorder(tree):
	pass

"""
Preorder traversal.
"""
def preorder(tree):
	pass

"""
Postorder traversal.
"""
def postorder(tree):
	pass
			
def main():
	tree = None
	tree = insert(tree, 5)
	tree = insert(tree, 3)
	tree = insert(tree, 4)
	tree = insert(tree, 1)
	tree = insert(tree, 7)
	tree = insert(tree, 6)
	tree = insert(tree, 9)

	inorder(tree)

if __name__ == '__main__':
	main()