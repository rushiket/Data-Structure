class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		self.prev = None

class DoubleLinkedList:
	def __init__(self):
		self.head = None


	def push(self,data):
		newNode = Node(data)
		if self.head is None:
			self.head = newNode
			return

		temp = self.head
		while temp.next is not None:
			temp = temp.next

		temp.next = newNode
		newNode.prev = temp

	def append(self,data,position):
		newNode = Node(data)
		if self.head is None:
			self.head = newNode
			return 
		if position < 1:
			print("\n Position should be >= 1.")
		elif(position == 1):
			newNode.next = self.head
			self.head.prev = newNode
			self.head =  newNode
		else:
			temp = self.head
			for i in range(1,position-1):
				if(temp is not None):
					temp = temp.next

			if(temp != None):
				newNode.next = temp.next
				newNode.prev = temp
				temp.next = newNode
				if (newNode.next != None):
					newNode.next.prev = newNode
				else:
					print("\n The Next node is null.")



	def deleteNode(self,node):
		cur = self.head
		while cur:
			if cur.data == node and cur == self.head:
				if not cur.next:

					cur = None
					self.head = None
					return
				else:
					nxt = cur.next
					cur.next = None
					nxt.prev = None
					cur = None
					self.head = nxt
					return 

			elif cur.data == node:

				if cur.next:
					nxt = cur.next
					prv = cur.prev

					prv.next = nxt
					nxt.prev = prv

					cur.next = None
					cur.prev = None
					cur = None
					return 
				else:

					 prv = cur.prev
					 prv.next = None
					 cur.prev = None
					 cur = None
					 return
			cur = cur.next

	def printList(self):

		if self.head is None:
			return "None"
		temp = self.head
		while temp is not None:
			print(temp.data)
			temp = temp.next

if '__main__' == __name__:

	dllist = DoubleLinkedList()

	print("#"*15)
	dllist.push(1)
	dllist.push(2)
	dllist.push(3)
	dllist.append(4,4)
	dllist.printList()
	print("#"*15)
	dllist.append(5,5)
	dllist.printList()
	print("#"*15)
	dllist.append(6,1)
	dllist.printList()
	print("#"*15)
	dllist.deleteNode(6)
	dllist.deleteNode(4)
	dllist.deleteNode(5)
	dllist.printList()
	print("#"*15)