from typing import Optional

"""
给定两个无环单链表的头节点 headA 和 headB。如果两个链表共享一段尾部，返回这段公共尾部的第一个节点。

如果没有交点，返回 None（题面中的 null）。

两个链表必须引用同一个节点对象才算相交。两个节点的值相同，仍可能是不同的节点。函数返回后，两个链表的结构须保持原样。


示例
A: 4 → 1 ────┐
              ├→ 8 → 4 → 5 → NULL
B: 5 → 6 → 1 ┘

返回值为 8 的共享节点。图中两个值为 1 的节点各自独立。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


        
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]: 
        """
        假设 A 的长度为 a，B 的长度为 b
        让 p 遍历完 A 区遍历 B，q 遍历完 B 去遍历 A
        这样 p 和 q 就会在相交的节点相遇
        """
        p,q=headA,headB
        while p!=q:
            p=p.next if p is not None else q
            q=q.next if q is not None else p
        
        return p