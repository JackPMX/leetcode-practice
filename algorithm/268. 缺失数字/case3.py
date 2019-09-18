from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        end = len(nums)
        nums.append(False)
        zeroTag = False
        i = 0
        while(i < end):
            tmp = abs(nums[i])
            if(nums[tmp] > 0):
                nums[tmp] = -nums[tmp]
            elif(nums[tmp] is False):
                nums[tmp] = True
            elif(nums[tmp] == 0):
                zeroTag = True
            i = i + 1
        for (index, value) in enumerate(nums):
            if(value is True):
                continue
            elif(value > 0):
                return index
        return 0


# nums = [7, 8, 9, 11, 12]
# nums = [1,2,3]
# nums = [0, -1, 3, 1]
# nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
s = Solution()
print(s.missingNumber(nums))
