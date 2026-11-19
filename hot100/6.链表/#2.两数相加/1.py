from typing import Optional

"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        # 链表的开头是低位，从低位开始逐位往前加，但是加的时候要考虑到进位
        # 首先要创建新的链表，就要有一个哨兵节点来辅助链表的创建
        # 其次是对进位的考虑，为了统一操作并且最后不会漏或多出节点，这里统一操作，只有在满足所有条件的情况下才创建后继节点
        
        dummy=ListNode(0) # 哨兵节点
        p=dummy # 当前需要创建节点的前继
        carry=0 # 当前节点相加后的进位
        
        # 首先逻辑是两个链表相加后再和上一个节点的进位相加，然后加完后创建新节点，并更新进位
        # 这里为了处理链表的长短不一，当指针指向空的时候就直接赋值 0 来解决
        # 防止最后的幽灵节点漏算，当两个链表都加完以后还要再一次考虑进位是否也算完了
        
        while l1 or l2 or carry:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            
            total=v1+v2+carry # 两个链表相加并和进位相加后的总和
            carry,curr_sum=divmod(total,10) # 商做进位，余数做当前要填进链表的值
            
            p.next=ListNode(curr_sum)
            p=p.next # 创建完后继后移，为后面创建做准备
            
            # l1 和l2 分别往后移动
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
            
        return dummy.next
    
        