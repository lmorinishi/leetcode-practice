class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # iteratively
        # prev = None
        # while head:
        #     curr = head
        #     head = head.next
        #     curr.next = prev
        #     prev = curr
        # return curr

        # recursively
        return self.reverse_me(head)

    def reverse_me(self, node, previous=None):
        if not node:
            return previous
        next_node = node.next
        node.next = previous
        return self.reverse_me(next_node, node)
