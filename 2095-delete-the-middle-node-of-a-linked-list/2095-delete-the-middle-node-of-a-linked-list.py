# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            head = head.next
            return head
        
        length = 0
        curr = head
        
        while curr:
            curr = curr.next
            length += 1
        
        mid = length // 2
        
        curr = head
        for i in range(mid):
            if (i+1) == mid:
                curr.next = curr.next.next
                return head
            curr = curr.next
            
        return head