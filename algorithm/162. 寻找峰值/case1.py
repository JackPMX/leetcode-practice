class Solution:
    def findPeakElement(self, nums: list) -> int:
        length = len(nums)
        nums.append(False)
        i = 0
        while i < length:
            if(nums[i] > nums[i + 1] or (i + 1) == length):
                return i
            else:
                i = i + 1


nums = [7, 2, 2, 3, 5, 6, 6]
s = Solution()
print(s.findPeakElement(nums))
