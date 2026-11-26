"""
给定单链表的头节点 head。若链表有环，返回从 head 出发第一个进入环的节点，否则返回 None。
链表的连接保持原样。
示例中的 pos 是尾节点连接的位置，从 0 开始计数，-1 表示尾节点指向空。方法只接收 head。

示例 1
输入：head = [3, 2, 0, -4], pos = 1
输出：索引 1 处的节点（值为 2）

示例 2
输入：head = [1], pos = -1
输出：None
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        pass
