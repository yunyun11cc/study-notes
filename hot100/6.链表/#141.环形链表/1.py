from typing import Optional

"""
给你一个链表的头节点 head ，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 
为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。

如果链表中存在环 ，则返回 true 。 否则，返回 false 。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        # 建立哈希表索引
        visited=set()

        curr=head
        while curr:
            if curr in visited: # 先判断当前的节点之前是否已经在集合中了，如果在说明之前访问过被二次访问了是有环的
                return True
            
            visited.add(curr)
            curr=curr.next

        return False
    
    
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        # 利用快慢双指针，相遇的时候就说明链表里面有环，更优的解法，原地求解
        if head is None or head.next is None:
            return False

        slow = head
        fast = head.next
        
        # 只要兔子还能迈出两步，就继续跑
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
            
        # 兔子跑到终点了，说明没有环
        return False

        