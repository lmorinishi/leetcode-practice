class Solution:
    def countAndSay(self, n: int) -> str:
        tmp = '1'
        for _ in range(n-1):
            times = 1
            current = tmp[0]
            read_out = ''
            for char in tmp[1:] + '_':
                if char == current:
                    times += 1
                else:
                    read_out += str(times) + current
                    current = char
                    times = 1
            tmp = read_out
        return tmp
