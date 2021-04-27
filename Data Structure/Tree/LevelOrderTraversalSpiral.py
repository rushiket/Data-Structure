#A structre of node
class Node:
	#A utility function of Node
	def __init__(self,key):
		self.val = key
		self.left = None
		self.right = None

#Function to print tree in spiral order
def printSpiral(root):
	if root is None:
		return 
	#Create Two stack 
	#To store alternate level

	#For the level to be printed from right to left.
	stack1 = []
	#For the level to be printed from left to right.
	stack2 = []

	# append root node to stack 1
	stack1.append(root)

	#keep printing while stack has some node

	while len(stack1) > 0 or  len(stack2) > 0:

		# Print tree from right to left
		while len(stack1) > 0:

			#print top of the stack
			print(stack1[-1].val, end=" ")

			#pop top node from stack and 
			#Assign to node variable
			node = stack1.pop()

			#Append right most node first in stack 
			if node.right is not None:
				stack2.append(node.right)

			#Append left of node in stack
			if node.left is not None:
				stack2.append(node.left)

		while len(stack2) > 0:

			#print top of the stack
			print(stack2[-1].val, end=" ")

			#pop top node from stack and 
			#Assign to node variable
			node = stack2.pop()

			#Append left of node in stack
			if node.left is not None:
				stack1.append(node.left)

			#Append right most node first in stack 
			if node.right is not None:
				stack1.append(node.right)

# Driver Code
if __name__ == '__main__':
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(7) 
    root.left.right = Node(6) 
    root.right.left = Node(5) 
    root.right.right = Node(4) 
    print("Spiral Order traversal of",
                    "binary tree is ") 
    printSpiral(root)




