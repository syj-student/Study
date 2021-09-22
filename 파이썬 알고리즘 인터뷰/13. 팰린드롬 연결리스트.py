# https://leetcode.com/problems/palindrome-linked-list/

class Solution:
	def isPalindrome(self, head: Optional[ListNode]) -> bool:
		if not head:
			return True
		deque = collections.deque()
		while head:
			deque.append(head.val)
			head = head.next
		while deque:
			try:
				if deque.popleft() != deque.pop():
					return False
			except:
				return True
		return True
