#Create Structure of Node
class Node:
	#A utility function to create Node
	def __init__(self,key):
		self.val = key
		self.left = None
		self.right = None

def printLevelOrder(root):
	# Base Case
	if root is None:
		return

	#create empty queue
	q = []

	#Enqueue root and initialize height
	q.append(root)

	while(len(q) > 0):

		#Print front of the queue
		#remove it from queue

		print(q[0].data)
		node = q.pop(0)

		#Enqueue left child 
		if node.left is not None:
			q.append(node.left)

		#Enqueue right child
		if node.right is not None:
			q.append(node.right)

#Driver Program to test above function

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print ("Level Order Traversal of binary tree is -")
printLevelOrder(root)














