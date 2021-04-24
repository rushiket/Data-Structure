class CircularQueue:
	# constructor
	def __init__(self,size):
		self.size = size
		#initializing queue with none
		self.queue = [None for i in range(size)]
		self.front = self.rear = -1

	def enqueue(self,data):
		#condition if queue is full
		if ((self.rear+1) % self.size == self.front):
			print("Queue is Full\n")
		# conditoin for empty queue
		elif (self.front == -1):
			self.front = 0
			self.rear = 0
			self.queue[self.rear] = data
		else:
			self.rear = (self.rear + 1) % self.size
			self.queue[self.rear] = data

	def dequeue(self):
		#conditon for empty queue
		if(self.front == -1):
			print("Queue is empty \n")
		elif (self.rear == self.front):
			temp = self.queue[self.front]
			self.front = -1
			self.rear = -1
			return temp
		else:
			temp = self.queue[self.front]
			self.front = (self.front + 1) % self.size
			return temp

	def display(self):

		#conditon for empty queue
		if (self.front == -1):
			print("Queue is empty \n")
		elif (self.rear >= self.front):
			print("Element in the circular queue are:",end = " ")
			for i in range(self.front, self.rear+1):
				print(self.queue[i],end=" ")
			print ()
		else:
			print("Element in the circular queue are:",end = " ")
			for i in range(self.front, self.size):
				print(self.queue[i], end = " ")
			for i in range(0, self.rear+1):
				print(self.queue[i],end = " ")
			print ()

		if ((self.rear + 1)% self.size == self.front):
			print("Queue is Full")

if __name__ == "__main__":
	ob = CircularQueue(5)
	ob.enqueue(2)
	ob.enqueue(2)
	ob.enqueue(3)
	ob.enqueue(4)
	ob.enqueue(5)
	ob.display()
	print("*"*10)
	ob.enqueue(6)
	ob.dequeue()
	ob.dequeue()
	ob.display()
	ob.dequeue()
	ob.dequeue()












