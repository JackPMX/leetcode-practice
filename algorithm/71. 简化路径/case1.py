class Solution:
    def simplifyPath(self, path: str) -> str:
        if(path[-1] != '/'):
            path = path + '/'
        stack = list()
        stack.append('root')
        word = ''
        for c in path:
            if c == '/' and stack[-1] == '/':
                stack.pop()
                # stack.append(word)
                if word == '.':
                    pass
                elif word == '..':
                    if(len(stack) == 1):
                        pass
                    else:
                        stack.pop()
                elif word == '':
                    pass
                else:
                    stack.append(word)
                word = ''
                stack.append(c)
            elif(c == '/' and stack[-1] != '/'):
                stack.append(c)
            else:
                word = word + c
        p = str()
        stack.pop(0)
        stack.pop(-1)
        # print(stack)
        if(len(stack) == 0):
            return '/'
        for s in stack:
            s = '/' + s
            p = p + s
        return p

s = Solution()
print(s.simplifyPath("/a/../../b/../c//.//"))
# print(s.simplifyPath(".."))
