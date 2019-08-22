# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list():
        result = list()

        def helper(node: TreeNode):
            if node is None:
                return
            else:
                helper(node.left)
                helper(node.right)
                result.append(node.val)
        helper(root)
        return result

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = None
node1.right = node2
node2.left = node3
s = Solution()
print(s.inorderTraversal(node1))
