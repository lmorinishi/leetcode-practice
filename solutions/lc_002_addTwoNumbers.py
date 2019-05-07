class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = 0
        sumlist = tmplist = ListNode(0)
        while l1 or l2 or cur:
            if l1:
                cur += l1.val
                l1 = l1.next
            if l2:
                cur += l2.val
                l2 = l2.next

            cur, remainder = divmod(cur, 10)
            tmplist.next = ListNode(remainder)
            tmplist = tmplist.next
            
        return sumlist.next
