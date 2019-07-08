class Solution:
    def reverse(self,x):
        if x > 0:
            reverse_string = int(str(x)[::-1])
        elif x < 0:
            reverse_string = -1*int(str(x*-1)[::-1])
        else:
            reverse_string = 0


        min_a = -2**31
        max_a = (2**31-1)
        if reverse_string > max_a or reverse_string < min_a:
            return 0

        return reverse_string

sol = Solution()
print(sol.reverse(123))


