class LinkedList:
	def __init__(self, val, next=None):
		self.val = val
		self.next = next
	def listappend(self, val):
		data = LinkedList(val)
		while self.next:
			self = self.next
		self.next = data

def test(head):
	head = head.next
	head = 20
	print(head)

a = LinkedList(10)
a.listappend(20)

while a:
	print(a.val)
	a = a.next
