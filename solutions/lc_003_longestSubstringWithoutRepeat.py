class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mydict = {}
        max_len, i = 0, 0
        for j in range(len(s)):
            if s[j] in mydict:
                i = max(mydict[s[j]], i)
            max_len = max(max_len, j-i+1)
            mydict[s[j]] = j+1
            j += 1
