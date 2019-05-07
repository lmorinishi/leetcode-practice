class Solution:
    def longest_palindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        mydict = {}
        for i in range(len(s)):
            lo1, hi1 = expand_out(s, i, i)
            mydict[hi1-lo1] = s[lo1:hi1]
            lo2, hi2 = expand_out(s, i, i+1)
            mydict[hi2-lo2] = s[lo2:hi2]
        return mydict[max(mydict)]


def expand_out(s: str, low: int, high: int) -> List[int]:
    if s[low] != s[high]:
        return [low, low]
    else:
        while low >= 0 and high < len(s) and s[low] == s[high]:
            low -= 1
            high += 1
        return [low + 1, high]
