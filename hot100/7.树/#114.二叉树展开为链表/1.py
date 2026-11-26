"""
给定二叉树的根节点 root，把树原地展开成一条沿 right 指针连接的链。
链上的节点顺序与原树的前序遍历一致，每个节点的 left 指针都置空。
输出示例展示修改后的树结构，函数只执行原地修改。

示例 1
输入：root = [1, 2, 5, 3, 4, null, 6]
输出：[1, null, 2, null, 3, null, 4, null, 5, null, 6]

示例 2
输入：root = []
输出：[]

示例 3
输入：root = [0]
输出：[0]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. 沿右指针遍历，遇到有左子树的节点就找到左子树最右边的节点。
# 2. 把原右子树接到该节点后面，再把原左子树移到当前节点的右边。
# 3. 清空当前节点的左指针，沿右指针继续处理后续节点。


class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        curr=root
        while curr:
            if curr.left:
                predecessor=curr.left # 进入到左子树中寻找最右节点
                while predecessor.right:
                    predecessor=predecessor.right
                # 先保存原右子树的连接，再让左子树成为后续链的一段。
                predecessor.right = curr.right
                curr.right=curr.left
                curr.left=None

            curr=curr.right
