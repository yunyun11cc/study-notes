from typing import Optional


"""
给定单链表的头节点 head，将节点值按非递减顺序排列，返回排序后的头节点。

示例 1
输入：head = [4, 2, 1, 3]
输出：[1, 2, 3, 4]

示例 2
输入：head = [-1, 5, 3, 4, 0]
输出：[-1, 0, 3, 4, 5]

示例 3
输入：head = []
输出：[]

进阶要求是 O(n log n) 时间和 O(1) 额外空间。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1. 遍历链表，把每个节点的值收集到数组中。
# 2. 将数组排序，再按顺序覆盖原链表的节点值。
# 3. 返回原来的头节点。这一版使用 O(n) 额外空间。


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 收集值后用数组排序，逐个写回链表的现有节点。
        visited=[]
        curr=head
        while curr:
            visited.append(curr.val)
            curr=curr.next
        visited.sort()

        curr=head
        for i in range(len(visited)):
            curr.val=visited[i] # 直接原地修改原链表的值
            curr=curr.next

        return head
