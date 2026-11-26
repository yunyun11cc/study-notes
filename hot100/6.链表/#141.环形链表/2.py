from typing import Optional


"""
给定单链表的头节点 head，判断沿 next 前进时是否会再遇到同一个节点。
存在环时返回 true，否则返回 false。
示例中的 pos 是尾节点连接的位置，从 0 开始计数，-1 表示尾节点指向空。方法只接收 head。

示例 1
输入：head = [3, 2, 0, -4], pos = 1
输出：true
解释：尾节点连回值为 2 的节点。

示例 2
输入：head = [1], pos = -1
输出：false
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1. 慢指针从头节点出发，快指针从头节点的下一个位置出发。
# 2. 慢指针每次走一步、快指针每次走两步，两者相遇说明有环。
# 3. 快指针无法再走两步时说明链表有终点，返回 false。


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 利用快慢双指针，相遇的时候就说明链表里面有环，更优的解法，原地求解
        if head is None or head.next is None:
            return False

        slow = head
        fast = head.next

        # fast.next 存在时，才可以安全地取它的下一个节点。
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next

        return False
