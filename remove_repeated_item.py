class Solution:
    def remove_repeated_num(self,arr1):

        length = len(arr1)
        if arr1 is None:
            return 0

        i = 0

        while i < len(arr1)-1:
            if arr1[i] == arr1[i+1]:
                arr1.pop(arr1[i])
            else:
                i +=1
        return arr1





sol = Solution()
print(sol.remove_repeated_num([1,1,1,1,2]))
