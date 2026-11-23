from collections import deque
from typing import Optional

"""
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

输入：root = [1,2,3,null,5,null,4]

输出：[1,3,4]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

# 直接层序遍历，然后将每一层最右边的节点加入结果就行了
        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return[]
        
        queue=deque([root])
        result=[] # 最终右视图的结果数组
        
        while queue:
            level_size=len(queue) # 当前这一层的元素个数
            
            for i in range(level_size): # 每一个 for 结束会得到一个装满这一层元素的 res
                node=queue.popleft()
                if i==level_size-1:
                    result.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result
            
         
            
        