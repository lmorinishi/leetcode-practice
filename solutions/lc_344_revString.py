class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # list reverse
        # s.reverse()

        # list slice
        # s[::-1]

        # iterate half list, swap
        for i in range(int(len(s)/2)):
            s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]

        # progressively inner string
        # def reverseStringRecurse(i, j) -> None:
        #     if i < j:
        #         s[i], s[j] = s[j], s[i]
        #         reverseStringRecurse(i+1, j-1)
        #
        # reverseStringRecurse(0, len(s)-1)
