class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1:
            return s

        rows = ["" for x in range(numRows)]
        curRow = 0
        goingDown = False

        for c in s:
            rows[curRow] += c
            if curRow == 0 or curRow == numRows-1:
                goingDown = not goingDown
            if goingDown:
                curRow += 1
            else:
                curRow -= 1

        return "".join(rows)
