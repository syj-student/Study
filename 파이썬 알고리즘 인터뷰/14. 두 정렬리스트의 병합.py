# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def __append(self, head, val):
		data = ListNode(val)
		ret = head
		if not head:
			return data
		while head.next:
			head = head.next
		head.next = data
		return ret

	def mergeTwoLists(self, l1, l2):
		ret = None
		while l1 or l2:
			if l1.val >= l2.val:
				ret = self.__append(ret, l2.val)
				l2 = l2.next
			else:
				ret = self.__append(ret, l1.val)
				l1 = l1.next
		tmp = l1 if l1 else l2
		while tmp:
			ret = self.__append(ret, tmp.val)
			tmp = tmp.next
		return ret

#class Solution:
#	def mergeTwoLists(self, l1, l2):
#		if (not l1) or (l2 and l1.val > l2.val):
#			l1, l2 = l2, l1
#		if l1:
#			l1.next = self.mergeTwoLists(l1.next, l2)
#		return l1

l1 = ListNode(10)
l2 = ListNode(20)
sol = Solution()
tmp = sol.mergeTwoLists(l1, l2)
while tmp:
	print(tmp.val)
	tmp = tmp.next
