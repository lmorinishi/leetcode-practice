class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # base python
        # return haystack.find(needle)

        # written out
        if len(needle) == 0:
            return 0
        elif len(haystack) < len(needle):
            return -1

        for i in range(len(haystack)-len(needle)+1):
            if haystack[i] == needle[0]:
                j = 0
                while i + j < len(haystack):
                    print(haystack[i + j], needle[j])
                    if haystack[i + j] != needle[j]:
                        break
                    elif j == len(needle)-1:
                        return i
                    j += 1
        return -1
