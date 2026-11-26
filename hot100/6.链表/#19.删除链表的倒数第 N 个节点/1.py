"""
给定单链表的头节点 head 和整数 n，删除从尾部数第 n 个节点，并返回删除后的头节点。
n 从 1 开始，且不超过链表长度。

示例 1
输入：head = [1, 2, 3, 4, 5], n = 2
输出：[1, 2, 3, 5]

示例 2
输入：head = [1], n = 1
输出：[]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1. 在头节点前放一个哨兵，快慢指针都从哨兵出发。
# 2. 让快指针先走 n 步，再让两个指针一起走到快指针位于尾节点。
# 3. 慢指针正好指向待删除节点的前驱，跳过该节点并返回哨兵之后的新表头。


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0, head)  # 删除头节点时也有前驱可用
        slow,fast=dummy,dummy

        while n>0:
            fast=fast.next
            n-=1

        while fast.next:
            slow=slow.next
            fast=fast.next

        p = slow.next  # slow 停在待删节点的前一个位置
        slow.next=p.next
        p=None

        return dummy.next
