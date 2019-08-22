class Solution:
    def findPeakElement(self, nums: list) -> int:
        left = 0
        right = len(nums) - 1
        while(left < right):
            mid = (left + right) >> 1
            if(nums[mid] < nums[mid+1]):
                left = mid+1
            else:
                right = mid
        return left


nums = [7, 2, 2]
s = Solution()
print(s.findPeakElement(nums))
