

"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。


输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 利用后序遍历的特性，去左右子树找p和q，最后回到当前节点汇总，看看当前节点是不是要的那个答案
# 用ans来存最后节点的位置，给一个整数变量count，每当遇到p和q就加1，当count为2的时候就尝试去填入ans，前提是ans不为空
# 这里第一个填入ans的就是我们要打节点，因为递归自底向上的特性，第一个符合要求的节点深度一定最深


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans=None
        
        def dfs(node):
            if node is None:
                return 0
            
            left_count=dfs(node.left,count)
            right_count=dfs(node.right,count)
            
            if node==p or node==q:
                count+=1

            if count+left_count+right_count==2 and self.ans==None:
                self.ans=node
            
            return count+left_count+right_count

        dfs(root)
            
        return self.ans
        
        