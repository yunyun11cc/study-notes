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


# 1. 用 prev 指向当前根节点在前序数组中的位置，left 和 right 划定中序区间。
# 2. 在中序区间线性查找根节点，用其下标划分左右子树并计算左子树大小。
# 3. 分别用前序数组中两棵子树的起点递归构造，接到当前根节点下。


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        def dfs(prev, left, right):
            if left > right:
                return None

            for root_idx in range(left, right + 1): # 拿到当前操作节点在中序序列中的位置
                if inorder[root_idx]==preorder[prev]:
                    break
            left_size = root_idx - left
            curr_node=TreeNode(preorder[prev])
            curr_node.left=dfs(prev+1,left,root_idx-1)
            # 跳过前序中的根节点和整棵左子树，右子树从下一项开始。
            curr_node.right = dfs(prev + left_size + 1, root_idx + 1, right)

            return curr_node


        return dfs(0,0,len(inorder)-1)
