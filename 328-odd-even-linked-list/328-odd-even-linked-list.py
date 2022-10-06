# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next :
            return head
        
        odd, even = head, head.next
        firstEven = head.next
        
        node = even.next
        i = 3
        while node :
            if i & 1 :
                odd.next = node
                odd = node
            else :
                even.next = node
                even = node
            node = node.next
            i += 1
        
        odd.next = firstEven
        even.next = None
        
        return head