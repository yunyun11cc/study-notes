import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
        
class Solution:
    def __init__(self):
        self.prev=float('-inf')

    def isValidBST(self, root: TreeNode | None) -> bool:
        prev = float('-inf')

        def isBST(node):
            nonlocal prev # 指明修改的是外部的prev，相当于指针

            if node is None:
                return True
            
            if isBST(node.left) is False:
                return False           
            if node.val <= prev:
                return False
            prev=node.val
            
            return isBST(node.right)
        
        return isBST(root)