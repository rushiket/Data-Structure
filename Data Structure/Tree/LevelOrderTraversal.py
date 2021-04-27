#A node structure
class Node:
	#A utility function to create Node
	def __init__(self,key):
		self.val = key
		self.left = None
		self.right = None

#Function to print level order traversal of tree
def printLevelOrder(root):
	h = height(root)
	for i in range(1, h+1):
		printGivenLevel(root,i)

#Function to print given level
def printGivenLevel(root, level):
	
	if root is None:
		return

	if level == 1:
		pass
		print(root.val,end=" ")
	elif level > 1 :
		printGivenLevel(root.left,level-1)
		printGivenLevel(root.right,level-1)



def height(root):
	if root is None:
		return 0
	else:
		#Compute height of each sub tree
		lheight = height(root.left)
		rheight = height(root.right)

		#Use the greater one
		if lheight > rheight:
			return lheight + 1
		else:
			return rheight + 1

			# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level order traversal of binary tree is -")

printLevelOrder(root)


