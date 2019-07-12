class Solution:
    def myatoi(self, str):
        limit = 2**31
        min_limit, max_limit = -limit, limit-1


        for idx, v in enumerate(str):
            if v == ' ':
                pass
            else:
                str = str[idx:len(str)]
                break
        pos = 0
        neg = 1
        num = 0
        N = len(str)
        if N < 1: return 0

        if str[0] == '-': neg = -1; pos = 1
        if str[0] == '+': pos = 1
        while pos < len(str):
            if ord(str[pos]) >= ord('0') and ord(str[pos]) <= ord('9'):
                num = num * 10 + (ord(str[pos]) - ord('0'))
                pos +=1
                if (neg * num) < min_limit: return min_limit
                if (neg * num) > max_limit: return max_limit

            else:
                break
        return neg * num





sol= Solution()
print(sol.myatoi('     '))
print(sol.myatoi('     my name '))
print(sol.myatoi('     1234'))
print(sol.myatoi('12345'))
print(sol.myatoi(' -42'))
print(sol.myatoi("2147483648"))