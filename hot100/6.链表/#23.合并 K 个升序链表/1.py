"""
lists 中的每个元素都是一条非递减链表的头节点。
将所有链表合并成一条非递减链表，并返回合并后的头节点。

示例 1
输入：lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
输出：[1, 1, 2, 3, 4, 4, 5, 6]

示例 2
输入：lists = []
输出：[]

示例 3
输入：lists = [[]]
输出：[]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        pass
