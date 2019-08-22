# 改进滑动窗口
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # charSet = set()
        # length = len(s)
        # i = 0
        # j = 0
        # maxLength = 0
        # while(i < length and j < length):
        #     if(s[j] not in charSet):
        #         charSet.add(s[j])
        #         j = j + 1
        #         maxLength = max(maxLength, j - i)
        #     else:
        #         charSet.remove(s[i])
        #         i = i + 1
        # return maxLength
        charList = list()
        length = len(s)
        i = 0
        j = 0
        confictIndex = 0
        while(i < length and j < length):
            if(s[j] not in charList):
                charList.append(s[j])
                j = j + 1
                maxLength = max(maxLength, j - i)
            else:
                # while(i <)
                pass

so = Solution()
s = "mnsjnsasduw"
print(so.lengthOfLongestSubstring(s))
