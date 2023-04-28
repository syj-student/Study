from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def convert_to_int(self, l1: Optional[ListNode]) -> int:
        ret = 0
        i = 0
        while l1:
            ret = ret + l1.val * 10 ** i
            l1 = l1.next
            i += 1
        return ret

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s = self.convert_to_int(l1) + self.convert_to_int(l2)
        answer = head = ListNode()
        for c in reversed(str(s)):
            now = ListNode(val=int(c))
            head.next = now
            head = now
        return head.next.next
    
print(Solution().addTwoNumbers(ListNode(val=0), ListNode(val=0)).val)