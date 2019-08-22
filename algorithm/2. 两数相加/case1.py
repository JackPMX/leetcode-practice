# 先转化为数字再转化为列表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        pass

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = ""
        s2 = ""
        ltmp1 = l1
        ltmp2 = l2
        while(True):
            s1 = s1 + str(ltmp1.val)
            if (ltmp1.next is not None):
                ltmp1 = ltmp1.next
            else:
                break
        s1 = "".join(list(reversed(s1)))
        while(True):
            s2 = s2 + str(ltmp2.val)
            if (ltmp2.next is not None):
                ltmp2 = ltmp2.next
            else:
                break
        s2 = "".join(list(reversed(s2)))
        s = str(int(s1) + int(s2))
        s = "".join(list(reversed(s)))
        resultS = []
        length = len(s)
        i = 0
        while(i < length):
            node = ListNode(s[i])
            resultS.append(node)
            i = i + 1
        i = 0
        while(i < length):
            if(i == length - 1):
                break
            else:
                resultS[i].next = resultS[i+1]
                i = i + 1
        for node in resultS:
            print(node.val)
        return resultS[0]

node1 = ListNode("2")
node2 = ListNode("4")
node3 = ListNode("3")
node1.next = node2
node2.next = node3

node4 = ListNode("5")
node5 = ListNode("6")
node6 = ListNode("4")
node4.next = node5
node5.next = node6
s = Solution()
s.addTwoNumbers(node1, node4)
print()
