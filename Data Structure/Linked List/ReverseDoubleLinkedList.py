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

	def InserNodeAt(self,data,position):

		newNode = Node(data)
		if self.head is None:
			self.head = newNode
			return
		temp = self.head
		if position < 1:
			print("\n Position should not < 1")
			return
		if position == 1:
			newNode.next = self.head
			self.head.prev = newNode
			self.head = newNode
		else:
			temp = self.head
			for i in range(1,position-1):
				if temp is not None:
					temp  = temp.next

			if temp != None:

				newNode.next = temp.next
				newNode.prev = temp
				temp.next = newNode
				if newNode.next != None:
					newNode.next.prev = newNode
			

	def deleteNode(self,node):
		cur = self.head
		while cur:
			if cur == self.head and cur.data == node:
				if not cur:
					cur = None
					self.head = None
					return None
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

					cur.prev = None
					prv.next = None
					cur = None
					return

			cur = cur.next

					
	def reverseList(self):
		if self.head is None:
			return
		cur = self.head
		temp = None
		
		while cur :
			temp = cur.prev
			cur.prev = cur.next
			cur.next = temp
			cur = cur.prev
		print(temp.data,temp.prev.data)
		if temp:
			self.head = temp.prev


	def printList(self):

		if self.head is None:
			return self.head.data

		temp = self.head
		while temp is not None:
			print(temp.data)
			temp = temp.next



if __name__ == "__main__":

	dllist = DoubleLinkedList()
	dllist.push(1)
	dllist.push(2)
	dllist.push(3)
	dllist.InserNodeAt(4,4)
	dllist.InserNodeAt(0,1)
	dllist.InserNodeAt(100,3)
	dllist.deleteNode(100)
	dllist.deleteNode(0)
	dllist.deleteNode(4)
	dllist.printList()
	print("*"*20)
	dllist.reverseList()

	dllist.printList()



