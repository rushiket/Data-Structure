class Stack():
	def __init__(self):
		self.items = []

	def push(self,item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def _isempty(self):
		return self.items == []

	def peek(self):
		if not self._isempty():
			return self.items[-1]

	def get_stack(self):
		return self.items


s = Stack()
