"""
给定同一棵二叉树的前序序列 preorder 和中序序列 inorder。
节点值互不相同。根据这两个序列还原二叉树，并返回根节点。

示例 1
输入：preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]
输出：[3, 9, 20, null, null, 15, 7]

示例 2
输入：preorder = [-1], inorder = [-1]
输出：[-1]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. 先建立中序节点值到下标的映射，查找子树根节点时可以直接定位。
# 2. 用根节点的中序下标划分左右区间，并计算左子树占用的元素数。
# 3. 在前序数组中跳过根和左子树即可找到右子树的起点，递归挂接两边。


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        def dfs(prev, left, right):
            if left > right:
                return None

            root_idx=inorder_map[preorder[prev]]
            left_size = root_idx - left

            curr_node=TreeNode(preorder[prev])
            curr_node.left=dfs(prev+1,left,root_idx-1)
            # 跳过前序中的根节点和整棵左子树，右子树从下一项开始。
            curr_node.right = dfs(prev + left_size + 1, root_idx + 1, right)

            return curr_node


        return dfs(0,0,len(inorder)-1)
