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


# 1. 递归搜索 p 和 q，遇到空节点或目标节点时直接返回。
# 2. 左右子树都返回节点时，当前节点就是两边目标的最近公共祖先。
# 3. 其余情况将唯一找到的节点或空值向上传递。


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node is None:
                return None

            # 1. 自己就是目标，直接往上汇报自己
            if node == p or node == q:
                return node

            # 2. 去左右子树找
            left = dfs(node.left)
            right = dfs(node.right)

            # 3. 左右都找到了，说明分岔口在我这，我就是最近的公共祖先
            if left and right:
                return node

            # 4. 只有一边找到了，把找到的那个往上传
            # （如果两边都没找到，左边就是 None，返回 None 也符合逻辑）
            return left if left else right

        return dfs(root)
