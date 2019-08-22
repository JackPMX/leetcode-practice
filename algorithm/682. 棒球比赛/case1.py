class Solution:
    def calPoints(self, ops: list) -> int:
        aideStack = list((0, 0, 0, 0))
        result = 0
        for op in ops:
            if op == '+':
                popUp = aideStack.pop()
                popDown = aideStack.pop()
                score = popDown + popUp
                result = result + score
                aideStack.append(popDown)
                aideStack.append(popUp)
                aideStack.append(score)
            elif op == 'D':
                popUp = aideStack.pop()
                score = 2 * popUp
                result = result + score
                aideStack.append(popUp)
                aideStack.append(score)
            elif op == 'C':
                popUp = aideStack.pop()
                result = result - popUp
            else:
                score = int(op)
                result = result + score
                aideStack.append(score)
        return result


# ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
ops = ["5", "2", "C", "D", "+"]
s = Solution()
print(s.calPoints(ops))
