class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        longest, left_most_valid = 0,0
        dict1={}
        for i, letter in enumerate(s):
            if letter in dict1:
                left_most_valid = max(left_most_valid, dict1[letter]+1)

            dict1[letter] = i
            longest = max(longest, i-left_most_valid + 1)

        return longest

sol = Solution()
print(sol.lengthOfLongestSubstring('pwwkew'))
print(sol.lengthOfLongestSubstring('abcdabcbb'))
print(sol.lengthOfLongestSubstring(''))
print(sol.lengthOfLongestSubstring(' '))
print(sol.lengthOfLongestSubstring('c'))