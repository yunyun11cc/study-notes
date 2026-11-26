"""
给定二叉树的根节点 root，返回树的最大深度，也就是从根到最远叶子经过的节点数。
空树的深度为 0。

示例 1
输入：root = [3, 9, 20, null, null, 15, 7]
输出：3

示例 2
输入：root = [1, null, 2]
输出：2
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. 空节点的深度为 0，直接返回。
# 2. 用后序递归得到左右子树的最大深度。
# 3. 取较大的子树深度加 1，把当前节点也算进去。


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0 # 空结点没有高度，递归终止条件

        left_depth=self.maxDepth(root.left) # 左子树的最大深度
        right_depth=self.maxDepth(root.right) # 右子树的最大深度

        return 1+max(left_depth,right_depth)
