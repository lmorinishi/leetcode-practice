class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Original try, memory error
        # s = s.strip()
        # s = [k.upper() for k in s.strip() if k.isalnum()]  # problematic line
        # if len(s) <= 1:
        #     return True
        #
        # def getPal(t: List[str]) -> bool:
        #     print(t)
        #     if len(t) <= 1:
        #         return True
        #     if t[0] == t[-1]:
        #         return getPal(t[1:-1:1])
        #     else:
        #         return False
        # return getPal(s)

        if len(s) <= 1:
            return True

        lo, hi = 0, len(s) - 1
        while lo < hi:
            while lo < hi and not s[lo].isalnum():
                lo += 1
            while lo < hi and not s[hi].isalnum():
                hi -= 1
            if s[lo].upper() != s[hi].upper():
                return False
            else:
                lo += 1
                hi -= 1
        return True
