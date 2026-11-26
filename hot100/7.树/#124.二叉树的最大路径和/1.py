

"""
二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。


输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
"""

# Definition for a binary tree node.
from tkinter import N
from turtle import right


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
     
# 每个节点要做的操作：当前节点 node 作为汇总路径上的折点，从左边拿一条合法路径，再从右边拿一条合法路径
# 在 node 汇总以后与最大值比较更新最大值
# 为了让 node 汇总完以后向上汇报的是一条合法的直线路径，就要从左右子树中砍掉值更小的那一条路径返回        
        
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        ans = float('-inf')

        def dfs(node) -> int:
            nonlocal ans
            if not node:
                return 0

            # 1. 左右汇报 + 负资产当场清零（< 0 的分支直接舍弃）
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # 2. 双边冲榜：当前节点作为路径“拐点”，同时连通左右两腿刷新全局最高分
            ans = max(ans, node.val + left_gain + right_gain)

            # 3. 单边汇报：向上只能提供一条不拐弯的直路，挑较粗的那条腿交差
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return ans
        
        