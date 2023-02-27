# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:        
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        answer = head
        
        prev = head
        curr = head.next
        
        while curr:
            if (prev.val == curr.val) or (prev.val-1000 == curr.val):
                prev.val += 1000
                curr.val += 1000
            
            prev = prev.next
            curr = curr.next
            
        
        # edge case: if dupulicates comes at first
        while answer and answer.val > 100:
            answer = answer.next
            
        result = answer
        
        while answer and answer.next:
            if answer.next.val > 100:
                answer.next = answer.next.next
                
            else:
                answer = answer.next
                
        return result
            
                