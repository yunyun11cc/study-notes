from typing import Optional

"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# 就是简单的利用归并排序的思想，去逐个合并两个链表，难点在于怎么去规划这次合并链表的代码
# 这里简单的利用了哨兵节点的思想

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        p,q=list1,list2
        dummy=ListNode(0)
        pre=dummy
        
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