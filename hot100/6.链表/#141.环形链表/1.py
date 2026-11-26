from typing import Optional


"""
给定单链表的头节点 head，判断沿 next 前进时是否会再遇到同一个节点。
存在环时返回 true，否则返回 false。
示例中的 pos 是尾节点连接的位置，从 0 开始计数，-1 表示尾节点指向空。方法只接收 head。

示例 1
输入：head = [3, 2, 0, -4], pos = 1
输出：true
解释：尾节点连回值为 2 的节点。

示例 2
输入：head = [1], pos = -1
输出：false
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1. 从头节点开始遍历，用集合记录访问过的节点对象。
# 2. 再次遇到集合里已有的节点时返回 true，说明已经绕回环内。
# 3. 沿 next 走到空节点时返回 false。


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 建立哈希表索引
        visited=set()

        curr=head
        while curr:
            if curr in visited: # 先判断当前的节点之前是否已经在集合中了，如果在说明之前访问过被二次访问了是有环的
                return True

            visited.add(curr)
            curr=curr.next

        return False
