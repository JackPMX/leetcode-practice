# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: Node) -> list:
        result = list()

        def helper(node: Node):
            if node is None:
                return
            else:
                if node.children is None:
                    pass
                else:
                    for child in node.children:
                        helper(child)
            result.append(node.val)
        helper(root)
        return result

node1 = Node(1, None)
node2 = Node(2, None)
node3 = Node(3, None)
node4 = Node(4, None)
node5 = Node(5, None)
node6 = Node(6, None)
node1.children = [node3, node2, node4]
node3.children = [node5, node6]
s = Solution()
print(s.postorder(node1))
