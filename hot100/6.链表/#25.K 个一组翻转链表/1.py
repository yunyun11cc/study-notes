"""
给定单链表的头节点 head 和正整数 k，从头开始将节点每 k 个分成一组。
翻转每个完整组中的节点连接，最后不足 k 个节点时保留它们的顺序。
节点值保持原样。返回翻转后的头节点。

示例 1
输入：head = [1, 2, 3, 4, 5], k = 2
输出：[2, 1, 4, 3, 5]

示例 2
输入：head = [1, 2, 3, 4, 5], k = 3
输出：[3, 2, 1, 4, 5]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1. 探测长度（终止条件）：从 head 往后走 k 步定位 next_head，中途提前遇到 None 说明不足 k 个，直接原样 return head
# 2. 局部反转：在 [head, next_head) 区间内反转指针，得到这一组的新头节点 prev（注意原 head 变成了本组尾巴）
# 3. 递归接力并返回：把本组尾巴 head.next 接上 reverse(next_head) 的结果，最后 return 本组新头节点 prev

class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        def reverse(node): # 这里只传入要反转的链表的第一个真实节点
            head=node
            step=0
            next_head=head
            while step<k:
                if next_head is None:
                    return head
                next_head=next_head.next # 从 head 走 k 步定位到下一个子串的头部
                step+=1
            
            # 开始反转[head, next_head)的链表
            curr,prev=head,None
            while curr!=next_head:
                # 存后继
                next_node=curr.next
                
                curr.next=prev
                prev=curr
                
                curr=next_node
            
            # 反转过后prev 是头，head 是尾
            head.next=reverse(next_head)
            return prev

        return reverse(head)
        
        
                
            
            
            
            
            