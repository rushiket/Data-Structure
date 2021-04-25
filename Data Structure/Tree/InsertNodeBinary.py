#creating new Node for
#Binary Search Tree

class Node:
	#Assign value to node properties
	def __init__(self,key):
		self.val = key
		self.left = None
		self.right = None

def inorder(temp):

	if temp is None:
			return
	inorder(temp.left)
	print(temp.val, end =" ")
	inorder(temp.right)

	#Inserting values in binary tree
def insert(temp,key):

		if not temp:
			root  = Node(key)
			return
		q = []
		q.append(temp)

		#Do level order traversal until we find 
		#an empty place.
		while (len(q)):
			temp = q[0]
			q.pop(0)

			if (not temp.left):
				temp.left = Node(key)
				break
			else:
				q.append(temp.left)

			if (not temp.right):
				temp.right = Node(key)
				break
			else:
				q.append(temp.right)


#Driver Code
if __name__ == "__main__":
	root = Node(10)
	root.left = Node(11)
	root.left.left = Node(7)
	root.right = Node(9)
	root.right.left = Node(15)
	root.right.right = Node(8)

	print("Inorder traversal before insertion:", end = " ")
	inorder(root)

	key = 12
	insert(root,key)

	print("\n\nInorder traversal after insertion:", end = " ")
	inorder(root)





