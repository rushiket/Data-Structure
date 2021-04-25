# class represent individual node in
# Binary Tree
class Node:
	def __init__(self,key):
		self.right = None
		self.left = None
		self.val = key



	#create node
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)


