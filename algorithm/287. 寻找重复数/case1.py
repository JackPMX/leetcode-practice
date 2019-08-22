# 快慢指针


class Solution:
    def findDuplicate(self, nums: list()) -> int:
        hare = 0
        tortoise = 0
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        finder = 0
        while nums[finder] != nums[tortoise]:
            tortoise = nums[tortoise]
            finder = nums[finder]
        return nums[finder]


nums = [1, 3, 4, 2, 2]
s = Solution()
print(s.findDuplicate(nums))
