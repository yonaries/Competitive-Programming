# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev, curr = ListNode(None), head
        while curr:
            if curr.val==val:
                if curr==head: head=head.next
                prev.next=curr.next
            if curr.val!=val: prev=curr
            curr=curr.next
        return head