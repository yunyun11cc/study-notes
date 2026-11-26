"""
单链表的每个节点除了 next，还有一个 random 指针，可指向原链表中的任意节点或空。
返回深拷贝的头节点。复制链表里的所有节点都必须是新对象，值及 next、random 的指向关系与原链表一致。
示例用 [值, random 下标] 表示各节点，random 下标从 0 开始，null 表示空指针。

示例 1
输入：head = [[7, null], [13, 0], [11, 1]]
输出：[[7, null], [13, 0], [11, 1]]
解释：复制链表的后两个节点分别指向复制链表的第一个和第二个节点。

示例 2
输入：head = [[1, 1], [2, 1]]
输出：[[1, 1], [2, 1]]
"""


# Definition for a linked list node with a random pointer.
class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = x
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node | None) -> Node | None:
        pass
