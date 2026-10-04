# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = head
        f = head.next

        while f and f.next:
            s = s.next
            f = f.next.next

        right = s.next
        s.next = None

        right_rev = None
        while right:
            r_n = right.next
            right.next = right_rev
            right_rev = right
            right = r_n
        
        while head and right_rev:
            left_n = head.next
            right_n = right_rev.next

            head.next = right_rev
            head.next.next = left_n

            head = left_n
            right_rev = right_n