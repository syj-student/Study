# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def __append(self, head, val):
		data = ListNode(val)
		if not head:
			head = data
			return
		while head.next:
			head = head.next
		head.next = data
		print(head)

	def mergeTwoLists(self, l1, l2):
		ret = None
		while l1 and l2:
			if not l1 or l1.val >= l2.val:
				self.__append(ret, l2.val)
				#print(ret.val)
				l2 = l2.next
			else:
				self.__append(ret, l1.val)
				#print(ret.val)
				l1 = l1.next
		#while l2:
		#	self.__append(ret, l2.val)
		#	l2 = l2.next
		#while l1:
		#	self.__append(ret, l1.val)
		#	l1 = l1.next
		return None

l1 = ListNode(10)
l2 = ListNode(20)
sol = Solution()
tmp = sol.mergeTwoLists(l1, l2)
print(tmp)
