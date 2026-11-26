"""
给定两个按非递减顺序排列的单链表 list1 和 list2。
把两个链表的原有节点接成一个非递减链表，返回合并后的头节点。

示例 1
输入：list1 = [1, 2, 4], list2 = [1, 3, 4]
输出：[1, 1, 2, 3, 4, 4]

示例 2
输入：list1 = [], list2 = [0]
输出：[0]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1. 用哨兵节点固定合并链表的起点，两个指针分别扫描两个输入链表。
# 2. 每次比较两个当前节点，把值较小的节点接到结果末尾并前移对应指针。
# 3. 一个链表用完时，把另一条链表剩余的一段直接接上。


class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        p,q=list1,list2
        dummy=ListNode(0)
        pre=dummy

        # pre 始终指向已合并部分的最后一个节点。
        while p and q:
            if p.val<q.val:
                pre.next=p
                pre=p
                p=p.next
            else:
                pre.next=q
                pre=q
                q=q.next

        pre.next = p or q # 利用短路将pre.next自动指向当前还非空的链表

        return dummy.next
