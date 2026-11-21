from typing import Optional

"""
给你一个二叉树的根节点 root ， 检查它是否轴对称。

输入：root = [1,2,2,3,4,4,3]
输出：true

输入：root = [1,2,2,null,3,null,3]
输出：false
"""




# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 看一颗树是否是对称的二叉树，首先在遍历的结点上画一条对称轴
# 当前结点的左孩子的左孩子和右孩子的右孩子相同，左孩子的右孩子和右孩子的左孩子相同
# 双指针不断在左右两边游动，左指针往左走，右指针就要往右走；左指针往右走，右指针就要往左走

class Solution:   
    def isSymmetric(self, root: TreeNode | None) -> bool: # 当前函数返回的就是该结点是否是一颗对称的二叉树
        if not root:
            return True
        
        return self._check(root.left,root.right) # 如果树有根节点，左右指针左右指针开始做匹配
        
    def _check(self,p: Optional[TreeNode],q: Optional[TreeNode]) -> bool: # 左右指针匹配
        if not p and not q: # 两个指针都为空的时候匹配成功
            return True
        
        # 匹配的过程中只要有一个为空或者数值不匹配，那就匹配失败
        if not p or not q or p.val != q.val:
            return False
        
        return self._check(p.left,q.right) and self._check(p.right,q.left)