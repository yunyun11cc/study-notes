from typing import Optional


"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
示例：
    输入：head = [1,2,3,4,5]
    输出：[5,4,3,2,1]

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        # 反转链表就是先把 NULL 作为新的头节点，不断的插入新节点
        # 最后插入完后返回最后的节点为头节点，这样最后一个节点就是 NULL
        # 要注意链表操作的统一性，对于任意一个节点都做重复相同的操作，这样不会产生特殊节点的额外判断
        
        curr,pre=head,None # 当前操作的节点
        
        while curr:
            # 存后继
            next_node=curr.next
                    
            # 插入节点
            curr.next=pre
            pre=curr
                    
            curr=next_node
        
        return pre