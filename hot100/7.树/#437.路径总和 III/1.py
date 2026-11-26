from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 递归遍历每一个节点，走所有的能向下的路，并判断当前是否已经累加到了目标和
# 每个节点要做的事：targetsum减去当前节点的值，并判断减去后是否等于0，如果等于0那说明路径合法，计数count加1
# 然后带着这个targetsum去递归当前节点的左子树和右子树
# 如果当前节点为空了就直接返回

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        
        def curr_node_path(node,targetSum):
            if node is None:
                return 0

            targetSum-=node.val
            curr_count=0
            if targetSum==0:
                curr_count+=1
            
            left_count=curr_node_path(node.left,targetSum)
            right_count=curr_node_path(node.right,targetSum)
            
            return curr_count+left_count+right_count
        

        return (curr_node_path(root,targetSum)+
                self.pathSum(root.left,targetSum)+
                self.pathSum(root.right,targetSum))
            
