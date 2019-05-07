class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) < 1:
            return -1
        seen_once = {}
        seen_twice = set()
        for i in range(len(s)):
            if s[i] in seen_twice:
                continue
            elif s[i] in seen_once:
                seen_once.pop(s[i])
                seen_twice.add(s[i])
            else:
                seen_once[s[i]] = i

        if len(seen_once) > 0:
            return min(seen_once.values())
        else:
            return -1
