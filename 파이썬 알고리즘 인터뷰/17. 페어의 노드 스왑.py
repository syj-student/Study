# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
	def swapPairs(self, head):
		prev_node = None
		answer = head
		while head:
			if prev_node == None:
				prev_node = head
			else:
				tmp = prev_node.val
				prev_node.val = head.val
				head.val = tmp
				prev_node = None
			head = head.next
		return answer
 