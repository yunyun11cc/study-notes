from typing import Optional

"""
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
示例：
输入：head = [1,2,2,1]
输出：true

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 直接暴力解法先将链表遍历到一个数组中，然后双指针左右同时遍历数组，就可以判断当前的数组是不是回文了
        # 但是这样的做法要用到O(n)的空间
        # 先将链表后半部分反转后从头节点开始往后比较，这样就可以只哦那个到O(1)的空间
        
        # 先利用快指针每次走2个单位，慢指针走1个单位，这样快指针走完的时候慢指针就会走到链表的中间节点
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
        
        p,q=pre,head
        while q:
            if p.val!=q.val:
                return False
            p=p.next
            q=q.next
        
        return True