class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = step = out = None
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        while l1 and l2:
            if l1.val < l2.val:
                curr = l1
                l1 = l1.next
            else:
                curr = l2
                l2 = l2.next
            if step:
                step.next = curr
                step = step.next
            else:
                step = curr
                out = step

        while l1:
            step.next = l1
            step = step.next
            l1 = l1.next
        while l2:
            step.next = l2
            step = step.next
            l2 = l2.next
        return out

