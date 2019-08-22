class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


nums = [6, 7, 100, 300]
target = 1080
s = Solution()
print(s.searchInsert(nums, target))
