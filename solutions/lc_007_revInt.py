class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            is_neg = True
            x *= -1
        else:
            is_neg = False

        out_int = 0
        while x > 0:
            x, rem = divmod(x, 10)
            if is_neg and ((out_int > 2**31/10) or (out_int == int((2**31)/10) and rem > 8)):
                return 0
            elif not is_neg and ((out_int > (2**31-1)/10) or (out_int == int((2**31-1)/10) and rem > 7)):
                return 0
            out_int = out_int * 10 + rem

        if is_neg:
            return -out_int
        return out_int
