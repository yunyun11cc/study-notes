from typing import Optional


"""
给定单链表的头节点 head。如果沿链表读取的节点值正序和逆序相同，返回 true，否则返回 false。

示例 1
输入：head = [1, 2, 2, 1]
输出：true

示例 2
输入：head = [1, 2]
输出：false

示例 3
输入：head = [1, 2, 3, 2, 1]
输出：true
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1. 快指针每次走两步，慢指针每次走一步。快指针到末尾时，慢指针到达中间。
# 2. 以慢指针所在节点为起点，原地反转这一段链表。
# 3. 从原表头和反转段开头逐对比较，反转段走完即比较结束。


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 偶数长度时，slow 最终指向后半段的第一个节点。
        fast,slow=head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next

        # 反转以 slow 为头节点的链表
        curr,pre=slow,None
        while curr:
            next_node=curr.next

            curr.next=pre
            pre=curr

            curr=next_node

        p, q = pre, head
        # 以反转段的长度为准。奇数长度时，中间节点与自身比较。
        while p:
            if p.val!=q.val:
                return False
            p=p.next
            q=q.next

        return True
