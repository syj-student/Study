# https://leetcode.com/problems/sort-list/#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		tmp = list()
		node = head
		while node:
			tmp.append(node.val)
			node = node.next
		tmp.sort()
		node = head
		for i in tmp:
			node.val = i
			node = node.next
		return head

class Solution:
	def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		if head is None:
			return
		half, slow, fast = head, head, head
		while fast and fast.next:
			half, slow, fast = slow, slow.next, fast.next.next
		half.next = None
		l1 = self.sortList(head)
		l2 = self.sortList(slow)
		root = node = ListNode()
		while l1 or l2:
			if l2 is None or (l1 and l2 and l1.val <= l2.val):
				node.next = l1
				l1 = l1.next
				node = node.next
			else:
				node.next = l2
				l2 = l2.next
				node = node.next
		return root.next