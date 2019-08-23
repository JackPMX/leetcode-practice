from typing import *


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        end = len(nums)
        oneTag = False
        i = 0
        endTag = False
        aideDict = dict()
        while(i < end):
            if(nums[i] == 1):
                oneTag = True
            elif(nums[i] < 1 or nums[i] > end):
                nums[i] = 1
            i = i + 1
        if(oneTag is False):
            return 1
        for num in nums:
            aideDict[num] = True
        i = 1
        while(i <= end):
            if(i not in aideDict):
                return i
            i = i + 1
        return i

nums = [7, 8, 9, 11, 12]
# nums = [1,2,3]
# nums = [0, -1, 3, 1]
s = Solution()
print(s.firstMissingPositive(nums))
