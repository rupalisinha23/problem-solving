class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        sorted_joined = sorted(nums1 + nums2)
        if len(sorted_joined) % 2 == 0:
            index = int(len(sorted_joined) / 2)
            return (sorted_joined[index] + sorted_joined[index - 1]) / 2
        else:
            index = (int(len(sorted_joined) / 2))
            return sorted_joined[index]


sol = Solution()
print(sol.findMedianSortedArrays([1,2],[1,2]))