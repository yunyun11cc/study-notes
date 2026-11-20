from typing import Optional

"""
给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。

输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# 遍历到当前节点，直接交换左右孩子的指针，然后直接返回该结点就可以了

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        root.left,root.right=root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root