class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or '' in strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        result = ''
        min_len = min(len(k) for k in strs)
        i = 0
        while i < min_len:
            if len(set([k[i] for k in strs])) == 1:
                result += strs[0][i]
                i += 1
            else:
                return result
        return result
