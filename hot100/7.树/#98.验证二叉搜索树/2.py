class Solution:
    def isBST(self,node):
            if node is None:
                return True
            
            if self.isBST(node.left) is False:
                return False           
            if node.val <= self.prev:
                return False
            self.prev=node.val
            
            return self.isBST(node.right)
    
    def isValidBST(self, root: TreeNode | None) -> bool:
        self.prev = float('-inf')
        return self.isBST(root)