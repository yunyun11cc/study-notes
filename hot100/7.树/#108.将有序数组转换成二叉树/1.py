"""
给定一个严格升序的整数数组 nums，构造一棵高度平衡的二叉搜索树，并返回根节点。
高度平衡指树中每个节点的左右子树高度之差最多为 1。

示例 1
输入：nums = [-10, -3, 0, 5, 9]
输出：[0, -10, 5, null, -3, null, 9]
解释：[0, -3, 9, -10, null, 5] 也满足要求。

示例 2
输入：nums = [1, 3]
输出：[1, null, 3]
解释：[3, 1] 也是合法结果。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. 当前数组区间为空（左边界大于右边界）时，返回空节点。
# 2. 取区间中点，用中间元素创建当前节点。
# 3. 分别用左半段、右半段递归构造左右孩子，挂接后返回当前节点。


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def dfs(left, right):  # left 和 right 都包含在当前区间内
            if left>right:
                return None

            mid = (right - left) // 2 + left  # 区间长度为偶数时取靠左的中点
            curr_node=TreeNode(nums[mid])
            curr_node.left=dfs(left,mid-1)
            curr_node.right=dfs(mid+1,right)

            return curr_node

        return dfs(0,len(nums)-1)
