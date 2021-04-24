class Queue:

	# __init__ function
	def __init__(self,capacity):
		self.front = self.size = 0
		self.rear = capacity - 1
		self.Q = [None]*capacity
		self.capacity = capacity
		print(self.capacity)

	# Queue is full when size becomes
    # equal to the capacity
	def isFull(self):
		return self.size == self.capacity

	# Queue is empty when size is 0
	def isEmpty(self):
		return self.size == 0

	#Function to add an item to the queue.
	#It changes rear and size
	def Enqueue(self,item):
		if self.isFull():
			print("Full")
			return
		self.rear = (self.rear + 1) % (self.capacity)
		self.Q[self.rear] = item
		self.size = self.size + 1
		print("% s Enqueued to queue" % str(item))

	def Dequeue(self):
		if self.isEmpty():
			print("Empty")
			return
		print("% s Dequeued from queue" % str(self.Q[self.front]))
		self.front = (self.front + 1) % (self.capacity)
		self.size = self.size - 1

	#Function to get front of queue
	def que_front(self):
		if self.isEmpty():
			print("Queue is empty")

		print("Front item is", self.Q[self.front])

	def que_rear(self):
		if self.isEmpty():
			print("Queue is empty")
		print("Rear item is", self.Q[self.rear])

if __name__ == '__main__':

	queue = Queue(3)
	print(queue.que_front(),queue.que_rear())
	print("*"*10)
	queue.Enqueue(10)
	queue.Enqueue(20)
	queue.Enqueue(30)
	queue.Enqueue(40)
	queue.Enqueue(50)
	queue.Dequeue()
	queue.que_front()
	queue.que_rear()




