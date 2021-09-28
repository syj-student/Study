# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
		if not lists:
			return None

		sortList = list()
		for head in lists:
			while head:
				heapq.heappush(sortList, head.val)
				head = head.next

		ret = head = ListNode()
		while sortList:
			head.next = ListNode(heapq.heappop(sortList))
			head = head.next

		return ret.next