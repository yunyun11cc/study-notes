from typing import Optional


"""
给定两个无环单链表的头节点 headA 和 headB。
若两条链表共享一段尾部，返回公共尾部的第一个节点。若无交点，返回 None。
相交要求两条链表引用同一个节点对象。调用前后链表的结构须一致。
示例中的数组列出节点值，skipA 和 skipB 给出两表各自到交点之前的节点数。

示例 1
输入：listA = [4, 1, 8, 4, 5], listB = [5, 6, 1, 8, 4, 5], skipA = 2, skipB = 3
输出：值为 8 的共享节点
解释：两个值为 1 的节点是各自链表中独立的对象。

示例 2
输入：listA = [2, 6, 4], listB = [1, 5]
输出：None
解释：两条链表各自结束，没有共享节点。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1. 两个指针分别从 headA 和 headB 出发，每轮各沿 next 前进一步。
# 2. 一个指针走到空节点后，从另一条链表的头开始走，抵消两条链表的长度差。
# 3. 两指针指向同一个对象时返回该对象，它可能是交点，也可能是 None。


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p, q = headA, headB
        while p is not q:
            # 换到对方链表时，从原始头节点重新开始。
            p = p.next if p is not None else headB
            q = q.next if q is not None else headA

        return p
