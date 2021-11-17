# https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
class Solution:
	def insertionSortList(self, head):
		cur = start = ListNode(0)
		while head:
			while cur.next and cur.next.val < head.val:
				cur = cur.next
			cur.next, head.next, head = head, cur.next, head.next
			if head and cur.val > head.val:
				cur = start
		return start.next


a = ListNode(20)
a.next = ListNode(10)
a.next.next = ListNode(15)
b = Solution()
a = b.insertionSortList(a)
while a:
	print(a.val)
	a = a.next