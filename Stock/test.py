#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def test(head):
    head.val = 10

a = ListNode()
print(a.val)
test(a)
print(a.val)
