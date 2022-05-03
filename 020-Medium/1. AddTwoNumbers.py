# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        
        cl1 = l1
        cl2 = l2

        curr = ListNode()
        
        cur = curr
        while cl1 is not None or cl2 is not None:
            n1 = cl1.val if cl1 is not None else 0
            n2 = cl2.val if cl2 is not None else 0
            
            cur_val = (n1 + n2 + carry) % 10
            
            carry = (n1 + n2 + carry) // 10

            nxt = ListNode(val=cur_val)

            cur.next = nxt

            cur = nxt
            
            if cl1 is not None:
                cl1 = cl1.next
            if cl2 is not None:
                cl2 = cl2.next
            
        if carry > 0:
            cur.next = ListNode(val=carry)
        
        return curr.next
