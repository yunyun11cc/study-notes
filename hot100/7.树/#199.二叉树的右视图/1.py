from collections import deque
from typing import Optional


"""
给定二叉树的根节点 root，返回从右侧看到的节点值，顺序从最上层到最下层。
每一层可见的是该层最右边的节点。

示例 1
输入：root = [1, 2, 3, null, 5, null, 4]
输出：[1, 3, 4]

示例 2
输入：root = [1, 2, 3, 4]
输出：[1, 3, 4]
解释：节点 4 在最下层，该层只有它一个节点。

示例 3
输入：root = []
输出：[]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. 用队列按层遍历，每轮开始时先记住当前层节点数。
# 2. 从左到右处理当前层的节点，并依次将它们的孩子入队。
# 3. 把每层最后出队的节点值加入右视图。


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return[]

        queue=deque([root])
        result=[] # 最终右视图的结果数组

        while queue:
            level_size=len(queue) # 当前这一层的元素个数

            for i in range(level_size):  # 本轮只处理当前层，后入队的是下一层
                node=queue.popleft()
                if i==level_size-1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
