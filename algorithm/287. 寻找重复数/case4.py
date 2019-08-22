# 二分法
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        start = 1
        end = len(nums)
        while(start < end):
            mid = (start + end) >> 1
            count = 0
            for num in nums:
                if(num <= mid):
                    count = count + 1
            if(count <= mid):
                start = mid + 1
            else:
                end = mid
        return start


nums = [1, 6, 4, 2, 6, 9, 6, 5, 3]
s = Solution()
print(s.findDuplicate(nums))
