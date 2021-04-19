class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class SingleLinkedList:
	def __init__(self):
		self.head = None

	#Inserting node stating of the List	
	def push(self,data):

		newNode = Node(data)
		newNode.next = self.head
		self.head = newNode

	#Inserting node at the ending of the List
	def append(self,data):
		
		#Assign new node with data
		newNode = Node(data)
		#print(newNode.data)

		#check for first node as null is null assign new node to head
		if self.head == None:
			self.head = newNode
			return
		# store head in temprory variable
		temp = self.head
		#travel till last node to Lisked list
		while temp.next != None:
			temp = temp.next
		# Assign new node to last node
		temp.next = newNode
		#print(temp.next.data)

	def InsertNodeAt(self,data,position):
		newNode = Node(data)
		if self.head is None:
			self.head = newNode
			return

		temp = self.head
		count = 0
		while temp != None and count < position:
			temp = temp.next
			count += 1
		newNode.next = temp.next
		temp.next = newNode
		


	def printList(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next



if __name__ == '__main__':
	llist = SingleLinkedList()
	llist.append(1)
	
	llist.append(2)
	
	llist.append(3)
	llist.push(0)
	llist.InsertNodeAt(5,3)
	llist.append(4)

	#printing LL data
	llist.printList()
	
