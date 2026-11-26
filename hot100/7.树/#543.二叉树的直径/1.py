from typing import Optional


"""
给定二叉树的根节点 root，返回树的直径。
直径是任意两个节点之间最长路径上的边数，这条路径可以经过根节点，也可以位于某棵子树中。

示例 1
输入：root = [1, 2, 3, 4, 5]
输出：3
解释：路径 4 → 2 → 1 → 3 经过 3 条边。

示例 2
输入：root = [1, 2]
输出：1
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. 后序遍历求左右子树的最大深度，空子树的深度为 0。
# 2. 经过当前节点的最长路径有左右深度之和那么多条边，据此更新直径。
# 3. 向父节点返回较大的子树深度加 1。


class Solution:
    def _max_depth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        left_depth=self._max_depth(node.left)
        right_depth=self._max_depth(node.right)

        # 左右深度相加得到经过当前节点的路径边数。
        self.max_diameter = max(self.max_diameter, left_depth + right_depth)

        return max(left_depth,right_depth)+1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter=0

        self._max_depth(root)

        return self.max_diameter
