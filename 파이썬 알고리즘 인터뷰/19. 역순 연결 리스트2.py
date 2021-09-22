# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
	def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
		answer, startNode = head, None
		for i in range(1, left):
			head  = head.next
		return answer