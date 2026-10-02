# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = head

        if head == None or head.next == None:
            return False

        f = head.next

        while f is not None:
            if s == f:
                return True
            s = s.next

            if f.next is None:
                return False
            else:
                f = f.next.next
        return False