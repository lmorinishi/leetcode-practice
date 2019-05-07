class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters = {}
        for i in range(len(s)):
            if s[i] in letters:
                letters[s[i]] += 1
            else:
                letters[s[i]] = 1
        for j in range(len(t)):
            if t[j] in letters:
                if letters[t[j]] <= 0:
                    return False
                else:
                    letters[t[j]] -= 1
            else:
                return False
        return True
