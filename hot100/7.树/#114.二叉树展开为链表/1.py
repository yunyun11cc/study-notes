"""给你二叉树的根结点 root ，请你将它展开为一个单链表：

展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。


输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        

"""
走到当前节点时:1.如果左孩子不为空，说明需要把左孩子挂到右边来，要去找左孩子里面最右边的节点
            2.如果左孩子为空，说明这个节点已经满足链表的特性了，直接往右子树走
"""      
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return root
        
        curr=root
        while curr:
            if curr.left:
                predecessor=curr.left # 进入到左子树中寻找最右节点
                while predecessor.right:
                    predecessor=predecessor.right
                predecessor.right=curr.right
                curr.right=curr.left
                curr.left=None
            
            curr=curr.right
        
        return root