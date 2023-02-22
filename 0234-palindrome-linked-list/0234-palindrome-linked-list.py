# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        string = ""
        
        while head:
            string += str(head.val)
            head = head.next
        
        left = 0
        right = len(string)-1
        
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
            
        return True
        