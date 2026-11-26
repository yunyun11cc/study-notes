"""
给定一棵非空二叉树，求所有合法路径中的最大路径和。
路径至少包含一个节点，相邻节点之间必须有边，每个节点最多经过一次。
路径可以从任意节点开始或结束，路径和是经过的节点值之和。

示例 1
输入：root = [1, 2, 3]
输出：6
解释：路径 2 → 1 → 3 的节点值之和为 6。

示例 2
输入：root = [-10, 9, 20, null, null, 15, 7]
输出：42
解释：最优路径为 15 → 20 → 7。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. 后序计算左右子树能贡献的最大单边路径和，负数贡献按 0 处理。
# 2. 以当前节点为折点，把两侧贡献一起加上并更新全局最大路径和。
# 3. 向父节点返回当前值加上较大的一侧贡献，供父节点继续向上延伸。


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
