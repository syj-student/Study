# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		evenNode = oddNode = answer = evenHead = None
		i = 1
		while head:
			if i % 2:
				if oddNode is None:
					answer = oddNode = head
				else:
					oddNode.next = head
					oddNode = head
			else:
				if evenNode is None:
					evenHead = evenNode = head
				else:
					evenNode.next = head
					evenNode = head
			head = head.next
			i += 1
		if oddNode:
			oddNode.next = evenHead
		else:
			oddNode = evenHead
		if evenNode:
			evenNode.next = None
		return answer