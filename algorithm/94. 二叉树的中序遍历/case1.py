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
                result.append(node.val)
                helper(node.right)
        helper(root)
        return result

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node1.left = node4
node1.right = node2
node2.right = node3
node3.left = node5
node4.left = node6
node4.right = node7
node7.right = node8
s = Solution()
print(s.inorderTraversal(node1))
