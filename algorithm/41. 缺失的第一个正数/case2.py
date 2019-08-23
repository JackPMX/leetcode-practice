from typing import *


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        end = len(nums)
        oneTag = False
        i = 0
        endTag = False
        while(i < end):
            if(nums[i] == 1):
                oneTag = True
            elif(nums[i] < 1 or nums[i] > end):
                nums[i] = 1
            i = i + 1
        if(oneTag is False):
            return 1
        for num in nums:
            num = abs(num)
            if(num == end):
                if(nums[0] > 0):
                    nums[0] = -nums[0]
            else:
                if(nums[num] > 0):
                    nums[num] = -nums[num]
        for (index, num) in enumerate(nums):
            if(num > 0):
                if(index == 0):
                    endTag = True
                else:
                    return index
        if(endTag is True):
            return end
        else:
            return end+1


# nums = [7, 8, 9, 11, 12]
# nums = [1,2,3]
nums = [0, -1, 3, 1]
s = Solution()
print(s.firstMissingPositive(nums))
