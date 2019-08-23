# 不满足o(1)空间的要求
from typing import *


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        end = len(nums) + 1
        i = 1
        while i <= end:
            if i not in nums:
                return i
            else:
                i = i + 1


# nums = [7, 8, 9, 11, 12]
nums = [3, 4, -1, 1]
s = Solution()
print(s.firstMissingPositive(nums))
