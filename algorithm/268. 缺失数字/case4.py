from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return ((0 + len(nums))*(len(nums) + 1)//2 - sum(nums))


# nums = [7, 8, 9, 11, 12]
# nums = [1,2,3]
# nums = [0, -1, 3, 1]
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
s = Solution()
print(s.missingNumber(nums))
