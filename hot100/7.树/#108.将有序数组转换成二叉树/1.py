import math

"""
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡 二叉搜索树。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

# 1. 终止条件：当前负责的数组为空（或左边界大于右边界），直接返回空节点
# 2. 创建当前节点：算出中间位置，用中间元素建出当前节点
# 3. 递归挂接并返回：分别用左半段、右半段递归构造左右孩子，挂到当前节点后将其返回       
        
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def dfs(left,right): # 当前处理的节点和操作的数组的边界
            if left>right:
                return None
            
            mid=(right-left)//2+left
            curr_node=TreeNode(nums[mid])
            curr_node.left=dfs(left,mid-1)
            curr_node.right=dfs(mid+1,right)
            
            return curr_node
        
        return dfs(0,len(nums)-1)