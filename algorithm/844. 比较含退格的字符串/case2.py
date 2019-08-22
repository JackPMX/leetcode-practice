class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def realStr(line: str) -> str:
            outStr = str()
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
