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

        rev_right = None
        while right:
            rn = right.next

            right.next = rev_right
            rev_right = right

            right = rn
            
        while head and rev_right:
            l_n = head.next
            r_n = rev_right.next

            head.next = rev_right
            head.next.next = l_n

            head = l_n
            rev_right = r_n
