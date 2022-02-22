# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:
	
	def __init__(self):
		self.que = collections.deque()

	def push(self, x: int) -> None:
		self.que.append(x)

	def pop(self) -> int:
		return self.que.popleft()

	def peek(self) -> int:
		return self.que[0]

	def empty(self) -> bool:
		return True if self.que else False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()