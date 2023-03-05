# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            head = head.next
            return head
        
        length = 0 # 2
        curr = head
        
        while curr:
            curr = curr.next
            length += 1
            
        
        n = (length - n)
        curr = head
        
        # edge case if the first node is the on that should be removed
        if n == 0:
            head = head.next
            return head
        
        i = 0
        while i < n-1:
            curr = curr.next
            i += 1
        
        curr.next = curr.next.next
        
        return head