"""
给定二叉树的根节点 root，返回按中序顺序访问得到的节点值列表。
中序顺序是左子树、当前节点、右子树。

示例 1
输入：root = [1, null, 2, 3]
输出：[1, 3, 2]

示例 2
输入：root = []
输出：[]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. 空节点返回空列表。
# 2. 递归得到左右子树的中序遍历列表。
# 3. 按左子树、当前节点、右子树的顺序拼接结果。


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        # 两次递归各返回一个列表，可以直接拼接。
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
