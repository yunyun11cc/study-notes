"""
给定二叉树的根节点 root，以及树中两个不同的节点 p 和 q，返回它们的最近公共祖先。
最近公共祖先是同时为 p 和 q 的祖先且深度最大的节点。节点可以是自己的祖先。

示例 1
输入：root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1
输出：3

示例 2
输入：root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 4
输出：5
解释：节点 5 本身就是节点 4 的祖先。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 1. 后序遍历，分别统计左右子树里出现了几个目标节点。
# 2. 当前节点是 p 或 q 时再加 1，得到当前整棵子树的命中数。
# 3. 第一次汇总出 2 个目标的节点就是最近公共祖先，记录后继续向上返回命中数。


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None

        def dfs(node):
            if node is None:
                return 0

            left_count = dfs(node.left)
            right_count = dfs(node.right)
            count = int(node is p or node is q)
            total = count + left_count + right_count

            # 后序遍历中第一个包含两个目标的节点深度最大。
            if total == 2 and self.ans is None:
                self.ans = node

            return total

        dfs(root)
        return self.ans