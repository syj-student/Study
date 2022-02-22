# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
	def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
		answer = head
		for _ in range(1, left):
			head  = head.next
		startNode = head
		valueBuffer = list()
		for _ in range(right - left + 1):
			valueBuffer.append(head.val)
			head = head.next
		for _ in range(right - left):
			startNode.val = valueBuffer.pop()
			startNode = startNode.next
		return answer