"""
给定一个包含 m x n 个元素的矩阵，按顺时针方向螺旋遍历矩阵并返回所有元素。
示列：
输入:matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出:[1,2,3,6,9,8,7,4,5]
"""

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m=len(matrix)
        n=len(matrix[0])
        result=[]

        top, bottom, left, right = 0, m-1, 0, n-1

        while top<=bottom and left<=right:
            if top <= bottom:
                for j in range(left,right+1):
                    result.append(matrix[top][j])
                top+=1
            
            if left <= right:
                for i in range(top,bottom+1):
                    result.append(matrix[i][right])
                right-=1
            
            if top <= bottom:
                for j in range(right,left-1,-1):
                    result.append(matrix[bottom][j])
                bottom-=1
            
            if left <= right:
                for i in range(bottom,top-1,-1):
                    result.append(matrix[i][left])
                left+=1

        
        return result