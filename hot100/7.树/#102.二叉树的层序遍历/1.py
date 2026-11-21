from collections import deque

"""
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]
"""



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        
        result=[]
        queue=deque([root]) # 用于层序遍历的双端队列
        
        while queue:
            level_size=len(queue)
            curr_level=[]
            
            for _ in range(level_size):
                node=queue.popleft()
                curr_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            result.append(curr_level)
        
        return result
            
            