# Definition for a binary tree node.
# 模拟系统栈


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list():
        if not root:
            return []
        # 1 表示递归处理
        stack = [(1, root)]
        res = []
        while stack:
            command, node = stack.pop()
            if command == 0:
                # 0 表示当前马上执行将结点的值添加到结果集中
                res.append(node.val)
            else:
                # 关键在这里：因为是模拟系统栈，应该把中序遍历的顺序倒过来写
                # 调整一下顺序就可以完成前序遍历和后序遍历
                if node.right:
                    stack.append((1, node.right))
                stack.append((0, node))
                if node.left:
                    stack.append((1, node.left))
        return res

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
