class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        inDict = {}

        for index, element in enumerate(nums):
            checkingValue = target - element
            if(inDict.get(checkingValue) is not None):
                # print(checkingValue, element)
                # print(inDict.get(checkingValue), index)
                return [inDict.get(checkingValue), index]
            else:
                inDict[element] = index


s = Solution()
nums = [2, 7, 11, 15]
target = 18
s.twoSum(nums, target)
