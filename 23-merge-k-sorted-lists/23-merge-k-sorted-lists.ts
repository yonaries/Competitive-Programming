/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
        if (lists.length === 0) {
        return null;
    }
    
    let result = new ListNode(-Infinity);
    let temp = result;
    
    let current = lists.shift();
    let merged = mergeKLists(lists);
    
    if (merged === null) {
        temp.next = current;
        return result.next;
    }
    
    while (merged || current) {
        if (merged === null) {
            temp.next = current;
            break;
        }
        
        if (current === null) {
            temp.next = merged;
            break;
        }
            
        if (merged.val < current.val) {
            temp.next = new ListNode(merged.val);
            
            temp = temp.next;
            merged = merged.next;
        } else if (merged.val === current.val) {
            temp.next = new ListNode(merged.val, new ListNode(current.val));
            temp = temp.next.next;
            
            merged = merged.next;
            current = current.next;
        } else if (merged.val > current.val) {
            temp.next = new ListNode(current.val);
            
            temp = temp.next;
            current = current.next;
        }
    }
    
    return result.next;
};