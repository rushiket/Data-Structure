class newNode:
	def __init__(self,key):
		self.data = key
		self.right = None
		self.left = None
		self.hd = 0

def TopView(root):

	if root is None:
		return 

	q =[]
	m = {}
	hd = 0

	root.hd = hd

	q.append(root)

	while len(q)>0:

		root = q[0]
		hd = root.hd

		if hd not in m:
			m[hd] = root.data

		if(root.left):
			q.append(root.left)
			root.left.hd = hd - 1

		if(root.right):
			q.append(root.right)
			root.right.hd = hd + 1

		q.pop(0)
	print(sorted(m))
	for i in sorted(m):
		print(m[i],end =" ")

if __name__ == "__main__":

    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.right = newNode(4)
    root.left.right.right = newNode(5)
    root.left.right.right.right = newNode(6)
    print("Following are nodes in top",
          "view of Binary Tree")
    TopView(root)




