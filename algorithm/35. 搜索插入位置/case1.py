# 一次遍历


class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        isAsc = True
        length = len(nums)
        if length < 2:
            pass
        else:
            if nums[0] < nums[1]:
                isAsc = True
            else:
                isAsc = False
        if isAsc is True:
            start = 0
            end = length - 1
            if target <= nums[start]:
                return start
            elif target > nums[end]:
                return length
            elif target == nums[end]:
                return end
            else:
                while(end - start > 1):
                    bar = (end + start)//2
                    if(nums[start] < target <= nums[bar]):
                        end = bar
                    else:
                        start = bar
                return end
        else:
            start = 0
            end = length - 1
            if target >= nums[start]:
                return start
            elif target < nums[end]:
                return length
            elif target == nums[end]:
                return end
            else:
                while(end - start > 1):
                    bar = (end + start)//2
                    if(nums[start] > target >= nums[bar]):
                        end = bar
                    else:
                        start = bar
                return end


nums = [6, 7, 100, 300]
target = 100
s = Solution()
print(s.searchInsert(nums, target))
