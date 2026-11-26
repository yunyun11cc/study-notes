from collections import deque


"""
给定二叉树的根节点 root，返回按层分组的节点值列表。
从根节点所在层开始逐层访问，同一层按从左到右的顺序记录。

示例 1
输入：root = [3, 9, 20, null, null, 15, 7]
输出：[[3], [9, 20], [15, 7]]

示例 2
输入：root = [1]
输出：[[1]]

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


# 1. 用队列保存待访问的节点，先将根节点入队。
# 2. 每轮先固定当前层的大小，只处理这一层的节点。
# 3. 出队时记录节点值，按左、右顺序将孩子入队供下一轮处理。


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        result=[]
        queue=deque([root]) # 用于层序遍历的双端队列

        while queue:
            level_size = len(queue)  # 这一轮只取当前层的节点
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
