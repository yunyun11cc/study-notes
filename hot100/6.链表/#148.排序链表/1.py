from typing import Optional

"""
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

示例：
输入：head = [4,2,1,3]
输出：[1,2,3,4]

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def sortList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 直接简单的暴力解，先将链表的数值存到数组中排序，然后原地的修改链表中的每一个值
        visited=[]
        curr=head
        while curr:
            visited.append(curr.val)
            curr=curr.next
        visited.sort()

        curr=head
        for i in range(len(visited)): 
            curr.val=visited[i] # 直接原地修改原链表的值
            curr=curr.next
        
        return head
    
    

       
        