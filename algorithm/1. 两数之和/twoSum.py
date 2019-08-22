class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        inDict = {}
        length = len(nums)
        i = 0
        while(i < length):
            checkingValue = target - nums[i]
            if(inDict.get(checkingValue) is not None):
                # print(checkingValue, nums[i])
                # print(inDict.get(checkingValue), i)
                return [inDict.get(checkingValue), i]
            else:
                inDict[nums[i]] = i
                i = i + 1


s = Solution()
nums = [2, 7, 11, 15]
target = 18
s.twoSum(nums, target)
