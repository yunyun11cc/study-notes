"给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。"

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        
        return([self.inorderTraversal(root.left).val]
               +[root.val]
               +self.inorderTraversal(root.right).val
               )