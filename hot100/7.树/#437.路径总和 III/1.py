from typing import Optional


"""
给定二叉树根节点 root 和整数 targetSum，统计节点值之和为 targetSum 的路径数。
路径可以从任意节点开始和结束，至少包含一个节点，并且只能沿父节点向子节点行进。

示例 1
输入：root = [10, 5, -3, 3, 2, null, 11, 3, -2, null, 1], targetSum = 8
输出：3
解释：符合要求的路径为 5 → 3、5 → 2 → 1、-3 → 11。

示例 2
输入：root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1], targetSum = 22
输出：3
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. 递归枚举树中的每个节点作为路径起点。
# 2. 从当前起点向两个孩子递归，每经过一个节点就从剩余目标和中减去它的值。
# 3. 剩余目标和为 0 时计入一条路径，并继续向下查找更长的合法路径。


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0

        def curr_node_path(node,targetSum):
            if node is None:
                return 0

            targetSum-=node.val
            curr_count=0
            if targetSum==0:
                curr_count+=1

            left_count=curr_node_path(node.left,targetSum)
            right_count=curr_node_path(node.right,targetSum)

            return curr_count+left_count+right_count


        # 分别统计从当前节点开始、从左子树开始、从右子树开始的路径。
        return (curr_node_path(root,targetSum)+
                self.pathSum(root.left,targetSum)+
                self.pathSum(root.right,targetSum))
