# Definition for a binary tree node.
# 线索二叉树


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> list():
        result = list()
        p = root
        while(p):
            result.append(p.val)
            thread = p.left
            if(thread):
                while(thread.right):
                    thread = thread.right
                thread.right = p.right
                tmp = p.left
                p.left = None
                p = tmp
            else:
                p = p.right
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
print(s.preorderTraversal(node1))
