# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		def makeNumber(head):
			num = collections.deque()
			while head:
				num.appendleft(str(head.val))
				head = head.next
			return ''.join(num)

		x = str(eval(makeNumber(l1) + '+' + makeNumber(l2)))
		answer = head = ListNode()
		for i in range(len(x)-1, -1, -1):
			head.next = ListNode(int(x[i]))
			head = head.next
		return answer.next