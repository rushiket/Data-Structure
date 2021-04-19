class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class SingleLinkedList:
	def __init__(self):
		self.head = None



#creating linked list
llist = SingleLinkedList()

#Assigning value to head of list
llist.head = Node(1)

#Assigning value to next node of list i.e. a
a = Node(2)
#Assigning value to next node of list i.e. b
b = Node(3)

llist.next = a
a.next = b

#print data of each node
print(llist.head.data)
print(a.data)
print(b.data)





