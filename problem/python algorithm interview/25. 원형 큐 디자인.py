# https://leetcode.com/problems/design-circular-queue/#

class MyCircularQueue:

	def __init__(self, k: int):
		self.deque = collections.deque()
		self.maxlen = k

	def isEmpty(self) -> bool:
		return False if len(self.deque) else True

	def enQueue(self, value: int) -> bool:
		if len(self.deque) < self.maxlen:
			self.deque.append(value)
			return True
		return False

	def deQueue(self) -> bool:
		if not self.isEmpty():
			self.deque.popleft()
			return True
		return False
	
	def Front(self) -> int:
		return -1 if self.isEmpty() else self.deque[0]

	def Rear(self) -> int:
		return -1 if self.isEmpty() else self.deque[-1]

	def isFull(self) -> bool:
		return True if len(self.deque) == self.maxlen else False