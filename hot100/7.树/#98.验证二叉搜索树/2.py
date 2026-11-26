"""
给定二叉树的根节点 root，判断它是不是有效的二叉搜索树。
对树中的每个节点，左子树的所有值都必须严格小于当前值，右子树的所有值都必须严格大于当前值。

示例 1
输入：root = [2, 1, 3]
输出：true

示例 2
输入：root = [5, 1, 4, null, null, 3, 6]
输出：false
解释：根节点右子树中的 4 小于根节点的值 5。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. 在入口方法中把前驱值初始化为负无穷，并存到 self.prev。
# 2. 用实例方法递归验证左子树，并比较当前节点值与记录的前驱值。
# 3. 当前值严格更大时更新 self.prev，再递归验证右子树。


class Solution:
    def isBST(self, node):
        if node is None:
            return True

        if self.isBST(node.left) is False:
            return False
        # self.prev 保留中序序列中上一个访问到的值。
        if node.val <= self.prev:
            return False
        self.prev=node.val

        return self.isBST(node.right)

    def isValidBST(self, root: TreeNode | None) -> bool:
        self.prev = float('-inf')
        return self.isBST(root)
