"""
给定单链表的头节点 head，反转整条链表，返回反转后的头节点。

示例 1
输入：head = [1, 2, 3, 4, 5]
输出：[5, 4, 3, 2, 1]

示例 2
输入：head = []
输出：[]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1. 用 pre 记录已反转部分的头节点，初始为 None。
# 2. 处理当前节点时先保存后继，再让当前节点指向 pre。
# 3. 前移 curr 和 pre，最后返回 pre 作为新头节点。


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        curr,pre=head,None # 当前操作的节点

        while curr:
            # 改写 next 前保存后继，才能继续处理剩余节点。
            next_node=curr.next

            # 插入节点
            curr.next=pre
            pre=curr

            curr=next_node

        return pre
