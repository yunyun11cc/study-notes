from collections import defaultdict
from typing import Optional


"""
给定二叉树根节点 root 和整数 targetSum，统计节点值之和为 targetSum 的路径数。
路径可以从任意节点开始和结束，至少包含一个节点，并且只能沿父节点向子节点行进。

示例 1
输入：root = [10, 5, -3, 3, 2, null, 11, 3, -2, null, 1], targetSum = 8
输出：3
解释：符合要求的路径为 5 → 3、5 → 2 → 1、-3 → 11。

示例 2
输入：root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1], targetSum = 22
输出：3
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. 从根向下维护当前路径的前缀和，并用哈希表记录祖先前缀和的出现次数。
# 2. 先查当前前缀和减去目标和出现了几次，再登记当前前缀和并递归两个孩子。
# 3. 离开节点时撤销它的前缀和记录，使哈希表只保留当前路径的信息。


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 哈希表记录：从根节点到当前节点的路径上，各个前缀和出现的次数
        # 初始化 {0: 1} 是为了处理“直接从根节点出发就凑齐 targetSum”的情况
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        def dfs(node: Optional[TreeNode], curr_sum: int) -> int:
            if node is None:
                return 0

            # 1. 前序位置：累加当前节点值，计算从根到当前节点的前缀和
            curr_sum += node.val

            # 2. 查表：寻找有多少个祖先前缀和满足 curr_sum - old_sum == targetSum
            res = prefix_count[curr_sum - targetSum]

            # 3. 登记：将当前节点的前缀和存入哈希表，供后续左右子树查询
            prefix_count[curr_sum] += 1

            # 4. 向下递归：累加左右子树中的合法路径条数（curr_sum 作为不可变参数，自动栈帧隔离）
            res += dfs(node.left, curr_sum)
            res += dfs(node.right, curr_sum)

            # 5. 后序位置（回溯注销）：左右子树均已遍历完毕，即将退栈离开当前路径
            # 必须撤销当前节点的前缀和记录，防止污染兄弟分支
            prefix_count[curr_sum] -= 1

            return res

        return dfs(root, 0)
