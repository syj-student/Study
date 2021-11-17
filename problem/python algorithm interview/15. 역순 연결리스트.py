# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		data = list()
		tmp = head
		while tmp:
			data.append()
			tmp = tmp.next
		tmp = head
		for i in range(len(data) - 1, -1, -1):
			tmp.val = data[i]
			tmp = tmp.next
		return head
