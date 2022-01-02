<<<<<<< HEAD
def test():
	a = [1, 2]
	yield a
	return 1
a = test()
print(next(a))
print(next(a))
=======
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
>>>>>>> 699f601385e8a6b5b758de95f13dc8feb87eed9f
