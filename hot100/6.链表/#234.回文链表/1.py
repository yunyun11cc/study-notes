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
        
        