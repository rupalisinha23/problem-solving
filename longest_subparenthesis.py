class Solution:
    def longest_parenthesis(self, s):

        start = -1
        max_len = 0
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if not stack:
                    start = i
                else:
                    stack.pop(-1)
                    if not stack:
                        max_len = max(max_len, (i-start))
                    else:
                        max_len = max(max_len, (i-stack[-1]))
        return max_len