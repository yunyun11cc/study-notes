"""
给定一个矩阵，如果一个元素为 0，则将其所在的行和列的所有元素都设为 0。
:type matrix: List[List[int]]
:rtype: None Do not return anything, modify matrix in-place instead.
"""


class Solution(object):
    def setZeroes(self, matrix):
        """
        直观解法：
        1、遍历整个矩阵，碰到0元素就将该元素所在的行和列保存下来
        2、将行和列保存在行集合和列集合中间，这样可以保证最后的行业列是不重复的，最后的空间复杂度是O(m+n)
        3、根据保存的行列再去遍历整个矩阵将对应的位置置零
        """
        rows=set()
        cols=set() # 用来存对应的行列的集合
        m=len(matrix)
        n=len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    rows.add(i)
                    cols.add(j)
        
        for x in rows:
            for y in range(n):  # 进入对应的行，把该行所有的列都置为0
                matrix[x][y]=0

        for x in range(m):
            for y in cols:  # 进入对应的列，把该列所有的行都置为0
                matrix[x][y]=0
        
        