class Solution:
    def findDuplicate(self, nums: list()) -> int:
        sett = set()
        for num in nums:
            if num in sett:
                return num
            else:
                sett.add(num)


nums = [1, 3, 4, 2, 2]
s = Solution()
print(s.findDuplicate(nums))
