"""
给定一个二叉树 root ，返回其最大深度。

二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

输入：root = [3,9,20,null,null,15,7]
输出：3
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# 对于当前遍历的结点，左右子树中更高的那一颗的高度加上1（结点本身的高度）
# 后序遍历的思路：先求左右子树更高的高度，然后回到当前结点加1
# 递归完以后回到root就是当前树的最大深度

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0 # 空结点没有高度，递归终止条件
        
        left_depth=self.maxDepth(root.left) # 左子树的最大深度
        right_depth=self.maxDepth(root.right) # 右子树的最大深度
        
        return 1+max(left_depth,right_depth)
    
    