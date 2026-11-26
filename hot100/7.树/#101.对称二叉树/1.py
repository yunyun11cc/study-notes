from typing import Optional


"""
给定二叉树的根节点 root，判断整棵树是否关于根节点的中轴线对称。

示例 1
输入：root = [1, 2, 2, 3, 4, 4, 3]
输出：true

示例 2
输入：root = [1, 2, 2, null, 3, null, 3]
输出：false
解释：两个值为 3 的节点位于各自父节点的同一侧，无法互为镜像。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. 从根节点的左右孩子开始成对检查镜像位置。
# 2. 两边都为空时匹配成功。只有一边为空或节点值不同就失败。
# 3. 分别比较左外侧与右外侧、左内侧与右内侧，两组都匹配才对称。


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
