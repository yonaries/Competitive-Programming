# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        length = 0
        curr = head
        
        while curr:
            curr = curr.next
            length += 1
        
        maxSum = -inf
        pairs = {} 
        
        i = 0
        while head:
            if i <= (length/2)-1:
                pairs[length-1-i] = head.val
                
            else:
                maxSum = max(maxSum, (pairs[i] + head.val))
            
            i += 1
            head = head.next
            
        return maxSum