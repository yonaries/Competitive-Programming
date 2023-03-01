# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        curr = head
        index = 0
        
        while curr and curr.next:
            if (index % 2 == 0):
                temp = curr.val
                curr.val = curr.next.val
                curr.next.val = temp
            curr = curr.next
            index += 1
            
        return head
                
                