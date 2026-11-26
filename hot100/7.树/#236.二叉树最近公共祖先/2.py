# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node is None:
                return None
            
            # 1. 自己就是目标，直接往上汇报自己
            if node == p or node == q:
                return node
                
            # 2. 去左右子树找
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 3. 左右都找到了，说明分岔口在我这，我就是最近的公共祖先
            if left and right:
                return node
            
            # 4. 只有一边找到了，把找到的那个往上传
            # （如果两边都没找到，左边就是 None，返回 None 也符合逻辑）
            return left if left else right
            
        return dfs(root)