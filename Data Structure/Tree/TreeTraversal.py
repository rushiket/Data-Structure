class Node:
	def __init__(self,key):
		self.val = key
		self.left = None
		self.right = None

def InOrder(temp):

	if temp == None:
		return
	InOrder(temp.left)
	print(temp.val,end = " ")
	InOrder(temp.right)

def PreOrder(temp):

	if temp == None:
		return
	print(temp.val,end = " ")
	InOrder(temp.left)
	InOrder(temp.right)

def PostOrder(temp):

	if temp == None:
		return
	InOrder(temp.left)
	InOrder(temp.right)
	print(temp.val,end = " ")

if __name__ == "__main__":
	tree = Node(10)
	tree.left = Node(9)
	tree.right = Node(11)
	tree.left.left = Node(7)
	tree.left.right = Node(8)
	print("\n This is Inorder traversal")
	InOrder(tree)
	print("\n This is PreOrder traversal")
	PreOrder(tree)
	print("\n This is PostOrder traversal")
	PostOrder(tree)


