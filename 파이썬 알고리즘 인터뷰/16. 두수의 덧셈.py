# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		l1_Number = ''
		l2_Number = ''
		while l1 or l2:
			if not l1:
				l1_Number += str(l1.val)
				l1 = l1.next
			if not l2:
				l2_Number += str(l2.val)
				l2 = l2.next
		ret_Number = list(map(int, reversed(str(int(l1_Number) + int(l2_Number)))))
		head = tmp
		for i in ret_Number:
			tmp = ListNode(i)
			tmp = tmp.next
		return head
