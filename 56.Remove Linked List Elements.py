class Solution(object):
    def removeElements(self, head, val):
        dummy_head = ListNode(-1)
        dummy_head.next = head

        curr = dummy_head

        while (curr.next != None):
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return dummy_head.next
        
