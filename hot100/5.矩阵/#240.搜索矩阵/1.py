"""
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。

如果Target在矩阵中返回True，不在矩阵中返回False
"""




class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        初步的想法就是用一个中间值进行比较，不断的缩小搜索的范围
          这里我们拿左下和右上的值来进行比较
          右上：如果相等返回true，如果小于则砍掉整列，如果大于则砍掉整行
          左下：如果相等返回true，如果小于则砍掉正行，如果大于则砍掉整列
        
        """
        
        m=len(matrix)
        n=len(matrix[0])
        top,right=0,n-1
        
        while top<=m-1 and right>=0:
            if target==matrix[top][right]:
                return True
            elif target<matrix[top][right]:
                right-=1
            else:
                top+=1
            
            
        return False
        