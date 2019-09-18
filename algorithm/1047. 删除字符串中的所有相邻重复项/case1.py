class Solution:
    def removeDuplicates(self, S: str) -> str:
        hStack = [0]
        for char in S:
            size = len(hStack)
            if(char == hStack[size-1]):
                hStack.pop()
            else:
                hStack.append(char)
        re = str()
        hStack.pop(0)
        for char in hStack:
            re = re+char
        return re


s = Solution()
sstr = "abccbdef"
print(s.removeDuplicates(sstr))
