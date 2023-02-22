# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newList = None
        
        while head:
            if not newList:
                newList = ListNode(head.val)
            else:
                node = ListNode(head.val)
                node.next = newList
                newList = node
            
            head = head.next
        
        return newList