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

	def reverseLinkedList(self):

		temp = self.head

		if temp is None:
			print("List is empty")
			return
		if temp.next == None:
			print("List has only one element")
			return

		prv = None
		cur = temp
		nxt = temp.next

		if cur != None:
			nxt = cur.next
			cur.next = prv
			pev = cur
			cur = nxt
		head = prv

	def printLinkedList(self):
		temp = self.head

		while temp != None:
			print(temp.data)
			temp = temp.next


if __name__ == '__main__':
	llist = SingleLinkedList()
	llist.printLinkedList()
	llist.push(1)
	llist.push(2)
	llist.printLinkedList()



