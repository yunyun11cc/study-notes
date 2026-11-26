"""
给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 三个指针，prev指向前序数组的序号，left和right分别指向左右子树数组的边界


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        def dfs(prev,left,right):
            if left>right:
               return None
           
            for root_idx in range(left, right + 1): # 拿到当前操作节点在中序序列中的位置
                if inorder[root_idx]==preorder[prev]:
                   break
            left_size = root_idx - left
            curr_node=TreeNode(preorder[prev])
            curr_node.left=dfs(prev+1,left,root_idx-1)
            curr_node.right=dfs(prev + left_size + 1,root_idx+1,right)
            
            return curr_node
        
        
        return dfs(0,0,len(inorder)-1)           