# https://leetcode.com/problems/palindrome-linked-list/

class Solution:
	def isPalindrome(self, head: Optional[ListNode]) -> bool:
		if not head:
			return True
		deque = collections.deque()
		while head:
			deque.append(head.val)
			head = head.next
		while len(deque) > 1:
			if deque.popleft() != deque.pop():
				return False
		return True
