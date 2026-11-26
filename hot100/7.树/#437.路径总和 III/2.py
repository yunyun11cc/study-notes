from collections import defaultdict
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



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