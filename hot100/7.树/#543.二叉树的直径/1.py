from typing import Optional



"""
给你一棵二叉树的根节点，返回该树的 直径 。

二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。

两节点之间路径的 长度 由它们之间边数表示。

输入：root = [1,2,3,4,5]
输出：3
解释：3 ，取路径 [4,2,1,3] 或 [5,2,1,3] 的长度。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        

class Solution:
    def _max_depth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        left_depth=self._max_depth(node.left)
        right_depth=self._max_depth(node.right)
        
        self.max_diameter=max(self.max_diameter,left_depth+right_depth)
        
        return max(left_depth,right_depth)+1
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter=0
        
        self._max_depth(root)
        
        return self.max_diameter
        
        
        