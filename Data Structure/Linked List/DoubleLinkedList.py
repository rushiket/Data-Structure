class Node:
	def __init__(self,data):
		self.data=data
		self.next = None
		self.prev = None

class DoubleLinkedList:

	def __init__(self):
		self.head = None

	def append(self,data):
		'''
		new_node = Node(data)
		new_node.next = self.head
		new_node.prev = None
		if self.head is not None:
			self.head.prev = new_node
		self.head = new_node

		'''
		newNode = Node(data)
		if self.head is None:
			self.haed = newNode
			return

		newNode.next = self.head
		newNode.prev = None
		
		if self.head is not None:
			self.head.prev = newNode
		self.head = newNode
		

	def push(self,data):
		newNode = Node(data)

		if self.head is None:
			self.head = newNode
			return

		head = self.head
		temp = head
		while temp.next != None:
			temp = temp.next
		temp.next = newNode
		newNode.prev = temp

	def printList(self):
		temp = self.head
		if temp is None:
			print("None")
		while temp:
			print(temp.data)
			temp = temp.next

if __name__ == '__main__':

	dlist = DoubleLinkedList()
	dlist.push(1)
	dlist.push(2)
	dlist.push(3)
	dlist.append(0)
	dlist.printList()


