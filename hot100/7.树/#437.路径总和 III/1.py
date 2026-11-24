from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 递归遍历每一个节点，curr_sum记录当前路径上已经产生的总和，curr_sum 初始化成当前遍历节点的值
# 每个节点要做的事：


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def Inorder(node):
            if node is None:
                return
            
            
        
        