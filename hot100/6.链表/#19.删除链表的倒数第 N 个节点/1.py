from typing import Optional


"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

示例：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

# 这里利用快慢指针来做到删除链表倒数第 N 个节点，这里为了能够删除正好在第一个节点的情况，要利用哨兵节点
# 先让快指针fast走N步，然后快慢指针一起往前走，直到fast.next=NULL
# 这样slow就会指向第N+1个节点

class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy=ListNode(0)
        slow,fast=dummy,dummy
        
        while n>0:
            fast=fast.next
            n-=1
            
        while fast.next:
            slow=slow.next
            fast=fast.next
            
        p=slow.next
        slow.next=p.next
        p=None
        
        return dummy.next