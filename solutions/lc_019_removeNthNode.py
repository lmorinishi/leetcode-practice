class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curr = check = head
        for i in range(n):
            check = check.next
        if check is None:
            head = head.next
            return head
        while check.next is not None:
            curr = curr.next
            check = check.next
        if n == 1:
            curr.next = None
        else:
            curr = curr.next
            curr.val = curr.next.val
            curr.next = curr.next.next
        return head
