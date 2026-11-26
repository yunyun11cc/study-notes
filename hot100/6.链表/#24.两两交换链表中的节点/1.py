"""
给定单链表的头节点 head，从表头开始每两个相邻节点交换一次，返回交换后的头节点。
交换通过修改连接完成。节点值保持原样，剩余的单个节点留在原位。

示例 1
输入：head = [1, 2, 3, 4]
输出：[2, 1, 4, 3]

示例 2
输入：head = [1, 2, 3]
输出：[2, 1, 3]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        pass
