"""
两个非空链表 l1 和 l2 分别表示两个非负整数。
每个节点存一位数字，低位在前。返回两个数的和，也用低位在前的链表表示。
除了整数 0，两个输入整数的最高位都不为 0。

示例 1
输入：l1 = [2, 4, 3], l2 = [5, 6, 4]
输出：[7, 0, 8]
解释：342 + 465 = 807。

示例 2
输入：l1 = [9, 9], l2 = [1]
输出：[0, 0, 1]
解释：99 + 1 = 100。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1. 用哨兵节点创建结果链表，从两个输入链表的低位开始相加。
# 2. 每次加当前两位与进位，某一条链表已结束时这一位按 0 处理。
# 3. 用商更新进位、用余数创建节点，两表结束后还要处理末尾进位。


class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy=ListNode(0) # 哨兵节点
        p=dummy # 当前需要创建节点的前继
        carry=0 # 当前节点相加后的进位

        # 两条链表都结束后，最后一位进位仍可能需要一个新节点。
        while l1 or l2 or carry:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0

            total=v1+v2+carry # 两个链表相加并和进位相加后的总和
            carry,curr_sum=divmod(total,10) # 商做进位，余数做当前要填进链表的值

            p.next=ListNode(curr_sum)
            p=p.next # 创建完后继后移，为后面创建做准备

            # l1 和l2 分别往后移动
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None

        return dummy.next
