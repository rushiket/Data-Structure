class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class SingleLinkedList:
	def __init__(self):
		self.head = None

	def push(self,data):

		newNode = Node(data)
		newNode.next = self.head
		self.head = newNode

	def deleteNode(self,data):
		head = self.head
		if head is None:
			print("Can't delete Node List is empty")
			return
		if head.data == data:
			head.data = None
			return

		temp = head
		while temp.next.data != data:
			temp = temp.next

		temp.next = temp.next.next
	def deleteHeadNode(self):
		if self.head is None:
			return None

		temp = self.head
		self.head = self.head.next
		temp = None
		return self.head

	def deleteNodeAtPosition(self,position):
		head = self.head

		if head is None:
			print("Can't delete Node List is empty")
			return

		temp = head		
		count = 1
		while temp != None and count < position:
				temp = temp.next
				count += 1

		temp.next = temp.next.next


	def printList(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next
if __name__ == '__main__':

	llist = SingleLinkedList()
	print(llist.head)
	llist.push(1)
	llist.push(2)
	llist.push(3)
	llist.push(4)
	
	llist.deleteHeadNode()
	print("*"*10)
	llist.printList()
	









