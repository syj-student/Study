# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
	def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
		answer = new_node = ListNode()
		stack = list()
		while head:
			if len(stack) == k:
				while stack:
					new_node.next = ListNode()
					new_node =  new_node.next
					new_node.val = stack.pop()
			stack.append(head.val)
			head = head.next
		if len(stack) == k:
			while stack:
				new_node.next = ListNode()
				new_node =  new_node.next
				new_node.val = stack.pop()
		else:
			for c in stack:
				new_node.next = ListNode()
				new_node =  new_node.next
				new_node.val = c
		return answer.next

class Solution:
	def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
		def reverse_linked_list(head, stack):
			while stack:
				head.val = stack.pop()
				head = head.next

		stack = list()
		while head:
			cnt = k
			tmp = head
