# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 优化：将for在中序里面对应下标的操作改为在哈希表里面查找


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def dfs(prev,left,right):
            if left>right:
               return None
           
            root_idx=inorder_map[preorder[prev]]
            left_size = root_idx - left
            
            curr_node=TreeNode(preorder[prev])
            curr_node.left=dfs(prev+1,left,root_idx-1)
            curr_node.right=dfs(prev + left_size + 1,root_idx+1,right)
            
            return curr_node
        
        
        return dfs(0,0,len(inorder)-1)     