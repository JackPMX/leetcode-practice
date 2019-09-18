class Solution:
    def removeDuplicates(self, S: str) -> str:
        hStack = list()
        for char in S:
            if(hStack and hStack[-1] == char):
                hStack.pop()
            else:
                hStack.append(char)
        return "".join(hStack)


s = Solution()
sstr = "abccbdef"
print(s.removeDuplicates(sstr))
