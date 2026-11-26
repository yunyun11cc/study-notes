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


# 1. 用中序遍历访问节点，第一次比较前将前驱值设为负无穷。
# 2. 先验证左子树，再检查当前值是否严格大于前驱值。
# 3. 通过比较后更新前驱值，再验证右子树。


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
