class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def realStr(line: str) -> str:
            aideStack = list()
            outStr = str()
            for c in line:
                if c == '#':
                    if aideStack:
                        aideStack.pop()
                    else:
                        continue
                else:
                    aideStack.append(c)
            for c in aideStack:
                outStr = outStr + c
            return outStr
        realS = realStr(S)
        realT = realStr(T)
        if realS == realT:
            return True
        else:
            return False

S = "ab##"
T = "b"
ss = Solution()
print(ss.backspaceCompare(S, T))
