"""
给定一个 m × n 的矩阵 matrix。对原矩阵中的每个 0，将它所在的一整行和一整列置零。
直接修改原矩阵。示例输出展示修改后的矩阵。

示例 1
输入：matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
输出：[[1, 0, 1], [0, 0, 0], [1, 0, 1]]

示例 2
输入：matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
输出：[[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
"""


# 1. 先遍历原矩阵，用两个集合分别记录 0 所在的行号和列号。
# 2. 扫描完成后，将集合中记录的各行全部置零。
# 3. 再将记录的各列置零。两个集合合计占用 O(m + n) 额外空间。


class Solution(object):
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows=set()
        cols=set() # 用来存对应的行列的集合
        m=len(matrix)
        n=len(matrix[0])

        # 先收集原矩阵中的 0，避免新写入的 0 扩大置零范围。
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
