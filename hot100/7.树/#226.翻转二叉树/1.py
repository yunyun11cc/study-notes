from typing import Optional


"""
给定二叉树的根节点 root，把每个节点的左右子树互换，并返回翻转后的根节点。

示例 1
输入：root = [4, 2, 7, 1, 3, 6, 9]
输出：[4, 7, 2, 9, 6, 3, 1]

示例 2
输入：root = [2, 1, 3]
输出：[2, 3, 1]

示例 3
输入：root = []
输出：[]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. 遇到空节点时直接返回。
# 2. 交换当前节点的左右孩子。
# 3. 递归翻转交换后的两棵子树，再返回当前节点。


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        root.left, root.right = root.right, root.left
        # 两次递归都会原地翻转对应的子树。
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
