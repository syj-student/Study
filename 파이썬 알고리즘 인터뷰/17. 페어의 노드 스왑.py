# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
	def swapPairs(self, head):
		prev_node = None
		tmp_head = head
		while tmp_head:
			if not prev_node:
				prev_node = tmp_head
			else:
				tmp = prev_node.val
				prev_node.val = tmp_head.val
				tmp_head.val = tmp
				prev_node = None
			tmp_head = tmp_head.next

class node:
	def __init__(self, val, next=None):
		self.val = val
		self.next = next

def test(head):
	head = None

number = 10
test(number)
print(number)

a = node(10)
test(a)
print(a.val)