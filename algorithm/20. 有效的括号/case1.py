class Solution:
    def isValid(self, s: str) -> bool:
        tag = len(s) % 2
        if(tag == 1):
            return False
        l = list()
        d = {'}': '{', '[': ']', '(': ')'}
        for c in s:
            index = len(l)-1
            if(c in d):
                l.append(c)
            else:
                if(index == -1):
                    return False
                else:
                    if(d[c] == l[index]):
                        l.pop()
                    else:
                        return False
        if(len(l) == 0):
            return True
        else:
            return False

s = Solution()
print(s.isValid('()'))
