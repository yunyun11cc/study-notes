"""
给定二叉搜索树的根节点 root 和整数 k，返回树中第 k 小的节点值。
从 1 开始计数，k 的范围是 1 到树的节点总数。

示例 1
输入：root = [3, 1, 4, null, 2], k = 1
输出：1

示例 2
输入：root = [5, 3, 6, 2, 4, null, null, 1], k = 3
输出：3
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        pass
