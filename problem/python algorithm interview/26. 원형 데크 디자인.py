# https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:

	def __init__(self, k: int):
		self.deque = collections.deque()
		self.maxlen = k

	def isEmpty(self) -> bool:
		return False if len(self.deque) else True

	def insertFront(self, value: int) -> bool:
		if len(self.deque) < self.maxlen:
			self.deque.appendleft(value)
			return True
		return False

	def insertLast(self, value: int) -> bool:
		if len(self.deque) < self.maxlen:
			self.deque.append(value)
			return True
		return False

	def deleteFront(self) -> bool:
		if not self.isEmpty():
			self.deque.popleft()
			return True
		return False

	def deleteLast(self) -> bool:
		if not self.isEmpty():
			self.deque.pop()
			return True
		return False

	def getFront(self) -> int:
		return -1 if self.isEmpty() else self.deque[0]

	def getRear(self) -> int:
		return -1 if self.isEmpty() else self.deque[-1]

	def isFull(self) -> bool:
		return True if len(self.deque) == self.maxlen else False
		