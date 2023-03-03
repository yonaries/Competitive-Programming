# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        refHead = None
        refCopy = refHead
        
        curr = head
        
        while curr and curr.next:
            if refHead == None: 
                refHead = curr.next
                refCopy = curr.next
            
            else:
                refCopy.next = curr.next
                refCopy = refCopy.next
            
            curr.next = curr.next.next
            if curr.next:
                curr = curr.next
        

        refCopy.next = None
        curr.next = refHead
            
        return head