from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return ((sum(nums) - sum(set(nums)))//(len(nums) - len(set(nums))))


nums = [1, 3, 4, 2, 2, 2]
s = Solution()
print(s.findDuplicate(nums))
