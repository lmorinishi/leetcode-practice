class Solution:
    def myAtoi(self, my_str: str) -> int:
        my_str = my_str.strip()
        is_neg = False
        if my_str == '':
            return 0
        else:
            valid_chars = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
            if my_str[0] == '-':
                is_neg = True
                my_str = my_str[1:]
            elif my_str[0] == '+':
                my_str = my_str[1:]
            tmp = 0
            i = 0
            while i < len(my_str) and my_str[i] in valid_chars:
                if ((tmp > (2**31)/10) or (tmp == int((2**31)/10) and int(my_str[i]) > 7)) and is_neg:
                    return -(2 ** 31)
                elif ((tmp > (2**31 - 1)/10) or (tmp == int((2**31 - 1)/10) and int(my_str[i]) == 8)) and not is_neg:
                    return 2**31 - 1
                tmp = 10 * tmp + int(my_str[i])
                i += 1
            if tmp == '':
                return 0
            if is_neg:
                return -tmp
            return tmp
